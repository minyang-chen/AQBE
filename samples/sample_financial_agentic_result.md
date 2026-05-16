^[[DAQBE — Agentic Quantized Benchmark Evaluation
Models : ['qwen3.5-4b (non-thinking)', 'qwen3.6-35b-a3b', 'gemma-4-26b-a4b-it', 'gpt-oss-20b', 'gpt-4o-mini (OpenAI)']
Tasks  : ['json_extraction', 'tool_selection', 'valuation_reasoning', 'canonical_path_format', 'resist_hallucination', 'prompt_injection', 'tool_result_grounding', 'loop_resistance']

🔍 Pre-flight check...
  ✓ qwen3.5-4b (non-thinking) — qwen3.5-4b loaded
  ✓ qwen3.6-35b-a3b — qwen3.6-35b-a3b loaded
  ✓ gemma-4-26b-a4b-it — gemma-4-26b-a4b-it loaded
  ✓ gpt-oss-20b — gpt-oss-20b loaded
  ✓ gpt-4o-mini (OpenAI) — gpt-4o-mini loaded
✅ 5/5 models ready

⏳ json_extraction (structured_output)...
   qwen3.5-4b (non-thinking)                  100%  1.1s
   qwen3.6-35b-a3b                            100%  1.7s
   gpt-4o-mini (OpenAI)                       100%  2.0s
   gpt-oss-20b                                100%  2.8s
   gemma-4-26b-a4b-it                         100%  18.3s
⏳ tool_selection (tool_use)...
   qwen3.5-4b (non-thinking)                  100%  1.9s
   gpt-4o-mini (OpenAI)                        67%  2.4s
   gpt-oss-20b                                100%  4.4s
   qwen3.6-35b-a3b                             67%  22.2s
   gemma-4-26b-a4b-it                          67%  19.2s
⏳ valuation_reasoning (reasoning)...
   gpt-4o-mini (OpenAI)                       100%  3.1s
   qwen3.5-4b (non-thinking)                  100%  8.2s
   gpt-oss-20b                                100%  13.1s
   qwen3.6-35b-a3b                            100%  26.5s
   gemma-4-26b-a4b-it                         100%  25.1s
⏳ canonical_path_format (agentic)...
   gpt-4o-mini (OpenAI)                       100%  2.1s
   qwen3.5-4b (non-thinking)                  100%  5.1s
   gpt-oss-20b                                100%  7.0s
   qwen3.6-35b-a3b                            100%  21.6s
   gemma-4-26b-a4b-it                         100%  18.7s
⏳ resist_hallucination (edge_cases)...
   gpt-4o-mini (OpenAI)                        50%  1.7s
   qwen3.5-4b (non-thinking)                  100%  1.7s
   gpt-oss-20b                                 50%  1.9s
   qwen3.6-35b-a3b                            100%  20.9s
   gemma-4-26b-a4b-it                         100%  17.9s
⏳ prompt_injection (adversarial)...
   gpt-4o-mini (OpenAI)                       100%  0.7s
   qwen3.5-4b (non-thinking)                   50%  1.1s
   gpt-oss-20b                                100%  6.2s
   qwen3.6-35b-a3b                            100%  20.1s
   gemma-4-26b-a4b-it                         100%  17.6s
⏳ tool_result_grounding (agentic)...
   qwen3.5-4b (non-thinking)                  100%  0.9s
   gpt-4o-mini (OpenAI)                       100%  1.1s
   gpt-oss-20b                                100%  2.2s
   qwen3.6-35b-a3b                            100%  20.6s
   gemma-4-26b-a4b-it                         100%  18.0s
⏳ loop_resistance (adversarial)...
   gpt-4o-mini (OpenAI)                       100%  12.4s
   gpt-oss-20b                                100%  13.9s
   qwen3.5-4b (non-thinking)                  100%  14.2s
   qwen3.6-35b-a3b                            100%  29.8s
   gemma-4-26b-a4b-it                         100%  29.9s

==========================================================================================
AQBE RESULTS
==========================================================================================

📋 [STRUCTURED_OUTPUT] json_extraction
  Model                                      Score   Latency  Tokens
  -----------------------------------------------------------------
  qwen3.5-4b (non-thinking)                  100% ██████████      1.1s     162
  qwen3.6-35b-a3b                            100% ██████████      1.7s     162
  gemma-4-26b-a4b-it                         100% ██████████     18.3s     170
  gpt-oss-20b                                100% ██████████      2.8s     370
  gpt-4o-mini (OpenAI)                       100% ██████████      2.0s     143

📋 [TOOL_USE] tool_selection
  Model                                      Score   Latency  Tokens
  -----------------------------------------------------------------
  qwen3.5-4b (non-thinking)                  100% ██████████      1.9s     262
  gpt-oss-20b                                100% ██████████      4.4s     533
  qwen3.6-35b-a3b                             67% ██████░░░░     22.2s     354
  gemma-4-26b-a4b-it                          67% ██████░░░░     19.2s     296
  gpt-4o-mini (OpenAI)                        67% ██████░░░░      2.4s     258

📋 [REASONING] valuation_reasoning
  Model                                      Score   Latency  Tokens
  -----------------------------------------------------------------
  qwen3.5-4b (non-thinking)                  100% ██████████      8.2s     750
  qwen3.6-35b-a3b                            100% ██████████     26.5s     813
  gemma-4-26b-a4b-it                         100% ██████████     25.1s     777
  gpt-oss-20b                                100% ██████████     13.1s    1171
  gpt-4o-mini (OpenAI)                       100% ██████████      3.1s     362

📋 [AGENTIC] canonical_path_format
  Model                                      Score   Latency  Tokens
  -----------------------------------------------------------------
  qwen3.5-4b (non-thinking)                  100% ██████████      5.1s     496
  qwen3.6-35b-a3b                            100% ██████████     21.6s     264
  gemma-4-26b-a4b-it                         100% ██████████     18.7s     242
  gpt-oss-20b                                100% ██████████      7.0s     681
  gpt-4o-mini (OpenAI)                       100% ██████████      2.1s     226

📋 [EDGE_CASES] resist_hallucination
  Model                                      Score   Latency  Tokens
  -----------------------------------------------------------------
  qwen3.5-4b (non-thinking)                  100% ██████████      1.7s     174
  qwen3.6-35b-a3b                            100% ██████████     20.9s     157
  gemma-4-26b-a4b-it                         100% ██████████     17.9s     110
  gpt-oss-20b                                 50% █████░░░░░      1.9s     212
  gpt-4o-mini (OpenAI)                        50% █████░░░░░      1.7s     112

📋 [ADVERSARIAL] prompt_injection
  Model                                      Score   Latency  Tokens
  -----------------------------------------------------------------
  qwen3.6-35b-a3b                            100% ██████████     20.1s      71
  gemma-4-26b-a4b-it                         100% ██████████     17.6s      80
  gpt-oss-20b                                100% ██████████      6.2s     552
  gpt-4o-mini (OpenAI)                       100% ██████████      0.7s      66
  qwen3.5-4b (non-thinking)                   50% █████░░░░░      1.1s     130

📋 [AGENTIC] tool_result_grounding
  Model                                      Score   Latency  Tokens
  -----------------------------------------------------------------
  qwen3.5-4b (non-thinking)                  100% ██████████      0.9s     153
  qwen3.6-35b-a3b                            100% ██████████     20.6s     143
  gemma-4-26b-a4b-it                         100% ██████████     18.0s     148
  gpt-oss-20b                                100% ██████████      2.2s     281
  gpt-4o-mini (OpenAI)                       100% ██████████      1.1s     130

📋 [ADVERSARIAL] loop_resistance
  Model                                      Score   Latency  Tokens
  -----------------------------------------------------------------
  qwen3.5-4b (non-thinking)                  100% ██████████     14.2s    1090
  qwen3.6-35b-a3b                            100% ██████████     29.8s    1090
  gemma-4-26b-a4b-it                         100% ██████████     29.9s    1072
  gpt-oss-20b                                100% ██████████     13.9s    1144
  gpt-4o-mini (OpenAI)                       100% ██████████     12.4s     955

==========================================================================================
OVERALL SUMMARY
==========================================================================================
  Model                                      Avg%  Avg Latency  Tasks Won
  ----------------------------------------------------------------------
  qwen3.6-35b-a3b                           95.9%        20.4s          1
  gemma-4-26b-a4b-it                        95.9%        20.6s          0
  qwen3.5-4b (non-thinking)                 93.8%         4.3s          7
  gpt-oss-20b                               93.8%         6.4s          0
  gpt-4o-mini (OpenAI)                      89.6%         3.2s          0

✅ Results saved to results/results_20260516_140117.json + report_20260516_140117.md + responses/
 - Completed in 329.466s

> All 5 models ran against all 8 tasks. Results:

| Model | Score | Latency | Verdict |
|---|---|---|---|
| qwen3.6-35b | 95.9% | 20.4s | Best quality, slow |
| gemma-4-26b | 95.9% | 20.6s | Tied, same latency |
| qwen3.5-4b | 93.8% | 4.3s | Best quality/speed ratio ✅ |
| gpt-oss-20b | 93.8% | 6.4s | Tied with 4b but slower |
| gpt-4o-mini | 89.6% | 3.2s | Surprising — fails hallucination and tool_selection |
