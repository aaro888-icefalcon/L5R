# World Subsystems — Rokugan / L5R 5E   (hook: world-tick; fired by tick.py at bookkeeping)
# The offscreen world keeps moving while the PC acts. At bookkeeping, tick.py reports which
# are DUE this scene; the engine then advances each honestly (roll a table / tick a clock /
# ask a Fate Question) and records it to campaign-state.md.
| subsystem            | cadence            | advance by |
|----------------------|--------------------|-----------|
| Offscreen clocks     | every scene        | tick each open Clock in campaign-state +1 toward its outcome; at full → it happens (resolve honestly) |
| Rival clan schemes   | every 3 scenes     | a clan with a live agenda makes one move: Fate Question on whether it advances, + a Meaning pair / `npc.py` for how |
| Faction standing     | on trigger: PC acts publicly / gains or loses face | adjust the relevant clan/lord's disposition & Glory/Status reaction; record it |
| The spirit-dark / Taint | every scene while in a haunted/Shadowlands region (floor CF) | the threat presses: tick its clock; a Fate Question for a new sign if none is active |
| Season & duty        | on trigger: time passes (travel, downtime, a span of days) | advance the calendar; surface any duty/obligation now due (court summons, patrol, debt) |
# Default if a row's table isn't named: advance the offscreen clock and ask a Fate Question for the detail.
