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
| `campaign-state.md` | **The single source of truth.** Overwritten at the end of every scene: the active-set, Chaos Factor, Threads/Characters/Clocks lists, overlays, and the current-scene recap. This is your save file. |
| `character-sheet.md` | The PC — rings, skills, derived stats, honor/glory/status, ninjō & giri, techniques, bonds, gear. |
| `setting-canon.md` | Campaign ground-truth (places, factions, named NPCs, tone, hard lines). Overrides invention; the GM records new facts here so they stay consistent. |
| `system-profile.md` | The l5r↔mythic seam — routes resolution to l5r-gm and pacing/oracle to mythic-gm. Pre-filled for L5R 5E; you rarely touch it. |
| `conflict-tracker.md` | Scratch sheet for an in-progress skirmish / duel / intrigue / mass battle. |
| `archive.md` *(created as needed)* | Where resolved threads and dead characters go, to keep the live state lean. |

`_template/` is the blank starting set — **copy it, don't play in it.**

## Save / resume

```bash
git add campaigns/my-campaign
git commit -m "Session 3: the duel at Kyūden Bayushi"
git push
```

To resume, just open the repo and ask Claude to continue — it reads `campaign-state.md` and
picks up from the last beat. You can keep several campaigns side by side, one folder each.
