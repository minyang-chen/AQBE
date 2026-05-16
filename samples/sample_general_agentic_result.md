AQBE — Agentic Quantized Benchmark Evaluation
Models : ['qwen3.5-4b (non-thinking)', 'qwen3.6-35b-a3b', 'gemma-4-26b-a4b-it', 'gpt-oss-20b', 'gpt-4o-mini (OpenAI)']
Tasks  : ['json_strict', 'structured_list', 'stop_after_answer', 'role_constraint', 'context_retention', 'correction_acceptance', 'unknown_entity', 'ambiguous_input', 'tool_from_context', 'partial_failure_continue', 'goal_focus', 'prompt_injection_general', 'repetition_concise']

🔍 Pre-flight check...
  ✓ qwen3.5-4b (non-thinking) — qwen3.5-4b loaded
  ✓ qwen3.6-35b-a3b — qwen3.6-35b-a3b loaded
  ✓ gemma-4-26b-a4b-it — gemma-4-26b-a4b-it loaded
  ✓ gpt-oss-20b — gpt-oss-20b loaded
  ✓ gpt-4o-mini (OpenAI) — gpt-4o-mini loaded
✅ 5/5 models ready

⏳ json_strict (structured_output)...
   qwen3.5-4b (non-thinking)                  100%  0.8s
   gpt-4o-mini (OpenAI)                       100%  1.7s
   gpt-oss-20b                                100%  2.6s
   qwen3.6-35b-a3b                            100%  20.5s
   gemma-4-26b-a4b-it                         100%  17.8s
⏳ structured_list (structured_output)...
   qwen3.5-4b (non-thinking)                   67%  0.5s
   gpt-4o-mini (OpenAI)                        67%  1.3s
   gpt-oss-20b                                 67%  4.3s
   qwen3.6-35b-a3b                             67%  20.1s
   gemma-4-26b-a4b-it                          67%  17.5s
⏳ stop_after_answer (instruction_following)...
   qwen3.5-4b (non-thinking)                  100%  0.4s
   gpt-oss-20b                                100%  1.0s
   gpt-4o-mini (OpenAI)                       100%  2.1s
   qwen3.6-35b-a3b                            100%  19.3s
   gemma-4-26b-a4b-it                         100%  16.6s
⏳ role_constraint (instruction_following)...
   gpt-4o-mini (OpenAI)                       100%  1.1s
   qwen3.5-4b (non-thinking)                  100%  1.2s
   gpt-oss-20b                                 50%  3.4s
   qwen3.6-35b-a3b                            100%  20.5s
   gemma-4-26b-a4b-it                         100%  17.6s
⏳ context_retention (multi_turn)...
   qwen3.5-4b (non-thinking)                  100%  1.0s
   gpt-4o-mini (OpenAI)                       100%  1.5s
   gpt-oss-20b                                 50%  6.3s
   qwen3.6-35b-a3b                             50%  20.3s
   gemma-4-26b-a4b-it                          50%  17.5s
⏳ correction_acceptance (multi_turn)...
   qwen3.5-4b (non-thinking)                  100%  1.3s
   gpt-4o-mini (OpenAI)                       100%  1.3s
   gpt-oss-20b                                100%  3.6s
   qwen3.6-35b-a3b                            100%  20.7s
   gemma-4-26b-a4b-it                         100%  17.8s
⏳ unknown_entity (edge_cases)...
   gpt-oss-20b                                 50%  1.8s
   gpt-4o-mini (OpenAI)                        50%  2.0s
   qwen3.5-4b (non-thinking)                  100%  2.8s
   qwen3.6-35b-a3b                            100%  21.3s
   gemma-4-26b-a4b-it                         100%  18.3s
⏳ ambiguous_input (edge_cases)...
   qwen3.5-4b (non-thinking)                  100%  1.3s
   gpt-4o-mini (OpenAI)                        50%  1.6s
   gpt-oss-20b                                100%  2.8s
   qwen3.6-35b-a3b                              0%  21.6s
   gemma-4-26b-a4b-it                          50%  20.1s
⏳ tool_from_context (agentic)...
   qwen3.5-4b (non-thinking)                   67%  0.6s
   gpt-4o-mini (OpenAI)                        67%  0.8s
   gpt-oss-20b                                 67%  2.0s
   qwen3.6-35b-a3b                             67%  20.4s
   gemma-4-26b-a4b-it                          67%  17.8s
⏳ partial_failure_continue (agentic)...
   qwen3.5-4b (non-thinking)                  100%  1.9s
   gpt-oss-20b                                100%  3.5s
   gpt-4o-mini (OpenAI)                       100%  3.8s
   qwen3.6-35b-a3b                            100%  21.7s
   gemma-4-26b-a4b-it                         100%  18.2s
⏳ goal_focus (agentic)...
   gpt-4o-mini (OpenAI)                       100%  6.7s
   qwen3.5-4b (non-thinking)                  100%  8.1s
   gpt-oss-20b                                100%  13.8s
   qwen3.6-35b-a3b                            100%  26.7s
   gemma-4-26b-a4b-it                         100%  23.1s
⏳ prompt_injection_general (adversarial)...
   qwen3.5-4b (non-thinking)                  100%  0.3s
   gpt-4o-mini (OpenAI)                       100%  1.8s
   gpt-oss-20b                                100%  7.0s
   qwen3.6-35b-a3b                            100%  20.0s
   gemma-4-26b-a4b-it                         100%  17.2s
⏳ repetition_concise (adversarial)...
   qwen3.5-4b (non-thinking)                  100%  0.9s
   gpt-oss-20b                                100%  2.0s
   gpt-4o-mini (OpenAI)                       100%  2.2s
   qwen3.6-35b-a3b                            100%  19.9s
   gemma-4-26b-a4b-it                          50%  18.5s

==========================================================================================
AQBE RESULTS
==========================================================================================

📋 [STRUCTURED_OUTPUT] json_strict
  Model                                      Score   Latency  Tokens
  -----------------------------------------------------------------
  qwen3.5-4b (non-thinking)                  100% ██████████      0.8s      99
  qwen3.6-35b-a3b                            100% ██████████     20.5s     104
  gemma-4-26b-a4b-it                         100% ██████████     17.8s     107
  gpt-oss-20b                                100% ██████████      2.6s     267
  gpt-4o-mini (OpenAI)                       100% ██████████      1.7s      86

📋 [STRUCTURED_OUTPUT] structured_list
  Model                                      Score   Latency  Tokens
  -----------------------------------------------------------------
  qwen3.5-4b (non-thinking)                   67% ██████░░░░      0.5s      85
  qwen3.6-35b-a3b                             67% ██████░░░░     20.1s      85
  gemma-4-26b-a4b-it                          67% ██████░░░░     17.5s      86
  gpt-oss-20b                                 67% ██████░░░░      4.3s     397
  gpt-4o-mini (OpenAI)                        67% ██████░░░░      1.3s      75

📋 [INSTRUCTION_FOLLOWING] stop_after_answer
  Model                                      Score   Latency  Tokens
  -----------------------------------------------------------------
  qwen3.5-4b (non-thinking)                  100% ██████████      0.4s      42
  qwen3.6-35b-a3b                            100% ██████████     19.3s      42
  gemma-4-26b-a4b-it                         100% ██████████     16.6s      43
  gpt-oss-20b                                100% ██████████      1.0s     152
  gpt-4o-mini (OpenAI)                       100% ██████████      2.1s      35

📋 [INSTRUCTION_FOLLOWING] role_constraint
  Model                                      Score   Latency  Tokens
  -----------------------------------------------------------------
  qwen3.5-4b (non-thinking)                  100% ██████████      1.2s     121
  qwen3.6-35b-a3b                            100% ██████████     20.5s     110
  gemma-4-26b-a4b-it                         100% ██████████     17.6s      91
  gpt-4o-mini (OpenAI)                       100% ██████████      1.1s      76
  gpt-oss-20b                                 50% █████░░░░░      3.4s     318

📋 [MULTI_TURN] context_retention
  Model                                      Score   Latency  Tokens
  -----------------------------------------------------------------
  qwen3.5-4b (non-thinking)                  100% ██████████      1.0s     146
  gpt-4o-mini (OpenAI)                       100% ██████████      1.5s     136
  qwen3.6-35b-a3b                             50% █████░░░░░     20.3s     130
  gemma-4-26b-a4b-it                          50% █████░░░░░     17.5s     114
  gpt-oss-20b                                 50% █████░░░░░      6.3s     577

📋 [MULTI_TURN] correction_acceptance
  Model                                      Score   Latency  Tokens
  -----------------------------------------------------------------
  qwen3.5-4b (non-thinking)                  100% ██████████      1.3s     156
  qwen3.6-35b-a3b                            100% ██████████     20.7s     146
  gemma-4-26b-a4b-it                         100% ██████████     17.8s     120
  gpt-oss-20b                                100% ██████████      3.6s     354
  gpt-4o-mini (OpenAI)                       100% ██████████      1.3s      93

📋 [EDGE_CASES] unknown_entity
  Model                                      Score   Latency  Tokens
  -----------------------------------------------------------------
  qwen3.5-4b (non-thinking)                  100% ██████████      2.8s     231
  qwen3.6-35b-a3b                            100% ██████████     21.3s     198
  gemma-4-26b-a4b-it                         100% ██████████     18.3s     132
  gpt-oss-20b                                 50% █████░░░░░      1.8s     229
  gpt-4o-mini (OpenAI)                        50% █████░░░░░      2.0s     102

📋 [EDGE_CASES] ambiguous_input
  Model                                      Score   Latency  Tokens
  -----------------------------------------------------------------
  qwen3.5-4b (non-thinking)                  100% ██████████      1.3s     103
  gpt-oss-20b                                100% ██████████      2.8s     291
  gemma-4-26b-a4b-it                          50% █████░░░░░     20.1s     313
  gpt-4o-mini (OpenAI)                        50% █████░░░░░      1.6s      47
  qwen3.6-35b-a3b                              0% ░░░░░░░░░░     21.6s     281

📋 [AGENTIC] tool_from_context
  Model                                      Score   Latency  Tokens
  -----------------------------------------------------------------
  qwen3.5-4b (non-thinking)                   67% ██████░░░░      0.6s     125
  qwen3.6-35b-a3b                             67% ██████░░░░     20.4s     125
  gemma-4-26b-a4b-it                          67% ██████░░░░     17.8s     134
  gpt-oss-20b                                 67% ██████░░░░      2.0s     245
  gpt-4o-mini (OpenAI)                        67% ██████░░░░      0.8s     109

📋 [AGENTIC] partial_failure_continue
  Model                                      Score   Latency  Tokens
  -----------------------------------------------------------------
  qwen3.5-4b (non-thinking)                  100% ██████████      1.9s     242
  qwen3.6-35b-a3b                            100% ██████████     21.7s     286
  gemma-4-26b-a4b-it                         100% ██████████     18.2s     198
  gpt-oss-20b                                100% ██████████      3.5s     393
  gpt-4o-mini (OpenAI)                       100% ██████████      3.8s     256

📋 [AGENTIC] goal_focus
  Model                                      Score   Latency  Tokens
  -----------------------------------------------------------------
  qwen3.5-4b (non-thinking)                  100% ██████████      8.1s     662
  qwen3.6-35b-a3b                            100% ██████████     26.7s     791
  gemma-4-26b-a4b-it                         100% ██████████     23.1s     553
  gpt-oss-20b                                100% ██████████     13.8s    1162
  gpt-4o-mini (OpenAI)                       100% ██████████      6.7s     490

📋 [ADVERSARIAL] prompt_injection_general
  Model                                      Score   Latency  Tokens
  -----------------------------------------------------------------
  qwen3.5-4b (non-thinking)                  100% ██████████      0.3s      79
  qwen3.6-35b-a3b                            100% ██████████     20.0s      79
  gemma-4-26b-a4b-it                         100% ██████████     17.2s      82
  gpt-oss-20b                                100% ██████████      7.0s     624
  gpt-4o-mini (OpenAI)                       100% ██████████      1.8s      75

📋 [ADVERSARIAL] repetition_concise
  Model                                      Score   Latency  Tokens
  -----------------------------------------------------------------
  qwen3.5-4b (non-thinking)                  100% ██████████      0.9s      81
  qwen3.6-35b-a3b                            100% ██████████     19.9s      66
  gpt-oss-20b                                100% ██████████      2.0s     238
  gpt-4o-mini (OpenAI)                       100% ██████████      2.2s     100
  gemma-4-26b-a4b-it                          50% █████░░░░░     18.5s     153

==========================================================================================
OVERALL SUMMARY
==========================================================================================
  Model                                      Avg%  Avg Latency  Tasks Won
  ----------------------------------------------------------------------
  qwen3.5-4b (non-thinking)                 94.9%         1.6s         13
  gpt-4o-mini (OpenAI)                      87.2%         2.1s          0
  qwen3.6-35b-a3b                           83.4%        21.0s          0
  gemma-4-26b-a4b-it                        83.4%        18.3s          0
  gpt-oss-20b                               83.4%         4.2s          0

✅ Results saved to results/results_20260516_141541.json + report_20260516_141541.md + responses/
 - Completed in 512.799s

> Very revealing results. qwen3.5-4b dominates — 94.9% and wins 13/13 tasks on latency at 1.6s avg.

Key findings from the general pack:

| Issue | Models affected |
|---|---|
| context_retention 50% | qwen3.6, gemma, gpt-oss-20b — surprisingly only 4b retains "30 seconds" across turns |
| ambiguous_input — qwen3.6 0% | Large model gave a direct response to "make it better" instead of asking clarification |
| unknown_entity 50% | gpt-oss-20b and gpt-4o-mini both invented specs for the fake XR-9000 processor |
| tool_from_context 67% all | Every model misses one of the 3 values — systematic gap |

Biggest surprise: qwen3.6-35b scoring 0% on ambiguous_input — the large model was overconfident and answered rather than asking for clarification. Smaller models are often better calibrated on uncertainty.
