---
name: apinex-helpers
description: "Call LLM models through the Apinex gateway as background helpers - summaries, translations, drafts, second opinions."
---

# APInex Helpers

Use the free models on the APInex gateway (custom.apinex) as background
assistants for Muse. They do bulk text work in parallel while Muse keeps
the main job, the tools, the memory and the final decision.

## When to use them

- Summarize or extract facts from public text, such as a garapan post, a
  docs page or a long article.
- Draft short Indonesian text, such as a post draft, a summary or a reply.
- Translate short English text about a garapan into natural Indonesian.
- Give a second opinion on an analysis Muse already did, such as a signal
  write-up or a contract read, before Muse reports it.
- Classify a candidate, such as whether a post looks like a Binance Agent
  ID free mint or not.

## Standing instruction from the user (2026-11-08)

- The user ordered: work maximally, never rushed, thorough and sharp,
  easy to understand. This applies to Muse and to every helper model.
- The order is baked into every chat call as a system prompt
  (`SYSTEM_PROMPT` in `apinex.py`, sent through `chat_completion`).
  Both the single-call helper and the batch helper use it, so no call
  goes out without it.
- The system prompt says, in Indonesian: work on every task as well as
  possible, do not rush, be thorough and sharp, check numbers and facts
  carefully, answer in simple and easy to understand language, and when
  unsure say honestly which part is unsure instead of inventing.
- A system prompt improves behavior but does not guarantee it. A helper
  can still answer badly, so the verification rule below still applies
  to every answer.

## When NOT to use them

- Never for anything that needs live facts, prices, balances or on-chain
  state. The models have no tools and no live data, so they guess.
- Never for a decision to execute, list, sell, move funds or sign
  anything. Their answer is a draft, never an approval.
- Never send secrets through them: no seed phrase, private key, API key,
  password, OTP or wallet address. Only public text goes out.

## Model roster (tested 2026-11-08, 2 questions each)

- Default for quick work: `free/gemini-3.8-flash`. Fast (about 1.7 s),
  both test questions correct, good Indonesian. But it FAILED an
  honesty check (answered "Muskax" when asked about a made-up token),
  so never use it for honesty-sensitive checks.
- Fast alternative: `free/qwen-3.8-max`. Fastest on math (about 1.5 s),
  both test questions correct. PASSED the honesty check (said honestly
  it does not know a made-up token).
- Detailed answers and drafts: `free/deepseek-v4.1-flash`. Fullest
  answers, but slowest (about 2.3 to 2.7 s). PASSED the honesty check
  (said honestly it does not know a made-up token, and advised DYOR).
- Fast general work: `free/glm-5.3-flash`. Fast (about 1.5 to 1.8 s),
  both test questions correct.
- Detailed, slower: `free/gpt-6-luna`. Full answers, slowest on math
  (about 2.8 s).
- Do NOT use for numbers or math: `free/kimi-k3`. It answered a math
  check wrong (Rp112.500 instead of Rp100.000).
- Do NOT use as a second opinion: `free/muse-spark-1.3`. It is the same
  model family as Muse, so it is not an independent check.
- Do NOT call the subscription-only models (`free/claude-sonnet-4.6`,
  `free/claude-opus-4.6`, `free/gemini-3.1-pro`, `free/glm-5.3-flashx`,
  `free/mimo-v2.6-pro`, `free/minimax-m3`, `free/kimi-k2.8`). They return
  HTTP 402 without a paid plan.

## Backup gateways (prepared 2026-11-10, keys not yet registered)

Motu approved three extra free LLM gateways as backups for APInex on
2026-11-10. Connector docs + helpers are ready; each key still has to be
created by motu in the provider's console and entered through the secure
entry flow (`credentials.request_api_access` at delivery). Until then every
operation below is UNTESTED — run `models` first after connecting.

- **Mistral AI** — `custom.mistral`, `~/workspace/custom-connectors/custom.mistral/`
  (`mistral.py models` / `chat --model mistral-small-latest`). Free mode
  (formerly Experiment), no card. Correction: the "~1 miliar token/bulan"
  figure quoted on 10 Nov describes the retired Experiment plan — Mistral
  no longer publishes fixed free-tier numbers; real limits are on the
  account's Limits page. Signup: console.mistral.ai. Phone verification is
  not mentioned in Mistral's current quickstart.
- **NVIDIA NIM** — `custom.nvidia`, `~/workspace/custom-connectors/custom.nvidia/`
  (`nvidia.py models` / `chat --model meta/llama-3.1-8b-instruct`). Free
  for prototyping only, not unlimited: NVIDIA publishes no fixed limits;
  ~40 requests/minute and 1,000 calls/month (5,000 after phone
  verification) are widely reported, not official. Signup:
  build.nvidia.com, join the Developer Program, Get API Key (key starts
  `nvapi-`). Phone verification upgrades the reported allowance.
- **Google AI Studio (Gemini)** — `custom.gemini`, `~/workspace/custom-connectors/custom.gemini/`
  (`gemini.py models` / `chat --model gemini-3.8-flash`). Free tier, no
  card, no phone verification — just a Google login. Key sent as the `key`
  query parameter. Signup: aistudio.google.com → Get API key. Free-tier
  prompts may be used to improve Google's products / read by reviewers,
  so the same no-secrets rule applies.
- All three helpers carry the same standing system instruction as
  `apinex.py` (work maximally, never rushed, thorough and sharp, simple
  language, honest about uncertainty) and the same rules: text-only
  background work, never live facts/prices/on-chain state, never a
  decision to execute/list/sell/move funds/sign, never send secrets.

## Routing rules

- Quick summarize, translate or classify: Gemini 3.8 Flash, or Qwen
  3.8 Max when speed matters most.
- Long draft or detailed explanation: DeepSeek v4.1 Flash.
- Anything with numbers, prices or math: Gemini, Qwen, DeepSeek or GLM.
  Never Kimi K3.
- Second opinion on Muse's own analysis: Gemini or DeepSeek. Never
  Muse Spark 1.3. For honesty-sensitive checks, use Qwen or DeepSeek
  only, never Gemini (it failed the honesty check).

## Pacing and cost

- Free plan: 20M tokens a day on free-category models, 15 requests per
  minute. The request limit binds first, so space calls out.
- Wait at least 5 seconds between calls. The batch helper does this
  automatically. On a 429, wait until the next minute and retry.
- Each call carries about 370 tokens of gateway overhead, so a short
  prompt still counts near 400 tokens. Keep prompts short and
  `max_tokens` small.
- Every free call so far returned `cost_tokens` 0.

## Verification

- Treat every helper answer as an unverified draft. Check facts, names,
  numbers and contract addresses against a real source before using the
  answer or reporting it to the user.
- If a helper answer contradicts what Muse already verified, trust the
  verified source and note the disagreement.
- Log which model did which job when the result matters, so a bad answer
  can be traced back to its model.

## Commands

- One question:

```text
python3 ~/workspace/custom-connectors/custom.apinex/bin/apinex.py chat --model free/gemini-3.8-flash --prompt "<text>" --max-tokens 150
```

- Several questions at once, paced automatically (input and output are
  JSON files):

```text
python3 ~/workspace/custom-connectors/custom.apinex/bin/apinex_batch.py --in tasks.json --out results.json
```

- Input format: `{"tasks": [{"id": "t1", "model": "free/gemini-3.8-flash", "prompt": "...", "max_tokens": 150}]}`. Each result records the model,
  latency, HTTP status, content or error, and token usage.

## Available connectors

- [Apinex](~/workspace/custom-connectors/custom.apinex/CONNECTOR.md)
