# Rokugan — solo Legend of the Five Rings 5E, run by Claude

A ready-to-play workspace for **solo / GM-less Legend of the Five Rings 5th Edition** in
**Rokugan**, with Claude Code as your Game Master. It runs the **mythic-gm v2 engine + companion**
architecture — one content-free engine, one L5R companion that fills its hooks:

| Skill | Role |
|---|---|
| **`mythic-gm`** *(engine)* | The Mythic GME 2e + Adventure Crafter engine — the oracle (Fate Questions), the Scene Test, Chaos Factor, random events, Turning Points/plot, and the no-softening discipline. Content-free and shared. Owns **pacing and the world oracle**. |
| **`l5r-gm`** *(companion)* | The L5R 5E ruleset & Rokugan setting — roll-and-keep checks, character creation, skirmish · duel · intrigue · mass battle, and content (315 techniques, 206 adversaries, 20 conditions) from all 8 books. Owns **all L5R resolution**. Ships a **`bridge/`** that fills the engine's hooks. |

The companion's **`bridge/`** wires the two into one table: the engine asks *what happens and
when*, and the bridge routes resolution to L5R, makes the oracle read as samurai drama, and supplies
Rokugan generation, pacing, and world — so the engine plays *as L5R in Rokugan*.

## How to play

Open this repo in Claude Code and say something like:

> *"Be my GM — let's start a Legend of the Five Rings campaign in Rokugan."*
> *"Continue my Rokugan game."*
> *"I want to play a Scorpion courtier caught between duty and a forbidden love."*

Claude loads the skills and takes it from **Session Zero** (or resumes your saved game). The
full rules of engagement live in [`CLAUDE.md`](CLAUDE.md) and each skill's `SKILL.md`.

## What makes it honest

Every uncertain outcome is rolled by a real script in the shell and shown to you — never
invented. Stakes are committed *before* the dice. NPCs act to win. Defeat (death, dishonor,
seppuku, capture, ruin) is real. The GM's instinct to soften the blow is treated as the enemy
of the game and actively resisted. No external dependencies — just **Python 3**.

## Layout

```
CLAUDE.md            ← the GM workflow & orchestration (start here)
.claude/skills/      ← mythic-gm (engine) + l5r-gm (companion, with its bridge/)
campaigns/           ← your saved games (one folder each); copy campaigns/_template to begin
```

## Saving your game

A campaign lives entirely in `campaigns/<your-campaign>/` — `campaign-state.md` is the save
file. **Commit that folder** to keep your game; see [`campaigns/README.md`](campaigns/README.md).

## Content note

The L5R, Mythic GME 2e, and Adventure Crafter rules/tables are bundled for **personal use**
(© their respective publishers — Edge/FFG, and Tana Pigeon / Word Mill Games). Don't
redistribute the copyrighted content.
