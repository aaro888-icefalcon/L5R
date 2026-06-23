# Generator Index — Rokugan / L5R 5E   (hooks: generate:*)
# need | when it's called | table(s) | mode (replace | conjunction | default)
| need                 | when called                          | table(s)                                              | mode        |
|----------------------|--------------------------------------|-------------------------------------------------------|-------------|
| new NPC (generic)    | any new Character invoked            | AC Character Crafter **+** `family_name.json` + `given_name.json` + `npc_role.json` | conjunction |
| name (person)        | a named samurai/commoner is needed   | `family_name.json` + `given_name.json` (clan = soft sort) | replace     |
| location / place     | a scene needs a place                | `location.json`                                       | replace     |
| antagonist / rival   | a statted foe is needed              | `scripts/npc.py build-rival …` (L5R units; prereqs waived) | replace     |
| named adversary      | a canon stat block is wanted         | `scripts/npc.py get "<name>"` / `lookup.py`           | replace     |
| technique / school / condition / clan | content lookup, not a roll | `scripts/lookup.py …`                                 | replace     |
| generic inspiration  | Discover Meaning, no specific need   | Mythic Elements / Meaning pair                        | default     |

# NOTES
# - "conjunction" = roll the companion table AND layer it on the engine's AC Character Crafter
#   (Special Trait + Identity + Descriptors), then re-skin the whole to Rokugan.
# - Clan is a SOFT sort, never a gate — an out-of-clan family/name/technique is a story hook.
# - Anything not listed -> Mythic/AC default, re-skinned to Rokugan.
# - JSON tables are list_d100 (coverage 100, built by ./build.py), rolled with:
#     python3 .claude/skills/mythic-gm/scripts/dice.py table \
#         .claude/skills/l5r-gm/bridge/generators/<name>.json
# - L5R content lookups & NPC composition are NOT random tables; they are the l5r-gm
#   scripts (lookup.py / npc.py) and own all rules detail.
