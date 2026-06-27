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
- **Premise / tone:** Samurai **war-drama** on the Lion–Crane front at **Toshi Ranbo**. Akihiko — a Falcon sun-priest of **known (scandalous) Seppun blood** — is a **chūi** in the **Imperial Legions**, sent to police a war between two great clans that hate each other and the Emperor's interference equally. His **ninjō** (bring his soldiers — a **Falcon contingent** of his own clansmen — home alive to the Valley of the Spirits) wars with his **giri** (win the Emperor's wars to bring **honor to the Falcon**, spending what must be spent). The trap: both pull toward the Falcon, in opposite directions — *to honor the clan he must spend the clan.* Full-spectrum: mass battle · skirmish · duel · court intrigue.
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
- **Adventure status:** **active** — Scenes 1–4. Sc.1 took up command; Sc.2 lit a forward post, lost a death-duel to **Matsu Kasumi** (spared his life), and the Lion crossed west; Sc.3 the camp was found **poisoned** (a blindfold), which Akihiko cured and traced to a caught professional, **Jōji**, earning taisa Saburō's writ; Sc.4 he rode to the western smoke to find the payoff — a **Lion strike sacking a Crane supply-village** through the gap he left, with Kasumi in it and the dishonor pointing at the Lion themselves (NOT the Scorpion).
- **Theme priority (this adventure):** **Personal › Action › Social › Tension › Mystery** — in `adventure.json` (`state.py adventure show campaigns/akihiko-legionnaire`); _player-set._

> **The Lists are JSON — the single source of truth.** Threads/Characters Lists + Theme priority live
> in `threads.json` · `characters.json` · `adventure.json` (entries carry `{name, weight, note}`; the
> dice roll over them, any length). `state.py init` scaffolds them; set weight/themes with `state.py
> thread|char|adventure …` and prose with `render_lists.py set-note …`. The `## Threads` /
> `## Characters & Factions` sections below are a **GENERATED** view — **never hand-edit them**;
> regenerate with `l5r-gm/scripts/render_lists.py render <dir> --in-place` (drift-check: `… --check`).

## Chaos Factor: 6
_(1–9; −1 if the PC was mostly in control last scene, +1 if it was chaotic — see `bridge/chaos-tendency.md`. Sc.2: Akihiko was overwhelmed — lost the duel, lost the road, ended at an enemy's mercy → **+1 → 6**.)_

## Threads — snapshot of `threads.json` · GENERATED (edit the JSON + re-render; do not hand-edit)
1. **The Toshi Ranbo front — the Lion–Crane war** *(w3)* — PRIMARY. The Lion and Crane — ancestral enemies — are at open war over the contested town of Toshi Ranbo (Akodo Arasou slain by Doji Hotaru's arrow, 1123). Akihiko's Legion is deployed to enforce an Imperial edict between two armies that hate each other. (facts.py relation lion crane)
2. **Keep my soldiers alive — ninjō vs the orders that spend them** *(w3)* — The engine of the drama. His cohort carries a FALCON (Toritaka) contingent — clansmen serving the Legion under their famous-blooded son; his ninjō is to march them home to the Valley of the Spirits ALIVE. Every order that spends lives to win the Emperor's war pokes it. The cruelty: his giri (honor the Falcon) is paid in the same Falcon lives his ninjō would save. Trigger to watch: Softheartedness (Fire) — he seizes up about KILLING, +3 strife when he takes a life. (Also Fear of Mediocrity (Fire): +3 strife when he must improvise/adapt to the unexpected on a Fire check.)
3. **The black-sheep blood & uncle Seppun Tadanobu's leash** *(w2)* — His known Imperial blood comes from the scandalous branch — grandfather left the Seppun to marry a Toritaka; uncle Tadanobu redeemed it and sponsors Akihiko. The favor is a leash: what does the uncle expect in return, and who resents the upjumped black-sheep nephew?
4. **Officers who know whose nephew he is — expectation & resentment** *(w2)* — Akihiko serves under officers aware of his Seppun patron and his minor-clan origins. ELEVATION here is rolled, not narrated (Status-priced Fate Questions); trust and favor arrive with strings.
5. **The spirit-dark of the battlefield — what the Falcon sees that the war hides** *(w1)* — Quiet thread. A battlefield is a feast for the dead; Akihiko's Falcon spirit-sight (Sixth Sense) may find yūrei, gaki, or worse moving under cover of the mundane war. Latent — let the dice surface it.
6. **A Lion's debt — the life I owe Matsu Kasumi** *(w1)* — Akihiko lives because Matsu Kasumi chose not to kill him in a death-duel he lost. A life-debt to a Lion enemy, witnessed by both armies. She will remember; so must he. The string will pull — in court, in war, or the next time their paths cross.
7. **Answering for the broken post — the lost road and taisa Saburō** *(w1)* — Akihiko's two riders carry word up the ridge: the post fell, the Lion crossed west, the edict broke — and the Throne's officer lives by a Matsu's mercy. His first duty, failed publicly his first night. The reckoning with taisa Seppun Saburō (who already despises his patron-bought commission) is coming with the dawn.
8. **The poisoned camp — find the hand killing the Legion (Saburō's charge)** *(w1)* — Sc.3 RESOLVED (mostly): the feast-poison was contained, the camp cured, and the poisoner — Jōji, a hired professional — caught alive. It was a coordinated BLINDFOLD for the western Lion strike, NOT random spite. Oracle: NOT the Scorpion (Exc No) — the dishonorable hand traces toward the LION (Akodo Shizue / her level). Open: break Jōji for the paymaster's name; the proof of Lion-bought poison is leverage at court. Akihiko earned Saburō's grudging writ for cracking it.
9. **The western strike — the Crane village burning through the gap I left** *(w1)* — Sc.4 played: Akihiko rode to the smoke with 6 men, found a Lion strike (Akodo Shizue cmdg, Kasumi running down fugitives) gutting a Crane supply-village. He couldn't save it (already lost) — but reframed his demand as courtesy (invoking Kasumi's mercy) + a bluff of incoming Imperial reinforcement, and TURNED THE COLUMN (Water·Courtesy success): Shizue withdrew 'of her own prudence,' sparing the last fugitives. He got no tell from her (she's the prime poison-paymaster but gave nothing provable) and she has MARKED him ('give your uncle my regards'). The Crane war-lifeline is wounded. Akihiko secured witness Daidoji Sukune. Now: carry it all to Saburō + build the case for the Lion's dishonor.

## Characters & Factions — snapshot of `characters.json` · GENERATED (NPC/force — want — disposition; PC NOT listed)
- **Seppun Tadanobu (uncle / Imperial patron)** *(w2)* — Akihiko's illustrious maternal uncle, reclaimed into the Seppun; his sponsor into the Legions. Powerful, watchful; his patronage is a leash. Wants — UNKNOWN (roll it); disposition: proprietary, demanding.
- **Akihiko's cohort — the soldiers under his command** *(w2)* — The squads he leads — including a FALCON (Toritaka) contingent of clansmen-levies he means to bring home alive (his ninjō), plus Legion ashigaru & bushi of mixed clans. Names & faces drawn in play (npc.py / generators). Their lives are the stakes; their home is the Valley of the Spirits.
- **The Lion army at Toshi Ranbo** *(w1)* — The largest, most formidable army in Rokugan; martial, honor-bound, hungry for vengeance after Arasou's death. Right Hand of the Emperor — being policed by the Emperor's own Legion is a humiliation they feel keenly. (facts.py clan lion)
- **The Crane army at Toshi Ranbo** *(w1)* — Smaller but exquisitely trained; the Left Hand of the Emperor, masters of court and the duel. Defending what they hold; will fight with law and word as much as steel. (facts.py clan crane)
- **Seppun Saburō (taisa / commanding officer)** *(w1)* — Akihiko's direct superior — taisa of the Legion company. A TRUE-BLOODED Seppun who rose from OBSCURITY by merit (seed: Succeed·Obscurity), not by name — and so has no patience for a commission bought with Tadanobu's favor. Knows exactly whose nephew Akihiko is and rides him HARDER for it, to be seen showing the patron's pup no slack. Demanding, watchful, competent; gives orders that spend lives to win the Throne's war. Want: deepen in play — make this posting prove his command was earned. Disposition: cold, testing, proprietary-but-skeptical.
- **Matsu Kasumi (Lion duelist — spared his life)** *(w1)* — Young Matsu officer (Akihiko's age), scarred, proud, the superior blade. Led 7 riders to test the post; challenged Akihiko to a death-duel after his deterrence failed. He taunted her (Lady Matsu's bravery), then apologized and met certain death with grace — and she STAYED HER HAND, sparing Imperial blood that knelt well. Took the road west; left him his life and a debt: 'Remember who gave it to you.' A complicated bond now — enemy, benefactor, equal. Disposition: respect, ownership, watchful.
- **The Legion healer corps (overwhelmed field-surgeons)** *(w1)* — The Legion's field-surgeons — the 'physician organization' (TP: Organization, Assistant, Harmful). Drowning under the poisoning, unable to name the cause; possibly implicated, possibly just overwhelmed. Akihiko, the sun-priest-physician, is set over/among them to solve it. Disposition: exhausted, defensive, out of their depth.
- **Jōji (captured poisoner — professional, alive)** *(w1)* — A professional poisoner-assassin under an entertainer's cover; poisoned the Legion's feast-sake (stone-fruit-kernel toxin) to blind it for the western strike. Caught alive by Akihiko (his suicide-tooth denied). Hidden papers point to a paymaster. Being interrogated offscreen by Gunsō Tetsuo. NOT a Scorpion job (oracle Exc No) — the hand traces toward the LION.
- **Gunsō Tetsuo (the hard sergeant breaking Jōji)** *(w1)*
- **Akodo Shizue (Lion strike commander — likely poison-paymaster)** *(w1)* — Lion (Akodo) commander of the western strike force (~50, Matsu horse + Akodo foot) sacking the Crane supply-village. Ambitious — likely the hand that secretly hired Jōji to poison the Imperial Legion so the Throne's referee couldn't see the Lion do this. A scandal if proven (the honorable Lion using poison). Sits the knoll; Kasumi serves under her. High Status (Blessed Lineage may stay her hand from killing Imperial blood).
- **Daidoji Sukune (Crane Iron Warrior — the last stand at the ford)** *(w1)* — Grey-haired Daidoji guardian; led the hopeless ford-stand (12 of his dead) that bought the villagers their escape. Akihiko turned the Lion column off them, then knelt in the ash tending Crane wounded — earning his hard respect. SECURED as a live WITNESS: rides to the Legion camp to tell Saburō (and any magistrate) that the Lion struck WITH FOREKNOWLEDGE — came 'easy,' no screen, no haste, 'like someone promised them no one would come.' A Crane who'd be believed. Not yet sworn to a court (conditional ally; answers his own Crane lords too). Owed a debt of care now.

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
- **The western strike (LIVE — Sc.4):** the Lion blinded the Legion with poison and struck WEST through Akihiko's lost road — **Akodo Shizue's** force is sacking a Crane supply-village on the Drowned Merchant *right now;* **Matsu Kasumi** runs down fugitives. Akihiko (6 men) is watching it burn. The edict is in ruins; the Crane lifeline is being gutted.
- **The Lion's secret dishonor (leverage clock):** proof the Lion bought victory with poison (NOT the Scorpion — oracle Exc No) would scandalize the Right Hand of the Emperor and redeem the Throne's humiliation. Evidence lives in Jōji's papers + his interrogation (Gunsō Tetsuo working him offscreen) and maybe at the burning village. Akodo Shizue is the prime paymaster suspect.
- **The Toshi Ranbo war:** Lion (vengeful, vast) vs Crane (beset — fewest forces, wealth-poor, bleeding) over Toshi Ranbo. The Imperial Legion (the referee) was just neutralized for a night; the Lion are exploiting it hard.
- **The reckoning with taisa Saburō:** Saburō gave Akihiko a writ to hunt the poisoner (earned by curing the camp) — conditional on *speed, silence, and finishing it.* He needs the western fire explained before he must answer to the Imperial Court for the Legion being caught blind.
- **A Lion's debt:** Akihiko's life belongs to Matsu Kasumi — who is *here,* on the attacking side, almost certainly unaware her clean victory was bought with dishonorable poison.
- **Uncle's expectations:** Tadanobu's patronage will call in its price; how will the uncle take news his nephew lost a duel, lost the road, and stood witness to a Lion atrocity?

## Current scene — Scene 4: *The Gap You Left* → **CLOSED**; Scene 5 (*the report to Saburō*) to frame
- **Sc.4 outcome:** Akihiko rode to the western smoke (6 men), found a Lion strike (Akodo Shizue cmdg, Kasumi running down fugitives) gutting a Crane supply-village. Couldn't save it. His Emperor's-will demand fell flat (Fate No — Shizue weaponized his lost road), but he recovered: reframed it as **courtesy** (invoking Kasumi's mercy) + a **bluff of incoming Imperial reinforcement**, and **TURNED THE COLUMN** (Water·Courtesy success) — Shizue withdrew 'of her own prudence,' sparing the last fugitives. No tell from her; she has **marked** him. He then tended Crane wounded and **secured Daidoji Sukune as a live witness** (Water·Sentiment + Water·Courtesy) — Sukune saw the Lion strike with FOREKNOWLEDGE ('like someone promised them no one would come'). Riding back east with Sukune.
- **Akihiko's state:** **strife 7/8** (a day's worth — one knock from unmasking), fatigue **3/10**, **Void 1/2**, no wounds. Honor 57 · Glory 32 · Status 36. With 5 samurai + the witness.
- **Scene 5 hook (the report):** back at the Legion camp — recount the morning to **taisa Saburō** (the cured poison, the caught assassin, the turned Lion, the witnessed Lion-foreknowledge), present **Sukune**, and learn what **Gunsō Tetsuo** wrung from **Jōji** (the paymaster's name?). Does the whole arc REDEEM Akihiko's standing with the merit-proud Seppun (an elevation — roll it, Status-priced)? And what does Saburō DO with proof the Lion poisoned the Emperor's Legion — a thing he must report to the Throne but cannot prove yet?
- **Chaos:** held at **6** (Sc.4: Akihiko exerted real control — turned the Lion, secured the witness — but the strike succeeded and the war escalated; a wash).
- **Self-audit drift counter (consecutive soft scenes):** 0

## Archive pointer
- Resolved threads / dead characters → `archive.md`
