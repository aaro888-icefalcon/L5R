# Campaigns

Each campaign is one folder here. The folder **is** the save game — committing it preserves
your game; the skill engines in `.claude/skills/` never change between sessions.

## Start a new campaign

```bash
cp -r campaigns/_template "campaigns/my-campaign"
```

Then tell Claude to begin — it runs **Session Zero** (sets the honest-dice contract, frames the
campaign and active-set, builds your character, seeds Threads) and fills the files in.

## What's in a campaign folder

| File | What it is |
|---|---|
| `campaign-state.md` | **The single source of truth.** Overwritten at the end of every scene: the active-set, current adventure & Theme priority, Chaos Factor, Threads/Characters/Clocks lists, campaign roster, overlays, and the current-scene recap. This is your save file. |
| `character-sheet.md` | The PC — rings, skills, derived stats, honor/glory/status, ninjō & giri, techniques, bonds, gear. |
| `setting-canon.md` | **Campaign** ground-truth (places, factions, named NPCs, tone, hard lines). Overrides invention *and* the companion's general Rokugan canon; the GM records new facts here so they stay consistent. |
| `seeds.md` | The live **30–40 seed deck** the GM draws scenes/Turning Points/Random Events from — refreshed at every bookkeeping (sources in `l5r-gm/bridge/seeds.md`). |
| `archive.md` | Where resolved Threads and dead/departed Characters go, to keep the live state lean. |
| `system-profile.md` | A thin pointer to the resolve seam — `l5r-gm/bridge/system-profile.md` (roll-and-keep, the four conflicts, routing). Pre-filled; touch it only for a campaign-specific house rule. |
| `conflict-tracker.md` | Scratch sheet for an in-progress skirmish / duel / intrigue / mass battle. |

`_template/` is the blank starting set — **copy it, don't play in it.** General L5R rules and Rokugan
lore live in `.claude/skills/l5r-gm/`; the engine and its bridge never change between sessions.

## Save / resume

```bash
git add campaigns/my-campaign
git commit -m "Session 3: the duel at Kyūden Bayushi"
git push
```

To resume, just open the repo and ask Claude to continue — it reads `campaign-state.md` and
picks up from the last beat. You can keep several campaigns side by side, one folder each.
