# AQBE — Agentic Quantized Benchmark Evaluation

A generalized evaluation framework for quantized LLMs in agentic workflows.

## Why AQBE

Standard LLM benchmarks (MMLU, HumanEval, GSM8K) test isolated single-turn capability.
AQBE targets the failure modes that only appear in production agentic workflows:

- Structured output reliability under token pressure
- Tool chain stability across multi-step skill files
- Schema compliance with constrained vocabularies
- Context retention across sequential tool calls
- Adversarial robustness in chat interfaces
- Thinking mode token exhaustion on structured output

## Usage

```bash
# Run all task packs with default models
python3 aqbe.py

# Custom model registry
python3 aqbe.py --models models.yaml

# Specific task pack
python3 aqbe.py --tasks task_packs/general_agentic.yaml

# Filter by category
python3 aqbe.py --category agentic

# Subset of models
python3 aqbe.py --model-filter small openai

# Custom output directory
python3 aqbe.py --output results/my_run


```

## File Structure

```
aqbe/
  aqbe.py              # Main runner — model-agnostic, task-agnostic
  models.yaml          # Model registry (endpoints, auth, params)
  task_packs/
    financial_agentic.yaml   # Financial domain tasks
    general_agentic.yaml     # Domain-agnostic agentic tasks (add your own)
  results/             # Auto-created — JSON + MD + per-model responses
```

## Adding Models

Edit `models.yaml`:

```yaml
models:
  my_model:
    label: "My Model Name"
    url: "http://localhost:8081/v1"
    model: "my-model-id"
    headers:
      Authorization: "Bearer my-key"
    temperature: 0.1
    max_tokens: 1024
    timeout: 60
```

## Adding Task Packs

Create a YAML file in `task_packs/`:

```yaml
pack_name: my_pack
tasks:
  - id: my_task
    category: reasoning
    description: "What this tests"
    system: "System prompt for the model"
    prompt: "User prompt"
    eval: regex_checks    # or: json_fields, numeric
    checks:
      - name: has_answer
        pattern: "expected.*pattern"
        case_insensitive: true
      - name: not_too_long
        max_words: 200
      - name: no_bad_word
        pattern: "forbidden"
        invert: true
```

### Eval Types

| Type | Use for | Required fields |
|---|---|---|
| `regex_checks` | Keyword presence, length, invert | `checks` list |
| `json_fields` | JSON structure validation | `expected_fields`, `expected_values` |
| `numeric` | Arithmetic correctness | `expected` dict with key: value |

## Scoring

- Each check is worth 2 points (configurable via `points` field)
- Score = (checks passed / total possible) × 100%
- Hard FAIL (0%) flags deployment blockers
- Results saved per-run with timestamp to `results/`

## Task Packs Included

| Pack | Domain | Tasks | Key failure modes tested |
|---|---|---|---|
| `financial_agentic.yaml` | Finance | 8 | Canonical paths, tool grounding, valuation reasoning |
| `general_agentic.yaml` | General | 14 | Structured output, multi-turn, edge cases, agentic harness, adversarial |

Run both together:
```bash
python3 aqbe.py --tasks task_packs/financial_agentic.yaml task_packs/general_agentic.yaml
```

## Key Findings (from initial FLAME-Q / AQBE v1 run)

- `qwen3.5-4b` non-thinking: best local model for agentic tasks (93.9%, 4.4s)
- `gemma-4-26b-a4b-it`: tied at 93.9%, fastest large model at 3.5s
- Thinking mode at ≤4b: degrades structured output — token budget exhausted by reasoning chain
- `/no_think` prefix: fixes thinking mode for qwen3.5 models on llamacpp servers
- `gpt-oss-20b`: underperforms its size — generic analysis, misses specific entities
- Models <2b: fail canonical path schema and multi-tool selection

See `EVAL_SUMMARY.md` in `model_test/` for full analysis.
