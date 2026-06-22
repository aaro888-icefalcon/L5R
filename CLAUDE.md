# Rokugan — a solo Legend of the Five Rings 5E table, run by Claude

This repository is a turnkey workspace for playing **Legend of the Five Rings 5th Edition**
solo (or GM-less) in **Rokugan**, with Claude as the Game Master. Two skills do the work:

- **`l5r-gm`** — the L5R 5E engine: roll-and-keep checks, character creation, the four
  conflicts (skirmish · duel · intrigue · mass battle), techniques/adversaries/conditions
  pulled from all 8 books, and the giri-vs-ninjō samurai drama. **Owns all L5R resolution.**
- **`mythic-gm`** — the Mythic GME 2e + Adventure Crafter engine: the oracle (Fate
  Questions), scene pacing, Chaos Factor, random events, and plot. **Owns pacing & the world oracle.**

They are designed to interlock: `l5r-gm` explicitly *defers to* `mythic-gm` for the oracle,
scene framing, and plot whenever `mythic-gm` is present. This repo runs **both, together.**

---

## ▶️ To play

When the user wants to **play / start / continue** a game in Rokugan (triggers: "L5R",
"Legend of the Five Rings", "Rokugan", "be my GM", "let's play a samurai", "continue my
campaign", a clan name, "duel/intrigue/skirmish/mass battle"):

1. **Load both skills.** Invoke the **`l5r-gm`** skill (it is the primary). It will operate
   the **`mythic-gm`** skill for oracle/pacing/plot. If only the oracle is wanted with no L5R
   rules, `mythic-gm` can run alone — but for a Rokugan game, always run the pair.
2. **Find the campaign.** Look in `campaigns/`. If a campaign folder with a
   `campaign-state.md` exists, **continue it**. Otherwise run **Session Zero** to create one.
3. **Follow the skills' play loop and discipline verbatim.** This file is the orchestrator and
   the repo map; the *authoritative* rules-of-engagement live in each skill's `SKILL.md`.

> The skills' `SKILL.md` files assume you operate from inside the skill directory. **In this
> repo, always invoke scripts by their full path from the repo root** (see Quick Reference),
> and treat **`campaigns/<name>/`** as the "campaign folder" they refer to.

---

## The seam — who owns what (do not blur it)

| Concern | Engine | Mechanism |
|---|---|---|
| Task checks, TN, strife, opportunity, unmasking | **l5r-gm** | `l5r-gm/scripts/dice.py check …` |
| Skirmish · duel · intrigue · mass battle | **l5r-gm** | `l5r-gm/references/conflict/` + `dice.py` |
| Character creation, techniques, adversaries, conditions | **l5r-gm** | `l5r-gm/scripts/lookup.py`, `npc.py` |
| World yes/no questions, "what's behind the door?" | **mythic-gm** | `mythic-gm/scripts/dice.py fate …` |
| Scene framing (Expected / Altered / Interrupt) | **mythic-gm** | `mythic-gm/scripts/dice.py scene …` |
| Chaos Factor, random events, plot / Turning Points | **mythic-gm** | `oracle.py`, `adventure_crafter.py`, `state.py chaos` |
| **The oracle ladder when inventing anything** | both | canon → L5R generator → Mythic oracle, **re-skinned to Rokugan** |

The contract between them is `campaigns/<name>/system-profile.md` (pre-filled in the template):
*route ALL resolution & combat to l5r-gm; defer world questions, pacing, Chaos, events, and plot to mythic-gm.*

---

## Repository layout

```
.
├── CLAUDE.md                 ← you are here: the orchestrator + repo map
├── README.md                 ← human-facing overview & setup
├── .claude/
│   └── skills/
│       ├── l5r-gm/           ← the L5R 5E engine  (SKILL.md, scripts/, data/, references/)
│       └── mythic-gm/        ← the Mythic oracle/pacing engine
└── campaigns/
    ├── README.md             ← how a campaign folder works
    ├── _template/            ← copy this to start a campaign (do NOT play in it)
    │   ├── campaign-state.md   ← the single source of truth (L5R active-set + Mythic apparatus)
    │   ├── character-sheet.md  ← the PC
    │   ├── conflict-tracker.md ← scratch sheet for an active skirmish/duel/intrigue/battle
    │   ├── setting-canon.md    ← world ground-truth (overrides invention)
    │   └── system-profile.md   ← the l5r↔mythic seam (pre-filled for L5R 5E)
    └── <your-campaign>/      ← one folder per campaign; this is what you commit
```

---

## The workflow

### Starting a new campaign (Session Zero)
1. Pick a slug and copy the template:
   `cp -r campaigns/_template "campaigns/<slug>"`
2. Run the **`l5r-gm`** Session Zero (set the honest-dice contract → frame the campaign and
   fill the **active-set** → build the PC via the Game of Twenty Questions → seed Threads from
   giri/ninjō → Chaos Factor 5). Write everything into `campaigns/<slug>/`.
3. Frame the first scene, surface only what the PC perceives, ask **"What do you do?"**, and stop.

### Continuing a campaign
1. Read `campaigns/<slug>/campaign-state.md` (and `character-sheet.md`). Recap the last beat in
   2–3 sentences, then resume the loop.
2. If a conflict was mid-flight, `conflict-tracker.md` holds its state.

### Every scene (summary — full detail in the skills)
Restate the creed → read state → frame the scene (mythic Scene Test) → **set stakes before
rolling** → "What do you do?" and STOP → resolve declared actions with **honest, shown dice**
(L5R check, or a Fate Question for world facts; a conflict drops into the matching subsystem) →
apply strife/honor/conditions/clocks → bookkeep (Chaos ±1, update Lists, run the self-audit) →
**overwrite `campaign-state.md`** → repeat.

---

## Honest dice & the discipline (non-negotiable)

This is the whole point — do not relax it to be agreeable:

- **Every uncertain outcome is decided by a script and shown** in a `[Adjudication: …]` block.
  If you state an outcome you did not roll, you have failed. Never invent or estimate a result.
- **Pre-commit the stakes before the roll. Roll before you narrate. Honor the oracle** — a No
  is a real No; a bad event is not "rescued."
- **You roll; the player chooses** which dice to keep. **Player knowledge ≠ PC knowledge.**
- **NPCs and foes act to win** — roll their competence, use their techniques (`npc.py`).
- **Defeat is real and scales to L5R's drama:** death, dishonor, seppuku, capture, ruin.
  Peril Points are OFF unless the *player* opts in aloud.
- Run the **self-audit** before sending any scene: a scene may not be sent unless something
  real is at stake or moved.

---

## ⚠️ Persisting your game — this environment is ephemeral

The container is reclaimed after the session ends; **anything not committed is lost.** The
skill *engines* are already committed — but a live game lives entirely in `campaigns/<slug>/`.

- After a meaningful beat or at the end of a session, **commit the campaign folder** and push:
  ```
  git add campaigns/<slug>
  git commit -m "Session N: <one-line recap>"
  git push -u origin claude/pensive-carson-hmcnts
  ```
- To resume later, the committed `campaign-state.md` is all you need — it is the save file.
- Offer to commit at natural stopping points; never let hours of play evaporate uncommitted.

---

## Script quick reference (run from the repo root)

```bash
# ── L5R resolution (l5r-gm owns this) ───────────────────────────────────────
python3 .claude/skills/l5r-gm/scripts/dice.py check --ring R --skill S --tn T   # roll-and-keep check
python3 .claude/skills/l5r-gm/scripts/lookup.py technique "Iaijutsu Cut"        # look up content…
python3 .claude/skills/l5r-gm/scripts/lookup.py find "<query>"                  #   …or search it
python3 .claude/skills/l5r-gm/scripts/lookup.py list techniques --clan crane --rank 1
python3 .claude/skills/l5r-gm/scripts/npc.py build-rival --name N --clan C --rank R
python3 .claude/skills/l5r-gm/scripts/state.py init --dir campaigns/<slug>      # seed a campaign folder
python3 .claude/skills/l5r-gm/scripts/state.py validate campaigns/<slug>/campaign-state.md

# ── Oracle / pacing / plot (mythic-gm owns this) ─────────────────────────────
python3 .claude/skills/mythic-gm/scripts/dice.py fate <Odds> <CF>               # Fate Question (yes/no)
python3 .claude/skills/mythic-gm/scripts/dice.py scene <CF> --mode <pure|crafter|prepared>
python3 .claude/skills/mythic-gm/scripts/oracle.py event-focus                  # random event…
python3 .claude/skills/mythic-gm/scripts/oracle.py pair actions                 #   …+ meaning pair
python3 .claude/skills/mythic-gm/scripts/adventure_crafter.py turning-point --plotlines N --characters M
python3 .claude/skills/mythic-gm/scripts/state.py chaos <+1|-1> <CF>            # adjust Chaos Factor
```

Fate odds: `Certain` · `"Nearly Certain"` · `"Very Likely"` · `Likely` · `50/50` · `Unlikely` ·
`"Very Unlikely"` · `"Nearly Impossible"` · `Impossible`.
