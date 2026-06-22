# System Profile — Legend of the Five Rings 5E  (for the mythic-gm seam)

- **Dice convention:** L5R roll-and-keep custom dice. Express a check as
  `python3 .claude/skills/l5r-gm/scripts/dice.py check --ring R --skill S --tn T`.
- **Core resolution:** roll (Ring) Ring d6 + (Skill rank) Skill d12, explode explosive successes, **keep
  up to Ring dice**; successes (kept) ≥ TN → success. Max successes = Ring value.
- **Degrees of success?** YES — bonus successes; plus opportunity (●) and strife (✷) as side-effects.
- **Stats:** five Rings (Air/Earth/Fire/Water/Void); skills (Artisan/Social/Scholar/Martial/Trade);
  derived Endurance/Composure/Focus/Vigilance; Honor/Glory/Status; Void points.
- **Conflict/combat:** four subsystems (skirmish, duel, intrigue, mass battle) in
  `references/conflict/`; initiative per type; defeat is real (death/dishonor/seppuku/capture/ruin).
- **NPC units:** L5R adversary/minion profiles via `.claude/skills/l5r-gm/scripts/npc.py` (compose from the shared toolbox).
- **Routing:** **route ALL task resolution & combat to l5r-gm** (`dice.py` + `references/conflict/`).
  Defer to mythic for world yes/no questions, scene framing, Chaos, random events, and plot.
- **Generation:** the oracle ladder — L5R-native generator first, else a Mythic oracle, re-skinned.
