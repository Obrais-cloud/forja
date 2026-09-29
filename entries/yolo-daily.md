# yolo-daily

| field | value |
|---|---|
| kind | `launcher` |
| path | `/Users/braisrevalderia/yolo-daily` |
| github | https://github.com/Obrais-cloud/yolo-daily |
| version | 1.1.0 |
| created | 2026-03-08 |
| tags | claude-code, yolo, launchd, autonomo, macbook |

**What it is.** Sesión diaria (02:00, launchd) de Claude Code con el skill /yolo en modo build; guarda la salida en logs/ (30 días). Corre con bypassPermissions

**When to reach for it.** Cuando quieras que Claude trabaje solo cada noche buscando y construyendo algo útil; revisar el log del día por la mañana

## Notes

*(free-form — anything you want to remember; `forja sync` won't overwrite this section.)*

**2026-09-29.** Estuvo roto del 25/08 al 29/09: `run.sh` llamaba `/opt/homebrew/bin/claude`, que desapareció al pasar Claude Code a la instalación nativa (`~/.local/bin`). Ahora lo localiza con `command -v` y lo registra en el log si falta. Reactivado por decisión de Brais sabiendo que corre con `bypassPermissions`.

