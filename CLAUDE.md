# Rokugan — a solo Legend of the Five Rings 5E table, run by Claude

This repository is a turnkey workspace for playing **Legend of the Five Rings 5th Edition**
solo (or GM-less) in **Rokugan**, with Claude as the Game Master. It runs the **mythic-gm v2
engine + companion** architecture: one content-free engine, one L5R companion that fills its hooks.

- **`mythic-gm`** *(the engine)* — Mythic GME 2e + The Adventure Crafter: the oracle (Fate
  Questions), the Scene Test, Chaos Factor, random events, Turning Points/plot, the seed & list
  machinery, and the no-softening discipline. **Content-free and shared.** Owns **pacing & the
  world oracle**. It runs the loop and, at session start, loads the companion's `bridge/`.
- **`l5r-gm`** *(the companion)* — the L5R 5E ruleset and Rokugan setting: roll-and-keep checks,
  character creation, the four conflicts (skirmish · duel · intrigue · mass battle),
  techniques/adversaries/conditions from all 8 books, and the giri-vs-ninjō samurai drama. **Owns
  all L5R resolution.** It ships a **`bridge/`** that fills the engine's hooks (resolve, meaning,
  chaos, themes, generators, world-tick, seeds), so the engine plays *as L5R in Rokugan.*

The seam is formal now: the engine asks the questions and paces; the **bridge** routes resolution
to L5R, makes the oracle read as samurai drama, and supplies Rokugan generation/pacing/world. This
repo runs **both, together.** (`l5r-gm` can also run standalone with its own oracle; `mythic-gm`
can run standalone for any RPG — but for Rokugan, always run the pair.)

---

## ▶️ To play

When the user wants to **play / start / continue** a game in Rokugan (triggers: "L5R",
"Legend of the Five Rings", "Rokugan", "be my GM", "let's play a samurai", "continue my
campaign", a clan name, "duel/intrigue/skirmish/mass battle"):

1. **Load both skills** and the bridge. Invoke **`l5r-gm`** (the L5R rules + the `bridge/`) and
   **`mythic-gm`** (the engine). The engine runs the play loop; at session start, load the
   companion bridge: `python3 .claude/skills/mythic-gm/scripts/bridge.py summary
   .claude/skills/l5r-gm/bridge` — use an override where present, else the engine default.
2. **Find the campaign.** Look in `campaigns/`. If a campaign folder with a
   `campaign-state.md` exists, **continue it**. Otherwise run **Session Zero** to create one.
3. **Follow the skills' play loop and discipline verbatim.** This file is the orchestrator and
   the repo map; the *authoritative* rules-of-engagement live in each skill's `SKILL.md`
   (engine loop: `mythic-gm/references/playloop.md` · companion: `l5r-gm` references).

> The skills' `SKILL.md` files assume you operate from inside the skill directory. **In this
> repo, always invoke scripts by their full path from the repo root** (see Quick Reference),
> pass the bridge as `.claude/skills/l5r-gm/bridge`, and treat **`campaigns/<name>/`** as the
> "campaign folder" the engine writes play state into.

---

## The seam — who owns what (do not blur it)

| Concern | Owner | Mechanism |
|---|---|---|
| Task checks, TN, strife, opportunity, unmasking | **l5r-gm** | `l5r-gm/scripts/dice.py check …` |
| Skirmish · duel · intrigue · mass battle | **l5r-gm** | `l5r-gm/references/conflict/` + `dice.py` |
| Character creation, techniques, adversaries, conditions | **l5r-gm** | `l5r-gm/scripts/lookup.py`, `npc.py` |
| World yes/no questions, "what's behind the door?" | **mythic-gm** | `mythic-gm/scripts/dice.py fate …` |
| Scene framing (Expected / Altered / Interrupt) | **mythic-gm** | `mythic-gm/scripts/dice.py scene …` |
| Chaos Factor, random events, plot / Turning Points | **mythic-gm** | `oracle.py`, `adventure_crafter.py`, `state.py chaos` |
| Generation (NPC name/role, place), re-skinned to Rokugan | **bridge** | `l5r-gm/bridge/generators/` + `dice.py table` |
| Offscreen world advancing at bookkeeping | **bridge** | `l5r-gm/bridge/subsystems.md` → `tick.py` |
| **The oracle ladder when inventing anything** | both | canon → bridge generator → Mythic oracle, **re-skinned to Rokugan** |

The contract is the companion **`bridge/`** (`.claude/skills/l5r-gm/bridge/`), declared in its
`bridge.md` manifest: *resolve & combat → l5r-gm; meaning/chaos/themes/generators/world-tick/seeds
→ Rokugan; world questions, scene pacing, Chaos, events, and plot → the engine.* A campaign's
`system-profile.md` simply points at the bridge (and can hold campaign-only overrides).

---

## Repository layout

```
.
├── CLAUDE.md                 ← you are here: the orchestrator + repo map
├── README.md                 ← human-facing overview & setup
├── .claude/
│   └── skills/
│       ├── mythic-gm/        ← the ENGINE (v2): SKILL.md, COMPANION-SKILLS.md, CONVERSION.md,
│       │                       scripts/ (dice, oracle, adventure_crafter, bridge, tick, system,
│       │                       state, build_data), data/, references/, agents/, assets/
│       └── l5r-gm/           ← the COMPANION: SKILL.md, scripts/, data/, references/, and…
│           └── bridge/       ← fills the engine hooks (bridge.md manifest + the 8 hook files,
│                               generators/*.json built by generators/build.py)
└── campaigns/
    ├── README.md             ← how a campaign folder works
    ├── _template/            ← copy this to start a campaign (do NOT play in it)
    │   ├── campaign-state.md   ← the single source of truth (L5R active-set + engine apparatus)
    │   ├── character-sheet.md  ← the PC
    │   ├── conflict-tracker.md ← scratch sheet for an active skirmish/duel/intrigue/battle
    │   ├── setting-canon.md    ← campaign ground-truth (overrides bridge canon & invention)
    │   ├── seeds.md            ← the live 30–40 seed deck (refreshed each bookkeeping)
    │   ├── archive.md          ← resolved threads / dead characters (keeps live state lean)
    │   └── system-profile.md   ← thin pointer to the bridge's resolve profile (+ optional overrides)
    └── <your-campaign>/      ← one folder per campaign; this is what you commit
```

---

## The workflow

### Starting a new campaign (Session Zero)
1. Pick a slug and copy the template:
   `cp -r campaigns/_template "campaigns/<slug>"`
2. Load the bridge (`bridge.py summary …`). Run **Session Zero** (set the honest-dice contract →
   frame the campaign and fill the **active-set** → build the PC via the Game of Twenty Questions →
   seed Threads from giri/ninjō → Chaos Factor 5 → populate the first `seeds.md`). The adventure's
   Theme priority is rolled from the bridge's `theme-weights.md`. Write everything into
   `campaigns/<slug>/`.
3. Frame the first scene, surface only what the PC perceives, ask **"What do you do?"**, and stop.

### Continuing a campaign
1. Read `campaigns/<slug>/campaign-state.md` (and `character-sheet.md`, `seeds.md`). Recap the last
   beat in 2–3 sentences, then resume the loop.
2. If a conflict was mid-flight, `conflict-tracker.md` holds its state.

### Every scene (summary — full detail in the skills)
Restate the creed → read state → frame the scene (engine Scene Test; Altered/Interrupt → a Turning
Point) → **set stakes before rolling** → "What do you do?" and STOP → resolve declared actions with
**honest, shown dice** (L5R check, or a Fate Question for world facts; a conflict drops into the
matching subsystem) → apply strife/honor/conditions/clocks → **bookkeep**: Chaos ±1, update Lists,
**world-tick** (`tick.py <bridge> <scene#>`), **refresh `seeds.md`** to 30–40, run the self-audit →
**overwrite `campaign-state.md`** → repeat.

---

## ⚖️ Resolution discipline — STOP at rung 1 *before* you reach for the oracle

> Why this is here, loud, in the always-on doc: a **Fate Question is an in-hand, tooled move you run
> every turn**; the **L5R check is the correct-but-passive** one. Under load the salient tool wins and
> the discipline that's merely *pointed to* (in `system-profile.md`) silently loses. So route **at the
> moment of resolution**, every time:

- **The PC *does* something uncertain → it is an L5R CHECK, not a Fate Question.**
  `l5r-gm/scripts/dice.py check --ring R --skill S --tn T`. Strife is the price of success — foreground it.
- **A world fact the PC can't settle by acting → Fate Question** (`mythic-gm/scripts/dice.py fate …`).
  That is **rung 4**, not rung 1. *Never resolve a PC's action with a Fate Question.*
- **An action opens a conflict → drop into the subsystem** (skirmish · duel · intrigue · mass battle).

**Trigger list — when this shows up in the fiction, the mechanic fires (don't wait to remember it):**

| In the fiction… | Fires |
|---|---|
| PC attempts anything with a real chance of failure | **L5R check** (ring+skill+TN); strife offered |
| Strife climbs past **composure** | **UNMASK** — the giri-vs-ninjō break; play it, don't skip it |
| The PC's **anxiety / adversity / passion** is poked *(see `character-sheet.md`: Softheartedness on a kill-or-spare choice · Fear of Failure on a high-stakes check that would harm dependents · Scorn of the Scorpion on Scorpion rapport · Marked by the Deep near a breach/Taint · Sixth Sense near hidden spirits · Stories/Blessed Lineage)* | that disadvantage's **strife / reroll / Void** |
| An oath sworn · a public act · dishonor · a notable deed | **Honor / Glory / Status** change |
| A spirit/world yes-no the PC can't act on | **Fate Question** (rung 4) — *then* interpret |

## ✅ Per-scene bookkeeping checklist — run at every scene end; none are optional
1. **Triggers cleared?** Did any anxiety/adversity/passion fire this scene (above)? Apply its strife/effect.
2. **State applied?** strife → composure (**unmask?**) · honor/glory/status · conditions · resources · clocks.
3. **World-tick:** `python3 .claude/skills/mythic-gm/scripts/tick.py .claude/skills/l5r-gm/bridge <scene#>`.
4. **Lists — edit the JSON, then regenerate the snapshot (never hand-edit the snapshot):**
   `state.py thread|char …` (weight) · `render_lists.py set-note …` (prose) → then
   `python3 .claude/skills/l5r-gm/scripts/render_lists.py render campaigns/<slug> --in-place`
   (verify with `… render campaigns/<slug> --check`).
5. **Chaos** ±1.   6. **Seeds** refreshed to 30–40.   7. **Self-audit.**   8. **Overwrite `campaign-state.md`.**

> **On resume / after context summarization:** re-read `character-sheet.md` (the PC's triggers) and the
> bridge's `system-profile.md`. The rules you *read once* decay; the loop you *run* stays hot — so reload
> the load-bearing imperatives, don't trust them to still be in context.

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
skill *engine and companion* are already committed — but a live game lives entirely in `campaigns/<slug>/`.

- After a meaningful beat or at the end of a session, **commit the campaign folder** and push:
  ```
  git add campaigns/<slug>
  git commit -m "Session N: <one-line recap>"
  git push -u origin <your-branch>
  ```
- To resume later, the committed `campaign-state.md` (+ `seeds.md`) is all you need — it is the save file.
- Offer to commit at natural stopping points; never let hours of play evaporate uncommitted.

---

## Script quick reference (run from the repo root)

```bash
# ── L5R resolution & content (l5r-gm — the companion owns this) ──────────────
python3 .claude/skills/l5r-gm/scripts/dice.py check --ring R --skill S --tn T   # roll-and-keep check
python3 .claude/skills/l5r-gm/scripts/lookup.py technique "Iaijutsu Cut"        # look up content…
python3 .claude/skills/l5r-gm/scripts/lookup.py find "<query>"                  #   …or search it
python3 .claude/skills/l5r-gm/scripts/lookup.py list techniques --clan crane --rank 1
python3 .claude/skills/l5r-gm/scripts/npc.py build-rival --name N --clan C --rank R
python3 .claude/skills/l5r-gm/scripts/state.py validate campaigns/<slug>/campaign-state.md

# ── The bridge (companion ↔ engine seam) ─────────────────────────────────────
python3 .claude/skills/mythic-gm/scripts/bridge.py summary  .claude/skills/l5r-gm/bridge   # hooks: override vs default
python3 .claude/skills/mythic-gm/scripts/bridge.py validate .claude/skills/l5r-gm/bridge   # structure + roll-test tables
python3 .claude/skills/mythic-gm/scripts/system.py route                                    # the resolve routing rule
python3 .claude/skills/l5r-gm/bridge/generators/build.py                                     # (re)build the L5R generator tables
python3 .claude/skills/mythic-gm/scripts/dice.py table \
        .claude/skills/l5r-gm/bridge/generators/family_name.json                             # roll a bridge table (honest)

# ── Oracle / pacing / plot (mythic-gm — the engine owns this) ────────────────
python3 .claude/skills/mythic-gm/scripts/dice.py fate <Odds> <CF> [--campaign campaigns/<slug>]   # Fate Question (auto-chains a Random Event; --campaign rolls the JSON Lists)
python3 .claude/skills/mythic-gm/scripts/dice.py scene <CF>                     # Scene Test (Adventure Crafter always on)
python3 .claude/skills/mythic-gm/scripts/oracle.py event --campaign campaigns/<slug> [--crafter]   # full Random Event chain (reads threads.json/characters.json)
python3 .claude/skills/mythic-gm/scripts/oracle.py character --campaign campaigns/<slug> --bridge .claude/skills/l5r-gm/bridge   # new NPC (L5R role + AC Crafter)
python3 .claude/skills/mythic-gm/scripts/oracle.py thread-list    --campaign campaigns/<slug>   # two-stage Thread invoke (NEW/PRE-EXISTING/CHOOSE)
python3 .claude/skills/mythic-gm/scripts/oracle.py character-list --campaign campaigns/<slug> --bridge .claude/skills/l5r-gm/bridge   # Character invoke (a NEW auto-generates)
python3 .claude/skills/mythic-gm/scripts/adventure_crafter.py themes --style drama --campaign campaigns/<slug>   # roll & save the adventure's Themes → adventure.json
python3 .claude/skills/mythic-gm/scripts/adventure_crafter.py turning-point --campaign campaigns/<slug> [--existing]   # Turning Point (themes+tens from adventure.json)
python3 .claude/skills/mythic-gm/scripts/state.py chaos <+1|-1> <CF>            # adjust Chaos Factor
python3 .claude/skills/mythic-gm/scripts/tick.py .claude/skills/l5r-gm/bridge <scene#>        # world-tick (bookkeeping)

# ── The JSON Lists (Threads / Characters / adventure config — the dice roll THESE, any length) ──
python3 .claude/skills/mythic-gm/scripts/state.py thread add|weight|remove|show campaigns/<slug> "<name>"   # manage threads.json (weight = re-add, max 3)
python3 .claude/skills/mythic-gm/scripts/state.py char   add|weight|remove|show campaigns/<slug> "<name>"   # manage characters.json
python3 .claude/skills/mythic-gm/scripts/state.py adventure show|set-themes campaigns/<slug> [A,B,C,D,E]     # Theme priority + tens counter (adventure.json)
python3 .claude/skills/mythic-gm/scripts/state.py list-count campaigns/<slug>                                # weighted-slot counts
python3 .claude/skills/mythic-gm/scripts/state.py migrate  campaigns/<slug>                                  # one-time: build the JSON Lists from an old markdown state
# the snapshot is GENERATED from the JSON — never hand-edit it (companion tool):
python3 .claude/skills/l5r-gm/scripts/render_lists.py render   campaigns/<slug> --in-place               # regenerate the Markdown snapshot FROM the JSON (kills drift)
python3 .claude/skills/l5r-gm/scripts/render_lists.py render   campaigns/<slug> --check                  # drift detector: exit 1 if snapshot ≠ JSON
python3 .claude/skills/l5r-gm/scripts/render_lists.py set-note campaigns/<slug> thread|character "<name>" "<note>"   # set an entry's prose (JSON stays the single source)
```

> **Lists are JSON — the single source of truth.** Each campaign's Threads/Characters Lists and Theme
> priority live in `threads.json` · `characters.json` · `adventure.json` (the machine-rollable source the
> dice roll over, any length; entries carry `{name, weight, note}`). The `## Threads` /
> `## Characters & Factions` sections in `campaign-state.md` are a **GENERATED** view — **never hand-edit
> them.** Edit the JSON (`state.py thread|char|adventure` for weight/themes, `render_lists.py set-note`
> for prose), then `render_lists.py render … --in-place`; the snapshot can't drift because it's derived,
> not synced by hand. A NEW Character result auto-generates one (L5R role generator + AC Crafter) via the bridge.

Fate odds: `Certain` · `"Nearly Certain"` · `"Very Likely"` · `Likely` · `50/50` · `Unlikely` ·
`"Very Unlikely"` · `"Nearly Impossible"` · `Impossible`.
