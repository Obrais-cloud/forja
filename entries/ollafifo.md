# ollafifo

| field | value |
|---|---|
| kind | `tool` |
| path | `/Users/braisrevalderia/ollafifo` |
| github | https://github.com/Obrais-cloud/ollafifo |
| version | — |
| created | 2026-05-28 |
| tags | ollama, proxy, fleet, concurrency |

**What it is.** Proxy HTTP de Ollama que limita concurrencia. Pasa N requests simultáneos (default 1), cola el resto. Por-modelo.

**When to reach for it.** Cuando varios clientes pegan a la vez al mismo Ollama y revientan VRAM con 500-OOM.

## Notes

*(free-form — anything you want to remember; `forja sync` won't overwrite this section.)*
