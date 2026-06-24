# Bridge manifest — l5r-gm (Legend of the Five Rings 5E · Rokugan)

This companion supplies the **L5R 5E ruleset** (roll-and-keep checks; the four conflicts —
skirmish · duel · intrigue · mass battle; character creation; techniques / adversaries / conditions
from all eight books) and the **Rokugan setting** to the mythic-gm engine. The engine runs the
scene / Chaos / Fate / Random-Event / Turning-Point loop and the no-softening discipline; this bridge
fills the engine's hooks so resolution routes to L5R, the oracle reads as samurai drama, and
generation, pacing, and the world reflect Rokugan. All randomness still runs through the engine's (and
l5r-gm's) scripts — honest, shown, cited. Unfilled hooks (e.g. adventure-ingest) defer to the engine.

```json
{
  "companion": "l5r-gm (Legend of the Five Rings 5E)",
  "engine": "mythic-gm>=2",
  "overrides": ["resolve","meaning","chaos","themes","generate:character","generate:element","world-tick","seeds"],
  "files": {
    "system_profile": "system-profile.md",
    "interpretation": "interpretation.md",
    "chaos": "chaos-tendency.md",
    "themes": "theme-weights.md",
    "generators": "generators/registry.md",
    "subsystems": "subsystems.md",
    "seeds": "seeds.md",
    "canon": "setting-canon.md"
  },
  "generators_map": {
    "character": { "mode": "conjunction", "table": "generators/npc_role.json",
                   "note": "re-skin to Rokugan: give the NPC a clan/family and flesh from setting-canon factions; build a rival with l5r-gm npc.py if it must fight or scheme" }
  }
}
```
