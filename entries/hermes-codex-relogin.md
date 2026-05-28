# hermes-codex-relogin

| field | value |
|---|---|
| kind | `script` |
| path | `/Users/braisrevalderia/bin/hermes-codex-relogin.sh` |
| github | — |
| version | — |
| created | 2026-05-27 |
| tags | hermes, codex, fleet, ops |

**What it is.** Script local que automatiza la cadena: reaper de codex app-server → codex login --device-auth en macmini → kickstart del gateway hermes → smoke test gpt-5.5.

**When to reach for it.** Cuando hermes falla con refresh_token_reused / context overflow. Se invoca a secas. Cubre el patrón hermes_codex_token_consumed_pattern.

## Notes

*(free-form — anything you want to remember; `forja sync` won't overwrite this section.)*
