#!/usr/bin/env python3
"""
build.py — companion generator build step for the l5r-gm bridge.

Emits verified, machine-rollable JSON tables (the engine's list_d100 schema) from
the L5R-native word lists below, so they get the same coverage guarantee Mythic's
tables get. Single source of truth = this file's lists.

Each table is a contiguous 1d100 range table; ranges are auto-distributed so
coverage == 100 (what `bridge.py validate` roll-tests). Re-run after editing a list:

    python3 .claude/skills/l5r-gm/bridge/generators/build.py

Then roll any table honestly with:

    python3 .claude/skills/mythic-gm/scripts/dice.py table \
        .claude/skills/l5r-gm/bridge/generators/<name>.json
"""
import json, os, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))


def sha(s):
    return "sha256:" + hashlib.sha256(s.encode("utf-8")).hexdigest()[:16]


def even_d100(values):
    """Distribute 1..100 across len(values) contiguous entries (coverage == 100)."""
    n = len(values)
    base, extra = divmod(100, n)
    entries, lo = [], 1
    for k, v in enumerate(values):
        size = base + (1 if k < extra else 0)
        hi = lo + size - 1
        entries.append({"min": lo, "max": hi, "value": v})
        lo = hi + 1
    return entries


def write(name, title, values, note=""):
    entries = even_d100(values)
    obj = {
        "id": f"l5r.{name}", "title": title, "type": "list_d100", "dice": "1d100",
        "source": "l5r-gm/bridge/generators/build.py", "entries": entries,
        "checksum": sha(str(entries)),
    }
    if note:
        obj["note"] = note
    p = os.path.join(HERE, f"{name}.json")
    json.dump(obj, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return name, len(values)


# ── Family names — great + minor clan families (clan is a SOFT sort, never a gate) ──
FAMILY_NAMES = [
    "Hida", "Hiruma", "Kaiu", "Kuni", "Yasuki",            # Crab
    "Doji", "Kakita", "Daidoji", "Asahina",                # Crane
    "Togashi", "Mirumoto", "Kitsuki", "Agasha",            # Dragon
    "Akodo", "Matsu", "Kitsu", "Ikoma",                    # Lion
    "Isawa", "Shiba", "Asako",                             # Phoenix
    "Bayushi", "Shosuro", "Soshi", "Yogo",                 # Scorpion
    "Shinjo", "Moto", "Iuchi", "Utaku", "Ide",             # Unicorn
    "Moshi", "Toritaka", "Yoritomo", "Tsuruchi", "Suzume",  # Minor clans
]

# ── Given names — mixed; evocative, period-plausible ──
GIVEN_NAMES = [
    "Hotaru", "Kachiko", "Toshimoko", "Sukune", "Yoshi", "Tetsuko", "Satsume",
    "Sumiko", "Hatsue", "Akiro", "Hizashi", "Yuki", "Kasumi", "Eniko", "Genzo",
    "Hiroyuki", "Saburo", "Joji", "Tomiko", "Reiko", "Kenji", "Daichi", "Emi",
    "Naoki", "Aiko", "Haru", "Michiko", "Toku", "Shizue", "Renjiro",
    "Masako", "Goro", "Chiyo", "Ujimitsu",
]

# ── NPC social role / station (for a new Character; layer over the Character Crafter) ──
NPC_ROLES = [
    "peasant farmer / heimin", "ashigaru (foot-soldier)", "bushi of a clan",
    "ronin (masterless)", "courtier", "magistrate / yoriki", "shugenja (priest)",
    "monk / brotherhood of Shinsei", "merchant patron (via a samurai front)",
    "artisan (smith / poet / painter)", "geisha / entertainer", "innkeeper / tea-house host",
    "village headman / nanushi", "scout / yojimbo", "scholar / sensei", "physician / healer",
    "ji-samurai (rural vassal)", "clan emissary / yojimbo of a guest", "eta (the unclean — hidden)",
    "imperial official / Emerald Magistrate's agent", "spy / metsuke (true allegiance hidden)",
    "elder / retired samurai", "pilgrim", "bandit / hinin outlaw",
]

# ── Location type (for "a scene needs a place" in Rokugan) ──
LOCATIONS = [
    "roadside tea-house", "Shinto shrine / kami-shrine", "Fortune's temple",
    "a clan dojo", "castle audience hall", "castle gate & guardhouse", "a garden of contemplation",
    "rice paddies & irrigation dikes", "fishing / river village", "market square",
    "magistrate's office", "bathhouse", "a bridge over a gorge or river", "mountain pass / checkpoint",
    "a noble's private chambers", "graveyard / ancestral barrow", "harbor & docks",
    "a monastery in the hills", "the deep wilds / haunted forest edge", "a battlefield or its aftermath",
    "winter court's guest wing", "a peasant longhouse", "a merchant's warehouse (samurai-fronted)",
    "the open road between provinces",
]


def main():
    built = []
    built.append(write("family_name", "L5R — Family Names", FAMILY_NAMES,
                       "Clan is a soft sort, never an actor-gate. Pair with given_name for a full name."))
    built.append(write("given_name", "L5R — Given Names", GIVEN_NAMES))
    built.append(write("npc_role", "L5R — NPC Role / Station", NPC_ROLES,
                       "Conjunction: layer over the AC Character Crafter for a new generic NPC."))
    built.append(write("location", "L5R — Rokugani Location Types", LOCATIONS))
    print("BUILT companion generator tables:")
    for name, n in built:
        print(f"  {name:14} {n:>3} entries -> 1d100 (coverage 100)")
    print("VERIFY: python3 .claude/skills/mythic-gm/scripts/bridge.py validate .claude/skills/l5r-gm/bridge")


if __name__ == "__main__":
    main()
