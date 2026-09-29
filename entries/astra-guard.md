# astra-guard

| field | value |
|---|---|
| kind | `script` |
| path | `/Users/braisrevalderia/astra-guard` (instalado en `~/.local/bin/astra-guard.py` de MacBook, mini y Studio) |
| github | https://github.com/Obrais-cloud/astra-guard |
| version | 0.4.0 |
| created | 2026-09-28 |
| tags | models, fleet, guard, launchd, codex, hermes, openclaw, gpt-6-astra, corsair |

**What it is.** Guardián de modelos: mantiene gpt-6-astra como principal y Corsair qwen3.8:27b como respaldo en Codex, Hermes y el canónico de OpenClaw; restaura con copia de seguridad y avisa por Telegram

**When to reach for it.** Cuando algo (una actualización, un agente, un cambio manual) pueda cambiar el modelo principal o la cadena de respaldo de la flota y quieras que vuelva solo a lo decidido

## Notes

*(free-form — anything you want to remember; `forja sync` won't overwrite this section.)*

**Despliegue (2026-09-28).** Mismo script en MacBook, mac mini y Mac Studio: `~/.local/bin/astra-guard.py` + launchd `com.fleet.astra-guard` (cada 30 min y al arrancar). Log: `~/Library/Logs/astra-guard.log`.

**Qué vigila.**
- Codex (`~/.codex/config.toml`): `model = "gpt-6-astra"`.
- Hermes (`~/.hermes/config.yaml`): la cadena `fallback_providers` = Corsair qwen3.8:27b → gpt-5.6-terra. Solo toca un Hermes cuyo modelo principal ya sea astra (el principal lo impone `hermes-config-watchdog`).
- OpenClaw: solo comprueba el canónico (`models-canonical.json`); lo impone `auto-repair.sh`.

**Cambiar la decisión (v0.3).** En `~/astra-guard/astra-guard.py`: `CODEX_PRIMARY`, `HERMES_PRIMARY`, `OPENCLAW_DEFAULT` y `HERMES_FB`; después `./deploy.sh` (pruebas + instala en MacBook, mini y Studio + compara huella), y solo entonces cambiar las configuraciones (canónicos primero).

**Disponibilidad GPT-6 (2026-09-29).** Con la cuenta de ChatGPT, en OpenClaw/Hermes solo funciona gpt-6-astra; sol y luna dan 400 "not supported when using Codex with a ChatGPT account" (en el Codex CLI del MacBook sí responden). Un reparto astra/sol se intentó y se revirtió.

**Incidente v0.1 (2026-09-28).** Una regex con `re.S` (DOTALL) borró ~900 líneas del `config.yaml` de Hermes en el mini y tocó un Hermes local ajeno en el MacBook. Restaurado en ~2 min desde sus copias `.bak-*-astra-guard`. v0.2: sin DOTALL y probado contra copias antes de instalar. Lección: nunca `re.S` para bloques YAML; probar guardianes que reescriben config contra copias.

**v0.4 (2026-09-29).** Avisa por Telegram (una vez por actualización) si el gateway de OpenClaw corre con un Node que Homebrew ha borrado; en ese estado el proveedor openai falla con `spawn … ENOENT` y los agentes caen a los respaldos. Arreglo: reiniciar `ai.openclaw.gateway` con disco holgado.
