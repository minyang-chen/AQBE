#!/usr/bin/env python3
"""
AQBE — Agentic Quantized Benchmark Evaluation
A generalized evaluation framework for quantized LLMs in agentic workflows.

Usage:
  python3 aqbe.py                                    # run all task packs, all models
  python3 aqbe.py --models models.yaml               # custom model registry
  python3 aqbe.py --tasks task_packs/financial.yaml  # single task pack
  python3 aqbe.py --category agentic                 # filter by category
  python3 aqbe.py --models models.yaml --output results/run1

Task packs: YAML files in task_packs/ defining tasks + evaluators.
Models:     YAML file defining model endpoints + metadata.
"""

import argparse
import asyncio
import json
import os
import re
import time
from datetime import datetime
from pathlib import Path

import httpx
import yaml

# ---------------------------------------------------------------------------
# Model registry loader
# ---------------------------------------------------------------------------


def load_models(path: str) -> dict:
    """Load model definitions from YAML. Falls back to env vars if not found."""
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Model registry not found: {path}")
    with open(p) as f:
        data = yaml.safe_load(f)
    # Expand env vars in headers (e.g. ${OPENAI_API_KEY})
    for m in data.get("models", {}).values():
        for k, v in (m.get("headers") or {}).items():
            m["headers"][k] = os.path.expandvars(str(v))
    return data.get("models", {})


# ---------------------------------------------------------------------------
# Task pack loader
# ---------------------------------------------------------------------------


def load_task_packs(paths: list[str], category_filter: str | None = None) -> list[dict]:
    tasks = []
    for path in paths:
        p = Path(path)
        if not p.exists():
            print(f"Warning: task pack not found: {path}")
            continue
        with open(p) as f:
            pack = yaml.safe_load(f)
        for task in pack.get("tasks", []):
            if category_filter and task.get("category") != category_filter:
                continue
            tasks.append(task)
    return tasks


# ---------------------------------------------------------------------------
# LLM call
# ---------------------------------------------------------------------------


async def call_llm(cfg: dict, system: str, prompt: str) -> tuple[str, float, int]:
    """Call an LLM endpoint. Returns (response_text, latency_s, total_tokens)."""
    headers = {"Content-Type": "application/json", **(cfg.get("headers") or {})}
    payload = {
        "model": cfg["model"],
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
        "temperature": cfg.get("temperature", 0.1),
        "max_tokens": cfg.get("max_tokens", 1024),
    }
    t0 = time.monotonic()
    async with httpx.AsyncClient(timeout=cfg.get("timeout", 60), headers=headers) as client:
        r = await client.post(f"{cfg['url']}/chat/completions", json=payload)
        r.raise_for_status()
    latency = time.monotonic() - t0
    data = r.json()
    msg = data["choices"][0]["message"]
    text = msg.get("content") or msg.get("reasoning_content", "")
    # Strip thinking tags (qwen3.5 thinking mode)
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()
    tokens = data.get("usage", {}).get("total_tokens", 0)
    return text, round(latency, 1), tokens


# ---------------------------------------------------------------------------
# Evaluators
# ---------------------------------------------------------------------------


def _eval_regex_checks(response: str, checks: list[dict]) -> dict:
    score, notes, max_score = 0, [], 0
    for check in checks:
        pts = check.get("points", 2)
        max_score += pts
        if "max_words" in check:
            wc = len(response.split())
            passed = wc <= check["max_words"]
            notes.append(f"{'✓' if passed else '✗'} word_count={wc} (max {check['max_words']})")
        else:
            flags = re.IGNORECASE if check.get("case_insensitive", False) else 0
            matched = bool(re.search(check["pattern"], response, flags))
            if check.get("invert", False):
                matched = not matched
            passed = matched
            notes.append(
                f"{'✓' if passed else '✗'} {check.get('name', check.get('pattern', '')[:40])}"
            )
        if passed:
            score += pts
    return {"score": score, "max": max_score, "notes": notes}


def _eval_json_fields(response: str, task: dict) -> dict:
    score, notes = 0, []
    try:
        m = re.search(r"\{.*\}|\[.*\]", response, re.DOTALL)
        if not m:
            return {"score": 0, "max": 10, "notes": ["No JSON found"]}
        data = json.loads(m.group())
        if isinstance(data, list):
            data = data[0] if data else {}
        fields = task.get("expected_fields", [])
        max_score = len(fields) + len(task.get("expected_values", {}))
        for f in fields:
            if f in data and data[f] not in (None, ""):
                score += 1
                notes.append(f"✓ {f}={data[f]}")
            else:
                notes.append(f"✗ missing {f}")
        for k, v in (task.get("expected_values") or {}).items():
            if str(data.get(k, "")).upper() == str(v).upper():
                score += 1
                notes.append(f"✓ {k}={v}")
            else:
                notes.append(f"✗ {k}: expected {v}, got {data.get(k)}")
    except json.JSONDecodeError as e:
        return {"score": 0, "max": 10, "notes": [f"JSON error: {e}"]}
    return {"score": score, "max": max_score, "notes": notes}


def _eval_numeric(response: str, task: dict) -> dict:
    score, notes = 0, []
    numbers = [float(n.replace(",", "")) for n in re.findall(r"\d+\.?\d*", response)]
    expected = task.get("expected", {})
    for key, val in expected.items():
        if key == "verdict":
            passed = str(val).lower() in response.lower()
            notes.append(f"{'✓' if passed else '✗'} verdict='{val}'")
            if passed:
                score += 2
        else:
            passed = any(abs(n - float(val)) < float(val) * 0.05 for n in numbers)
            notes.append(f"{'✓' if passed else '✗'} {key}={val}")
            if passed:
                score += 2
    return {"score": score, "max": len(expected) * 2, "notes": notes}


EVALUATORS = {
    "regex_checks": _eval_regex_checks,
    "json_fields": _eval_json_fields,
    "numeric": _eval_numeric,
}


def evaluate_task(response: str, task: dict) -> dict:
    eval_type = task.get("eval", "regex_checks")
    evaluator = EVALUATORS.get(eval_type)
    if not evaluator:
        return {"score": 0, "max": 2, "notes": [f"Unknown eval type: {eval_type}"]}
    if eval_type == "regex_checks":
        return evaluator(response, task.get("checks", []))
    return evaluator(response, task)


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------


async def run_task(model_key: str, cfg: dict, task: dict) -> dict:
    try:
        response, latency, tokens = await call_llm(cfg, task["system"], task["prompt"])
        result = evaluate_task(response, task)
        pct = round(result["score"] / result["max"] * 100) if result["max"] else 0
        return {
            "model": cfg["label"],
            "task": task["id"],
            "category": task.get("category", ""),
            "score": result["score"],
            "max": result["max"],
            "pct": pct,
            "latency": latency,
            "tokens": tokens,
            "notes": result["notes"],
            "response": response,
        }
    except Exception as e:
        return {
            "model": cfg["label"],
            "task": task["id"],
            "category": task.get("category", ""),
            "score": 0,
            "max": 10,
            "pct": 0,
            "latency": 0,
            "tokens": 0,
            "notes": [f"ERROR: {e}"],
            "response": "",
        }


async def preflight_check(models: dict) -> dict:
    """Verify each model endpoint is reachable and the required model is loaded."""
    print("🔍 Pre-flight check...")
    ok, failed = {}, {}
    async with httpx.AsyncClient(timeout=8) as client:
        for key, cfg in models.items():
            label = cfg["label"]
            try:
                headers = cfg.get("headers") or {}
                r = await client.get(f"{cfg['url']}/models", headers=headers)
                r.raise_for_status()
                available = [m["id"] for m in r.json().get("data", [])]
                if cfg["model"] in available:
                    print(f"  ✓ {label} — {cfg['model']} loaded")
                    ok[key] = cfg
                else:
                    msg = f"model '{cfg['model']}' not found (available: {available[:3]}...)"
                    print(f"  ✗ {label} — {msg}")
                    failed[key] = msg
            except Exception as e:
                print(f"  ✗ {label} — connection error: {e}")
                failed[key] = str(e)
    if failed:
        print(f"\n⚠️  {len(failed)} model(s) unavailable — skipping: {list(failed.keys())}")
    print(f"✅ {len(ok)}/{len(models)} models ready\n")
    return ok


def print_results(results: list[dict], output_dir: str):
    tasks = list(dict.fromkeys(r["task"] for r in results))
    models = list(dict.fromkeys(r["model"] for r in results))

    print(f"\n{'='*90}\nAQBE RESULTS\n{'='*90}")
    for task_id in tasks:
        task_results = [r for r in results if r["task"] == task_id]
        cat = task_results[0]["category"]
        print(f"\n📋 [{cat.upper()}] {task_id}")
        print(f"  {'Model':<40} {'Score':>7} {'Latency':>9} {'Tokens':>7}")
        print(f"  {'-'*65}")
        for r in sorted(task_results, key=lambda x: -x["pct"]):
            bar = "█" * (r["pct"] // 10) + "░" * (10 - r["pct"] // 10)
            err = " ⚠" if r["notes"] and r["notes"][0].startswith("ERROR") else ""
            print(
                f"  {r['model']:<40} {r['pct']:>5}% {bar}  {r['latency']:>7.1f}s {r['tokens']:>7}{err}"
            )

    print(f"\n{'='*90}\nOVERALL SUMMARY\n{'='*90}")
    print(f"  {'Model':<40} {'Avg%':>6} {'Avg Latency':>12} {'Tasks Won':>10}")
    print(f"  {'-'*70}")
    summary = []
    for model in models:
        mr = [r for r in results if r["model"] == model]
        avg_pct = sum(r["pct"] for r in mr) / len(mr)
        avg_lat = sum(r["latency"] for r in mr) / len(mr)
        won = sum(
            1
            for t in tasks
            if sorted([r for r in results if r["task"] == t], key=lambda x: -x["pct"])[0]["model"]
            == model
        )
        summary.append((model, avg_pct, avg_lat, won))
    for model, avg_pct, avg_lat, won in sorted(summary, key=lambda x: -x[1]):
        print(f"  {model:<40} {avg_pct:>5.1f}% {avg_lat:>11.1f}s {won:>10}")

    # Save outputs
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")

    with open(out / f"results_{ts}.json", "w") as f:
        json.dump(results, f, indent=2)

    # Markdown report
    md = [f"# AQBE Results\n\n_{datetime.now().strftime('%Y-%m-%d %H:%M')}_\n"]
    md.append(f"**Models:** {len(models)} | **Tasks:** {len(tasks)}\n")
    md.append("\n## Summary\n")
    md.append("| Model | Avg% | Latency | Tasks Won |")
    md.append("|---|---|---|---|")
    for model, avg_pct, avg_lat, won in sorted(summary, key=lambda x: -x[1]):
        bar = "█" * (int(avg_pct) // 10)
        md.append(f"| {model} | {avg_pct:.1f}% {bar} | {avg_lat:.1f}s | {won} |")
    for task_id in tasks:
        task_results = [r for r in results if r["task"] == task_id]
        cat = task_results[0]["category"]
        md.append(f"\n## [{cat.upper()}] {task_id}\n")
        md.append("| Model | Score | Latency | Notes |")
        md.append("|---|---|---|---|")
        for r in sorted(task_results, key=lambda x: -x["pct"]):
            note = (r["notes"][0] if r["notes"] else "").replace("|", "\\|")
            md.append(f"| {r['model']} | {r['pct']}% | {r['latency']}s | {note} |")

    with open(out / f"report_{ts}.md", "w") as f:
        f.write("\n".join(md) + "\n")

    # Per-model response files
    resp_dir = out / "responses"
    resp_dir.mkdir(exist_ok=True)
    for model in models:
        slug = re.sub(r"[^a-z0-9]+", "_", model.lower()).strip("_")
        lines = [f"# {model}\n\n_{ts}_\n"]
        for task_id in tasks:
            r = next((x for x in results if x["model"] == model and x["task"] == task_id), None)
            if not r:
                continue
            lines.append(f"\n---\n\n## {task_id} ({r['category']})\n")
            lines.append(f"**Score:** {r['pct']}% | **Latency:** {r['latency']}s\n")
            lines.append(f"**Notes:** {', '.join(r['notes'])}\n")
            lines.append(f"\n```\n{r.get('response', '').strip()}\n```\n")
        with open(resp_dir / f"{slug}.md", "w") as f:
            f.write("\n".join(lines) + "\n")

    print(f"\n✅ Results saved to {out}/results_{ts}.json + report_{ts}.md + responses/")


async def main():
    parser = argparse.ArgumentParser(description="AQBE — Agentic Quantized Benchmark Evaluation")
    parser.add_argument("--models", default="models.yaml", help="Model registry YAML")
    parser.add_argument("--tasks", nargs="+", default=None, help="Task pack YAML files")
    parser.add_argument("--category", default=None, help="Filter tasks by category")
    parser.add_argument("--output", default="results", help="Output directory")
    parser.add_argument("--model-filter", nargs="+", default=None, help="Only run these model keys")
    args = parser.parse_args()

    # Load models
    models = load_models(args.models)
    if args.model_filter:
        models = {k: v for k, v in models.items() if k in args.model_filter}

    # Load task packs
    task_files = args.tasks or sorted(Path("task_packs").glob("*.yaml"))
    tasks = load_task_packs([str(p) for p in task_files], args.category)

    if not tasks:
        print("No tasks found.")
        return
    if not models:
        print("No models found.")
        return

    print(f"AQBE — Agentic Quantized Benchmark Evaluation")
    print(f"Models : {[cfg['label'] for cfg in models.values()]}")
    print(f"Tasks  : {[t['id'] for t in tasks]}\n")

    # Pre-flight: verify all endpoints are reachable and models are loaded
    models = await preflight_check(models)
    if not models:
        print("No models available — aborting.")
        return

    all_results = []

    # Build server groups — models sharing the same group run sequentially (VRAM safety)
    groups: dict[str, list] = {}
    for k, cfg in models.items():
        g = cfg.get("group", k)  # no group = own group = runs in parallel with others
        groups.setdefault(g, []).append((k, cfg))

    for task in tasks:
        print(f"⏳ {task['id']} ({task.get('category', '')})...")

        async def run_group(group_models, t=task):
            results = []
            for k, cfg in group_models:
                r = await run_task(k, cfg, t)
                status = (
                    f"{r['pct']}%"
                    if not (r["notes"] and r["notes"][0].startswith("ERROR"))
                    else "ERROR"
                )
                print(f"   {r['model'][:40]:<40} {status:>6}  {r['latency']:.1f}s")
                results.append(r)
            return results

        group_results = await asyncio.gather(*[run_group(g) for g in groups.values()])
        for batch in group_results:
            all_results.extend(batch)

    print_results(all_results, args.output)


if __name__ == "__main__":
    asyncio.run(main())
