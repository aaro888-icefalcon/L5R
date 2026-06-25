# Campaign State — Toritaka Akihiko, Chūi of the Imperial Legions

> **The single source of truth.** Overwrite this at the END of every scene.
> If a change happened in the fiction but isn't written here, it didn't happen.
> Validate: `python3 .claude/skills/l5r-gm/scripts/state.py validate campaign-state.md`

## Active set (the context filter — only matching content loads)
```yaml
active_set:
  sources:    [core, emerald-empire, fields-of-victory]   # war + Imperial; add others as the campaign reaches them
  clans:      [falcon, lion, crane, scorpion, imperial]   # PC Falcon (Seppun blood); the warring sides; Scorpion scorn
  subsystems: [core-check, skirmish, duel, intrigue, mass-battle, downtime, advancement]
  modes:      [war, court, wilderness, spiritual]
  flags_allowed: []                  # mature | maho | gaijin — OFF unless the player opts in aloud
```

## Frame
- **Premise / tone:** Samurai **war-drama** on the Lion–Crane front at **Toshi Ranbo**. Akihiko — a Falcon sun-priest of **known (scandalous) Seppun blood** — is a **chūi** in the **Imperial Legions**, sent to police a war between two great clans that hate each other and the Emperor's interference equally. His **ninjō** (keep his soldiers alive) wars with his **giri** (win the Emperor's wars, spend what must be spent). Full-spectrum: mass battle · skirmish · duel · court intrigue.
- **TONE CALIBRATION:** **realism · challenging · gritty.** Status 36 is a low ceiling; Akihiko is a junior officer and a black-sheep nephew, not a chosen one. **Elevation is a Status-priced Fate Question, never narrated; a Yes arrives with strings.** Consult `facts.py` before inventing politics; move Honor/Glory/Status via `social.py`. A Fate-Yes leans toward complication.
- **Adventure source:** **Pure Mythic** (mythic-gm owns oracle / scene pacing / Chaos / events / plot)
- **Genre & stakes vocabulary:** samurai-drama — death / dishonor / seppuku / capture / ruin
- **Resolution:** L5R roll-and-keep (l5r-gm) · oracle = Fate Chart (mythic-gm) | Fate Check
- **Discipline:** HARDCORE (no softening; Peril Points OFF unless the player opts in)
- **Engine & companion:** mythic-gm (engine) + l5r-gm `bridge/` (companion)
  - **System profile (resolve):** `.claude/skills/l5r-gm/bridge/system-profile.md`
  - **Setting canon:** `.claude/skills/l5r-gm/bridge/setting-canon.md` (Rokugan) + this folder's `setting-canon.md` (campaign)
  - **Seed deck:** `seeds.md`   ·   **Archive:** `archive.md`

## CURRENT ADVENTURE: Arc 1 — *The Edict at Toshi Ranbo*
_Each adventure has its **own** Threads & Characters Lists and its own Theme priority. A **new
adventure** begins when the current one's main Thread(s) Conclude (the Threads List empties) or the
player declares one._
- **Adventure status:** **active** (Session Zero complete; Scene 1 to be framed at the next session)
- **Theme priority (this adventure):** **Personal › Action › Social › Tension › Mystery** — in `adventure.json` (`state.py adventure show campaigns/akihiko-legionnaire`); _player-set._

> **The Lists are JSON — the single source of truth.** Threads/Characters Lists + Theme priority live
> in `threads.json` · `characters.json` · `adventure.json` (entries carry `{name, weight, note}`; the
> dice roll over them, any length). `state.py init` scaffolds them; set weight/themes with `state.py
> thread|char|adventure …` and prose with `render_lists.py set-note …`. The `## Threads` /
> `## Characters & Factions` sections below are a **GENERATED** view — **never hand-edit them**;
> regenerate with `l5r-gm/scripts/render_lists.py render <dir> --in-place` (drift-check: `… --check`).

## Chaos Factor: 5
_(1–9; −1 if the PC was mostly in control last scene, +1 if it was chaotic — see `bridge/chaos-tendency.md`)_

## Threads — snapshot of `threads.json` · GENERATED (edit the JSON + re-render; do not hand-edit)
1. **The Toshi Ranbo front — the Lion–Crane war** *(w3)* — PRIMARY. The Lion and Crane — ancestral enemies — are at open war over the contested town of Toshi Ranbo (Akodo Arasou slain by Doji Hotaru's arrow, 1123). Akihiko's Legion is deployed to enforce an Imperial edict between two armies that hate each other. (facts.py relation lion crane)
2. **Keep my soldiers alive — ninjō vs the orders that spend them** *(w3)* — The engine of the drama. Every order that spends lives to win the Emperor's war pokes his ninjō; a healer commanding soldiers in a war of attrition. Watch for the kill-or-spare and harm-to-dependents triggers (Softheartedness, Fear of Failure).
3. **The black-sheep blood & uncle Seppun Tadanobu's leash** *(w2)* — His known Imperial blood comes from the scandalous branch — grandfather left the Seppun to marry a Toritaka; uncle Tadanobu redeemed it and sponsors Akihiko. The favor is a leash: what does the uncle expect in return, and who resents the upjumped black-sheep nephew?
4. **Officers who know whose nephew he is — expectation & resentment** *(w2)* — Akihiko serves under officers aware of his Seppun patron and his minor-clan origins. ELEVATION here is rolled, not narrated (Status-priced Fate Questions); trust and favor arrive with strings.
5. **The spirit-dark of the battlefield — what the Falcon sees that the war hides** *(w1)* — Quiet thread. A battlefield is a feast for the dead; Akihiko's Falcon spirit-sight (Sixth Sense) may find yūrei, gaki, or worse moving under cover of the mundane war. Latent — let the dice surface it.

## Characters & Factions — snapshot of `characters.json` · GENERATED (NPC/force — want — disposition; PC NOT listed)
- **Seppun Tadanobu (uncle / Imperial patron)** *(w2)* — Akihiko's illustrious maternal uncle, reclaimed into the Seppun; his sponsor into the Legions. Powerful, watchful; his patronage is a leash. Wants — UNKNOWN (roll it); disposition: proprietary, demanding.
- **Akihiko's cohort — the soldiers under his command** *(w2)* — The ashigaru and bushi he leads — the people his ninjō is sworn to keep alive. Names & faces to be drawn in play (npc.py / generators). Their lives are the stakes.
- **The Lion army at Toshi Ranbo** *(w1)* — The largest, most formidable army in Rokugan; martial, honor-bound, hungry for vengeance after Arasou's death. Right Hand of the Emperor — being policed by the Emperor's own Legion is a humiliation they feel keenly. (facts.py clan lion)
- **The Crane army at Toshi Ranbo** *(w1)* — Smaller but exquisitely trained; the Left Hand of the Emperor, masters of court and the duel. Defending what they hold; will fight with law and word as much as steel. (facts.py clan crane)
- **His commanding officer (Imperial Legion taisa — TBD in play)** *(w1)* — Akihiko's direct superior — a captain (taisa) of the Legion. Clan, name, and disposition to be generated when first met; knows of the Seppun connection.

## Adventure Features (prepared-adventure mode only)
-

## Overlays
- **Keyed Scenes:** _(Trigger → Event; Count)_ none
- **Thread Progress Track:** _(Focus Thread, Track 10/15/20, points, flashpoint flag)_ none
- **Peril Points:** OFF _(or: N remaining, player-invoked only)_

## Adventure Crafter state (crafter mode only)
- n/a (Pure Mythic) · Theme priority lives in `adventure.json`: Personal, Action, Social, Tension, Mystery

## Campaign roster (persists across adventures: recurring NPCs, long arcs)
- **Seppun Tadanobu** — illustrious maternal uncle; Akihiko's Imperial patron & the hand that placed him in the Legions.
- **Toritaka Michio (b. Seppun Michio)** — maternal grandfather, the talented black sheep who left the Seppun to marry a Toritaka. (deceased)
- **Family** — Akiro (brother, apprentice healer), Hizashi (father, Centipede sun-priest), Sumiko (mother, half-Seppun, carries the known line).
- **The Scattered Corps** — cross-clan healers/wardens bound to Akihiko by a past crisis; scattered on duty.

## Clocks (offscreen factions / threats / progress — advanced by `tick.py` at bookkeeping)
- **The Toshi Ranbo war:** Lion (vengeful, vast) vs Crane (defending, smaller) — the Imperial edict Akihiko's Legion enforces sits between them; neither wants the Emperor's hand on their war.
- **Uncle's expectations:** Tadanobu's patronage will call in its price; clock ticks toward what he wants.

## Current scene — SESSION ZERO COMPLETE → Scene 1 to be framed next session
- **Opening situation (the cold open to frame):** Akihiko arrives at the Toshi Ranbo front with (or to take up) his command in an Imperial Legion company — a Falcon sun-priest and black-sheep Seppun nephew set over soldiers, between two great-clan armies that resent the Throne's referee. The first scene establishes his cohort, his commanding officer (generate when met), the shape of the standoff, and the first place his ninjō (keep them alive) grinds against an order.
- **Stakes on the table (to pre-commit at Scene 1):** his soldiers' lives; his standing with a superior who knows whose nephew he is; the fragile edict holding two armies apart.
- **Self-audit drift counter (consecutive soft scenes):** 0

## Archive pointer
- Resolved threads / dead characters → `archive.md`
