# System Profile — Legend of the Five Rings 5E   (hook: resolve)

> The resolve hook for the mythic-gm engine. **All L5R task resolution & combat route to
> l5r-gm**; the engine defers world yes/no questions, scene framing, Chaos, random events,
> and plot to itself. Precedence: this profile > rulebook > recollection.

- **Dice convention:** L5R roll-and-keep custom dice (Ring d6 + Skill d12). Express a check as
  `python3 .claude/skills/l5r-gm/scripts/dice.py check --ring R --skill S --tn T`.
  (Generic dice, if ever needed: `dice.py roll 1d10`.)
- **Core resolution:** roll **(Ring)** Ring dice + **(Skill rank)** Skill dice, resolve explosive
  successes, **keep up to Ring dice**; kept successes ≥ **TN** → success. Opposed checks compare
  successes; some checks are vs a static TN.
- **Degrees of success?** YES — bonus successes (beyond TN) buy effects; **opportunity (●)** and
  **strife (✷)** are side-effects kept alongside successes. (Drives the engine's Exceptional
  mapping when a Fate Question stands in for a rule via `--mode rule`.)
- **Stats / skills:** five **Rings** (Air · Earth · Fire · Water · Void); skill groups
  (Artisan · Social · Scholar · Martial · Trade); derived **Endurance · Composure · Focus ·
  Vigilance**; **Honor / Glory / Status**; **Void points**.
- **Defenses / health:** TN to be hit / Armor TN; fatigue vs **Endurance** (→ Incapacitated);
  strife vs **Composure** (→ **Unmasking**); **wounds → critical strikes**.
- **Combat / conflict:** four subsystems — **skirmish · duel · intrigue · mass battle**
  (`references/conflict/`). Initiative is rolled per type; rounds → turns (approach=Ring →
  action → check → apply). Defeat is **real**: death · dishonor · seppuku · capture · ruin.
- **NPC stat units:** L5R adversary / minion / rival profiles via
  `python3 .claude/skills/l5r-gm/scripts/npc.py build-rival …` (composed from the shared
  technique toolbox; prerequisites waived on grant) or `npc.py get "<name>"` for canon blocks.
  When the engine's **NPC Statistics** Fate Question is used, read its ±% result into L5R units
  (Ring/skill ranks, TNs, conflict rank).
- **Routing default:** RPG (l5r-gm) resolves **all checks, conflicts, character-gen, advancement,
  conditions, harm**. Defer to **Fate Questions** for world yes/no, "what's behind the door",
  and any uncertainty with no L5R mechanic. A check that opens a fight drops into the matching
  conflict subsystem; the engine still answers narrative beats inside it (a doubles-≤-CF Fate
  result can fire a Random Event mid-conflict).
- **Subsystems as Fate Questions:** none — L5R has a mechanic for strife, fear, taint, and
  intrigue; use those, not a Fate Question, when one applies.
