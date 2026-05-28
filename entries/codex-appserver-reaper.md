# codex-appserver-reaper

| field | value |
|---|---|
| kind | `service` |
| path | `macmini:/Users/remotework/.openclaw/scripts/codex-appserver-reaper.py` |
| github | — |
| version | — |
| created | 2026-05-27 |
| tags | hermes, codex, fleet, cron |

**What it is.** Reaper cron */15 que mantiene un solo @openclaw/codex app-server vivo en macmini; mata los huérfanos que comparten/queman el refresh token de ChatGPT.

**When to reach for it.** Activo en cron de macmini — no se invoca manual. Ver ~/.hermes/logs/codex-reaper.log para auditar reaps.

## Notes

*(free-form — anything you want to remember; `forja sync` won't overwrite this section.)*
