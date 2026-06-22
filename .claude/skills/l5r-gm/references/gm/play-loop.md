---
source: l5r-gm
title: The Play Loop (operational detail)
scope: gm
---

# The Play Loop

Three tiers; the discipline (SKILL.md) is on at every tier. If mythic-gm is loaded it owns the outer
tier (scene framing, Chaos, random events, world oracle, plot); you own the entire interior — every
check and every conflict.

## The check procedure (used constantly)

1. **Declare intention** — what the character is trying to accomplish, and what failure will cost
   (pre-commit the stakes).
2. **Choose ring + skill** — the *skill* is the training; the *ring* is the **approach** (Air = guile/
   grace, Earth = caution/endurance, Fire = passion/aggression, Water = adaptability, Void = insight).
3. **Set TN** (1 easy … 5 formidable; opposed = target's relevant stat).
4. **Roll:** `python3 scripts/dice.py check --ring R --skill S --tn T`. Explosive successes add dice.
5. **Keep up to Ring dice — the PLAYER chooses** (success vs. strife trade-off). Max successes = Ring.
6. **Resolve:** successes ≥ TN → success (+ bonus successes); spend **opportunity (●)**; add **strife (✷)**
   from kept dice; if total strife > composure → **UNMASK** (the samurai's feelings break through).
7. Narrate only what the dice fixed.

## Scene types
- **Narrative** — investigation, travel, roleplay; resolve with checks + the oracle ladder.
- **Downtime** — between adventures; spend XP/advance (titles), craft, recover, forge bonds, rituals.
- **Conflict** — structured time; one of the four subsystems below.

## The four conflicts (load the matching shard)
- **Skirmish** (`references/conflict/skirmishes.md` + `conflict-scenes.md` + `silhouette-range-bands-and-terrain.md`)
  — tactical melee; initiative by Vigilance; range bands; Attack/Maneuver/etc.; damage → fatigue/wounds →
  **critical strikes**; conditions (`conditions.md`); harm/death (`harm-and-healing.md`).
- **Duel** (`references/conflict/duels.md`) — formal one-on-one; set terms; the strike of the moment;
  concession; honor and glory ride on it.
- **Intrigue** (`references/conflict/intrigues.md`) — court conflict; social objectives; initiative;
  composure damage and secrets; ruin and obligation as defeat.
- **Mass battle** (`references/conflict/mass-battles.md`) — armies, battle zones, strategic objectives,
  leaders' actions; the PC's deeds swing cohesion.

## Bookkeeping checklist (end of each scene)
- Strife → composure (unmask?); honor / glory / status shifts; conditions; fatigue/wounds.
- Resources/koku; bonds; Threads updated; offscreen clocks advanced.
- Chaos Factor ±1 (mythic); overwrite `campaign-state.md`; run the SELF-AUDIT.

## NPCs / antagonists
Stat or compose with `scripts/npc.py` (they draw techniques from the same library — `build-rival`).
They **act to win**: roll their competence, use their techniques, never play them dumb.
