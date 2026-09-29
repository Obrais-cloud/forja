# fleet-health

| field | value |
|---|---|
| kind | `script` |
| path | `/Users/braisrevalderia/fleet-health` (desplegado en `macmini:~/.openclaw/scripts/`) |
| github | https://github.com/Obrais-cloud/fleet-health |
| version | 2026.09.29 |
| created | 2026-07-21 |
| tags | fleet, health, monitoring, launchd, macmini, runbook |

**What it is.** Salud de la flota: comprueba que cada servicio SIRVE (HTTP/launchd/FDs/almacenamiento/modelos), no solo que exista; tabla humana o --check con alertas solo en cambios. Estados UP / DEGRADED / DOWN / OFF (desactivado a propósito)

**When to reach for it.** Primer paso ante cualquier problema de la flota (lo pide el FLEET-RUNBOOK): ssh macmini 'bash ~/.openclaw/scripts/fleet-health.sh'

## Notes

*(free-form — anything you want to remember; `forja sync` won't overwrite this section.)*

**2026-09-29.** Añadido el estado **OFF**: un servicio con `launchctl disable` ya no cuenta como caído (antes paperclip salía DOWN aunque se desactivó a propósito el 20/09). Backup `fleet-health.sh.bak-*-pre-off` en el mini. Repo privado desde 2026-09-29: `./deploy.sh` instala en el mini con copia de seguridad y pasada real; `./pull.sh` trae cambios hechos directamente en el mini.

