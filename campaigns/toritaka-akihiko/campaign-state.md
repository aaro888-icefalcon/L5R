# Campaign State — Toritaka Akihiko, Warden of the Sun

> **The single source of truth.** Overwrite this at the END of every scene.
> If a change happened in the fiction but isn't written here, it didn't happen.
> Validate: `python3 .claude/skills/l5r-gm/scripts/state.py validate campaign-state.md`

## Active set (the context filter — only matching content loads)
```yaml
active_set:
  sources:    [core, shadowlands, celestial-realms]
  clans:      [falcon, centipede, scorpion, mantis, phoenix]
  subsystems: [core-check, skirmish, duel, intrigue, mass-battle, downtime, advancement]
  modes:      [court, war, wilderness, spiritual]
  flags_allowed: []        # maho | mature | gaijin — OFF unless player opts in aloud
```

## Frame
- **Premise / tone:** Samurai drama on the haunted marches of **Toritaka Province**. Akihiko — a scorned Minor-Clan warrior-priest of known Seppun (Imperial) blood — guards flesh and steel against rival schemes and the spirit-dark, aching to belong. Full-spectrum: duel · intrigue · skirmish · mass battle.
- **Adventure source:** **Pure Mythic** (mythic-gm owns oracle / scene pacing / Chaos / events / plot)
- **Genre & stakes vocabulary:** samurai-drama — death / dishonor / seppuku / capture / ruin
- **Resolution:** L5R roll-and-keep (l5r-gm) · oracle = Fate Chart (mythic-gm)
- **Discipline:** HARDCORE (no softening; Peril Points OFF unless the player opts in)
- **Engine & companion:** mythic-gm (engine) + l5r-gm `bridge/` (companion)
  - **System profile (resolve):** `.claude/skills/l5r-gm/bridge/system-profile.md` (+ this folder's `system-profile.md` overrides)
  - **Setting canon:** `.claude/skills/l5r-gm/bridge/setting-canon.md` (Rokugan) + this folder's `setting-canon.md` (campaign)
  - **Seed deck:** `seeds.md`   ·   **Archive:** `archive.md`

## CURRENT ADVENTURE: Arc 2 — *The Long Road Back*
_Each adventure has its own Threads & Characters Lists and its own Theme priority. A new adventure
begins when the current one's main Thread(s) Conclude or the player declares one — roll new Themes
from `bridge/theme-weights.md`, start fresh Lists, carry over still-relevant Characters/Threads,
archive the rest._
- **Adventure status:** **active** — Arc 1 (*The First Ward*) concluded as a capstone (the Dawn Mirror claimed, Imperial blood confirmed). Arc 2 opens with the journey home to deliver the Mirror to Lord Hatsue, through a week-stale, Scorpion-watched march — then the long work of wielding it (cure the mark · free the souls · bind the deep power).
- **Theme priority (this adventure):** **Tension › Action › Social › Mystery › Personal** — stored in `adventure.json` (`state.py adventure show campaigns/toritaka-akihiko`); _rolled `adventure_crafter.py themes --style drama`, Arc 2 open._

## Chaos Factor: 3
_(1–9; −1 if the PC was mostly in control last scene, +1 if it was chaotic. Scene 11: Hatsue's death & a succession crisis — chaotic — but Akihiko steered it: redirected the naming, steadied Chiyo, deferred the deal, held the clan together → in control, −1, 4→3.)_

## Threads — snapshot of `threads.json` · GENERATED (edit the JSON + re-render; do not hand-edit)
1. **The Dawn Mirror & the binding-duty (PRIMARY QUEST)** *(w3)* — *Asahi no Kagami*, claimed (Sc.5), now borne by Akihiko. Not a weapon — it BINDS the deep power in captured sunlight; can cure his mark & free the taken souls. Wake it: Akihiko's Sacred sun-fire at an open dawn, by a willing soul who takes the binding as a lasting duty (Akihiko, the chain's new anchor). Immediate: deliver it safely to Lord Hatsue.
2. **The Mark — danger AND key (the leash)** *(w3)* — The power's hook in Akihiko (Marked by the Deep); CONTAINED but used as the conduit (Sc.8) to reach & sear the power — double-edged, proven both ways. The leash by which he may drag the power to the Mirror.
3. **The power in the deep Shinomen** *(w2)* — Nameless, older than the Empire & the Kami; cannot be killed, only BOUND; its one fear is the sun. STUNG (Sc.8): Akihiko ran sun-fire up a soul-thread and wounded it — first hurt in 1200 years; it now knows his fire all the way down, fixed on him.
4. **The taken souls of Hibari Mura** *(w2)* — Gathered & woven toward some purpose, NOT destroyed. PROVEN partly reclaimable (Sc.8): Akihiko's sun-fire severed one puppet-thread & freed a boy's body — the soul still in the deep (the Mirror is the full cure).
5. **The leak / the Scorpion closing in** *(w2)* — The Scorpion acted on it — and the ambush was DEFEATED, Gennai captured (Sc.9). Immediate threat foiled; but the broader word is out and the cell will react to losing him. Now entangled with the Emerald Magistrate's Scorpion investigation.
6. **Lord Hatsue's fraying mind** *(w1)* — Spending her sight on the threat; declining at home while Akihiko is away.
7. **The Imperial (Seppun) blood — known heritage** *(w1)* — No buried secret: runs through grandmother Seppun Yuki (minor Imperial scion) → Sumiko → Akihiko, and grants the house a notch of extra Falcon standing. The Dawn Mirror recognized it. Still a thing high-Status others could exploit or resent.
8. **The Mirror's price — the binding consumes its anchor** *(w2)* — Hatsue's deathbed secret (Sc.11): the Dawn Mirror doesn't hold the deep power on its own — it needs a living ANCHOR who spends their self/soul/sight keeping the chain taut (the First Yotogi, the Keeper 1200y, Hatsue's 2 years of sight). To wake & wield it, the anchor is slowly consumed. Hatsue meant that anchor to be Akihiko — 'the other inheritance.'
9. **The Falcon's fate — the Lion protectorate (independence vs survival)** *(w2)* — Karō Ujiyasu's deal: submit the Falcon as a vassal of the LION (an Akodo lord, eastern hills) — garrison, granaries, protection vs the Scorpion & the dark — for fealty/independence. Hatsue refused (she gambled on the First Ward). Deferred to morning; now Lady Chiyo's seal to give or refuse. (Note: Matsu Toshimoko is Lion.)
10. **What's wrong with Chiyo (iron, undone — a hidden thing)** *(w1)* — Iron Chiyo — 'scariest of his peers,' breaks Lions' noses without flinching — came undone at the deathbed in a way that is NOT mere grief. Akihiko failed to read it (Sc.11); something is behind a door she's never closed before. Guilt? Fear? Knowledge? A hidden thing.

## Characters & Factions — snapshot of `characters.json` · GENERATED (NPC/force — want — disposition; PC NOT listed)
- **Gennai (Scorpion spymaster)** *(w2)* — CAPTURED (Sc.9): his leak-bought ambush in the sunken lane smashed; Akihiko ran him down and maimed his sword-hand, handed him in irons to Matsu. A captured nemesis — interrogation, escape risk, and his masters' reaction all loom. Taunted about 'who else is listening on these roads.'
- **The Scorpion Clan** *(w2)* — Their ambush cell smashed & Gennai taken (Sc.9); the land-grab continues but now under Emerald Magistrate scrutiny — and they'll move to recover or silence Gennai. Hostile, bloodied, exposed to Imperial wrath.
- **The power in the deep Shinomen** *(w2)* — Harvest souls / spread — malign, looming (quiet near the PC for now).
- **Toritaka Jōji** *(w2)* — Akihiko's closest comrade-Warden, sworn confidant; senior to him; riding home at his side, blunt and loyal.
- **The captured porter** *(w1)* — Left bound on the hill 'for the Kami to judge' (days ago): freed himself, died, or retrieved by Gennai — and remembers the Warden who left him.
- **Matsu Toshimoko (Emerald Magistrate)** *(w3)* — ALLY now (Sc.9): Akihiko handed her a live Scorpion agent, cracking her marches-investigation open; rides to Kyūden Toritaka as ally, not inquisitor — still owed Lord Hatsue's answers. Vowed the Scorpion will answer to the Throne for the ambush.
- **The freed boy of Hibari Mura** *(w1)* — A Hibari Mura reed-cutter the deep power puppeted across the ford; Akihiko severed the thread with Sacred sun-fire. Body alive & reclaimed, soul still gathered in the deep — soul-empty like Suzu.
- **Toritaka Chiyo (new Lady of the Falcon)** *(w2)* — Hatsue's eldest daughter; tough-as-nails, the scariest of Akihiko's peers; NEW Lady of the Falcon (the seat). Leans on Akihiko's steadiness in the crisis. Carrying something hidden (see thread). Holds the deal-decision.
- **Toritaka Ujiyasu (karō)** *(w1)* — The clan's karō (seneschal); aged, ran the household for generations. A frightened pragmatist, NOT wicked — negotiated the Lion protectorate to save a drowning clan. Deferred to morning; will press the deal again.

## Adventure Features (prepared-adventure mode only)
- n/a (Pure Mythic)

## Campaign roster (persists across adventures: recurring NPCs, long arcs — full detail in `setting-canon.md`)
- **Gennai** — Scorpion spymaster; recurring antagonist who knows Akihiko's face and that he hides something. **CAPTURED (Sc.9)**, sword-hand maimed, in Matsu's irons — interrogation / escape / his masters' reaction all loom.
- **Lord Toritaka Hatsue, "the Yotogi"** — Akihiko's lord, hard mentor, secret-sharer. **DIED (Sc.11)** — held on for the Mirror; named Akihiko "the other inheritance" (the ward, not the seat); revealed the Mirror's price, then passed. → `archive.md`.
- **Toritaka Chiyo** — Hatsue's eldest daughter; iron, the scariest of Akihiko's peers; **NEW Lady of the Falcon** (Sc.11). Holds the seat & the Lion-deal decision; leans on Akihiko's steadiness; carrying a hidden thing.
- **Toritaka Ujiyasu** — the clan's aged *karō*; a frightened pragmatist (not wicked) who brokered the Lion protectorate to save a drowning clan.
- **Family** — Akiro (brother, apprentice healer), Hizashi (father, heretic Centipede sun-priest), Sumiko (mother; carrier of the Seppun blood), **Seppun Yuki** (grandmother; minor Imperial scion, family matriarch, keeper of the line's truth).
- **Suzu** — sole survivor of Hibari Mura's soul-harvest; soul-shocked, bonded to her rescuer; the only living witness; recovering with Akiro at Kyūden Toritaka.
- **Toritaka Jōji** — Akihiko's closest comrade-Warden; senior; rode to the barrow and home.
- **The Scattered Corps** — healers & wardens of many clans bound to Akihiko by a past crisis; far apart on duty (Eniko, Genzō, Bara, Hiroyuki, Saburō, Kasumi).
- **Matsu Toshimoko** — Emerald Magistrate (Lion); witnessed the ford, then the lane. **Now an ally (Sc.9)** after Akihiko handed her a live Scorpion; rides to Kyūden Toritaka, still owed Lord Hatsue's answers.
- **The freed boy of Hibari Mura** — reclaimed from the deep power's puppetry by Akihiko's sun-fire; body alive, soul still taken (a second soul-shocked survivor, like Suzu).
- **Long arcs:** the Seppun blood (who exploits or honors it); the Dawn Mirror's binding-duty (cure the mark · free the souls · bind the deep power).

## Clocks (offscreen factions / threats / progress — advanced by `tick.py`; the night of Hatsue's death, Kyūden Toritaka)
- **Hatsue's decline → RESOLVED:** she **DIED** (Sc.11), her watch ended; the clan grieves and holds one night.
- **The succession & the Lion deal:** Lady **Chiyo** now holds the seat & the deal-decision; Ujiyasu's protectorate offer is deferred to morning — a dawn fork: independence (the Mirror's gamble) vs survival (Lion vassalage).
- **Scorpion (post-ambush):** bloodied, Gennai captive in the cellars; regrouping to recover/silence him; the marches still contested.
- **The Shinomen harvest:** active — the WOUNDED deep power regroups offscreen, fixed on Akihiko (whose Mirror, he now knows, will consume its wielder).
- **Imperial scrutiny → alliance:** Matsu Toshimoko present — an ally owed answers, who just heard her own clan (Lion) named as the Falcon's would-be protector.

## Overlays
- **Keyed Scenes:** none
- **Thread Progress Track:** none
- **Peril Points:** OFF _(player-invoked only)_

## Adventure Crafter state (crafter mode only)
- n/a (Pure Mythic)

## Current scene — Scene 11: *The High Room* (Interrupt · Turning Point) → **CLOSED**
- **Where / when:** Lord Hatsue's death-chamber, night; the clan gathered, then cleared to the principals.
- **Last beat (2–3 sentences):** Scene Test 2 vs CF 4 → Interrupt; the Turning Point CONCLUDED the *Ninjō — to belong* thread. Hatsue, dying & lucid (no witchery — Fate No, Sixth Sense clear), named Akihiko her heir; he redirected it (success) toward her daughter **Chiyo** to keep the succession clean. At her side she revealed the **Mirror's price** (it consumes its living anchor — she meant Akihiko), named him "the other inheritance — the ward, not the seat," then DIED. Akihiko cleared the room to the principals, learned of **karō Ujiyasu's Lion-protectorate deal**, and steadied the new Lady Chiyo — counseling unity and deferring the decision to morning.
- **Akihiko's state:** strife **3/8** (redirect +1; held grief +2), fatigue 0/10, Void 2/2; bears the Dawn Mirror — and now knows its price. Honor 55 / Glory 41 / Status 36. XP 0 (tally at session-end). **Ninjō resolved:** he belongs now — as the clan's anchor/ward ("the other inheritance"), the role that will consume him.
- **Stakes on the table now:** the clan holds one night. By morning: Chiyo's decision on the Lion deal (independence vs survival); the Mirror's terrible price; what's wrong with Chiyo; the Emerald Magistrate owed answers (with her own clan now in the frame); the captive Gennai. A natural session/chapter pause.
- **Self-audit drift counter (consecutive soft scenes):** 0

## Archive pointer
- Resolved threads / dead characters → `archive.md` (Keeper *Toritaka Genkō*; the gaki *Kuchinashi*; Arc 1 summary).
