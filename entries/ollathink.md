# ollathink

| field | value |
|---|---|
| kind | `tool` |
| path | `/Users/braisrevalderia/ollathink` |
| github | — |
| version | 0.1.0 |
| created | 2026-05-27 |
| tags | ollama, proxy, thinking, fleet |

**What it is.** Proxy transparente que normaliza modelos thinking de Ollama: inyecta think:false para Qwen3*/DeepSeek-R1/QwQ/gpt-oss/MiniMax-M2/GLM-Z/etc. y elimina <think> de las respuestas (streaming y no-streaming, /api/* y /v1).

**When to reach for it.** Cuando un cliente recibe respuestas vacías o ensuciadas con <think>...</think> de modelos híbridos. Apuntas el cliente a http://localhost:11533 y olvidas el problema. Encaja en la cadena → ollathink → ollafifo → ollasecret → ollama.

## Notes

*(free-form — anything you want to remember; `forja sync` won't overwrite this section.)*
