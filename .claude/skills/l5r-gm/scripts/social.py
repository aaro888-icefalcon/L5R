#!/usr/bin/env python3
"""
social.py — Honor / Glory / Status / Titles, the L5R 5E social-standing ledger.

These three social attributes (and the titles that move Status) used to live only as
hand-written numbers in character-sheet.md, with no rules enforcement — which is exactly
how a PC's standing drifts upward for free. This tool makes every change COSTED, LOGGED,
and VISIBLE, per the rules in references/resolution/ and references/gm/running-the-game.md.

Source of truth: campaigns/<slug>/social.json  (character-sheet.md should point here).

Rules baked in (L5R 5E core):
  • Each attribute is 0..100; its RANK is the tens digit (value//10, or 10 at 100).
  • Table 7-1 award/forfeit SCALE is computed from the CURRENT rank:
        trifling = 1      minor = rank      major = rank x2      massive = rank x4
  • Honor is INTERNAL (changes regardless of witnesses); Glory is EXTERNAL (public deeds);
    Status is STATIC — it moves almost only via TITLES (each title carries a Status Award,
    usually capped, plus an XP-to-completion track that unlocks a title ability).
  • Decreases are the PLAYER's choice (forfeit / stake), never a GM penalty — this tool
    records them; it does not impose them.
  • THRESHOLDS: when Honor or Glory crosses above 64 the character gains a virtue/fame
    advantage; when it falls below 30 they gain a flaw/infamy (Tables 7-2 / 7-3). The tool
    ALARMS on every crossing so it is never silently ignored.

Commands:
  init <campaign> [--name N] [--honor H] [--glory G] [--status S]
  show <campaign>
  award   <campaign> <honor|glory|status> <trifling|minor|major|massive|N> "reason"
  forfeit <campaign> <honor|glory|status> <trifling|minor|major|massive|N> "reason"
  stake   <campaign> <honor|glory|status> <scale|N> "what is staked on / lost if"
  resolve-stake <campaign> <#index> <kept|lost>
  set     <campaign> <honor|glory|status> <value> "reason"      (resets / direct sets)
  title <campaign> add "Name" --award N [--cap M] --xp N [--ability "..."] [--by "..."]
  title <campaign> xp "Name" <points>               (advance completion; unlocks ability)
  title <campaign> list
  title <campaign> remove "Name"
  log <campaign> [--n N]
  rank <value>                                       (utility: print the rank of a value)
"""
import os, sys, json, argparse

ATTRS = ("honor", "glory", "status")
SCALES = ("trifling", "minor", "major", "massive")


# ----- json io -----------------------------------------------------------------
def _path(campaign):
    return os.path.join(campaign, "social.json")

def load(campaign):
    p = _path(campaign)
    if not os.path.exists(p):
        sys.exit(f"no social.json in {campaign} — run: social.py init {campaign}")
    with open(p, encoding="utf-8") as f:
        return json.load(f)

def save(campaign, data):
    with open(_path(campaign), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
        f.write("\n")


# ----- rules -------------------------------------------------------------------
def rank(value):
    """Rank = tens digit; 10 at exactly 100."""
    v = max(0, min(100, int(value)))
    return 10 if v == 100 else v // 10

def scale_points(scale, cur_rank):
    s = scale.lower()
    if s == "trifling": return 1
    if s == "minor":    return max(1, cur_rank)
    if s == "major":    return max(1, cur_rank * 2)
    if s == "massive":  return max(1, cur_rank * 4)
    raise ValueError(scale)

def resolve_amount(token, cur_rank):
    """A scale word (computed from rank) or a literal integer."""
    if token.lower() in SCALES:
        return scale_points(token, cur_rank), token.lower()
    return abs(int(token)), f"{abs(int(token))} pts (explicit)"

def crossings(attr, old, new):
    """Threshold alarms for honor/glory (64 up = virtue/fame; 30 down = flaw/infamy)."""
    if attr == "status":
        return []
    out = []
    if old <= 64 < new:
        out.append("↑ crossed 64 — GAINS a virtue/fame advantage (Table 7-2/7-3): pick one")
    if old > 64 >= new:
        out.append("↓ dropped to/below 64 — LOSES the 64+ advantage")
    if old >= 30 > new:
        out.append("↓ crossed below 30 — GAINS a flaw/infamy adversity (Table 7-2/7-3): pick one")
    if old < 30 <= new:
        out.append("↑ rose to/above 30 — LOSES the sub-30 adversity")
    return out


# ----- mutation core -----------------------------------------------------------
def _apply(campaign, attr, delta, scale_label, reason, kind):
    data = load(campaign)
    if attr not in ATTRS:
        sys.exit(f"attribute must be one of {ATTRS}")
    old = int(data.get(attr, 0))
    new = max(0, min(100, old + delta))
    data[attr] = new
    entry = {"attr": attr, "delta": new - old, "scale": scale_label,
             "reason": reason, "kind": kind, "value_after": new}
    data.setdefault("log", []).append(entry)
    save(campaign, data)
    arrow = "▲" if delta > 0 else "▼"
    print(f"{arrow} {attr.upper()} {old} → {new}  ({new - old:+d}, {scale_label}; rank {rank(old)}→{rank(new)})")
    print(f"   {kind}: {reason}")
    for c in crossings(attr, old, new):
        print(f"   ⚠ {c}")
    return data


def cmd_award(campaign, attr, token, reason):
    data = load(campaign)
    amt, label = resolve_amount(token, rank(data.get(attr, 0)))
    if attr == "status" and token.lower() in SCALES:
        print("   note: Status rarely moves by award — it normally changes via a TITLE. Proceeding.")
    _apply(campaign, attr, +amt, label, reason, "award")

def cmd_forfeit(campaign, attr, token, reason):
    data = load(campaign)
    amt, label = resolve_amount(token, rank(data.get(attr, 0)))
    _apply(campaign, attr, -amt, label, reason, "forfeit")

def cmd_stake(campaign, attr, token, reason):
    data = load(campaign)
    amt, label = resolve_amount(token, rank(data.get(attr, 0)))
    if attr != "status" and amt > int(data.get(attr, 0)):
        sys.exit(f"cannot stake {amt} {attr} — only {data.get(attr,0)} available (you may stake only what you have)")
    stake = {"attr": attr, "amount": amt, "scale": label, "reason": reason, "status": "pending"}
    data.setdefault("stakes", []).append(stake)
    save(campaign, data)
    idx = len(data["stakes"]) - 1
    print(f"⚖ STAKE #{idx}: {amt} {attr} ({label}) on — {reason}")
    print(f"   resolve with: social.py resolve-stake {campaign} {idx} <kept|lost>")

def cmd_resolve_stake(campaign, idx, outcome):
    data = load(campaign)
    stakes = data.get("stakes", [])
    i = int(idx)
    if i < 0 or i >= len(stakes): sys.exit(f"no stake #{idx}")
    st = stakes[i]
    if st["status"] != "pending": sys.exit(f"stake #{idx} already {st['status']}")
    if outcome == "kept":
        st["status"] = "kept"
        save(campaign, data)
        print(f"✓ STAKE #{idx} KEPT — no change. ({st['amount']} {st['attr']} preserved: {st['reason']})")
    elif outcome == "lost":
        st["status"] = "lost"
        save(campaign, data)
        _apply(campaign, st["attr"], -st["amount"], f"{st['scale']} (stake lost)", st["reason"], "stake-lost")
    else:
        sys.exit("outcome must be 'kept' or 'lost'")

def cmd_set(campaign, attr, value, reason):
    data = load(campaign)
    if attr not in ATTRS: sys.exit(f"attribute must be one of {ATTRS}")
    old = int(data.get(attr, 0)); new = max(0, min(100, int(value)))
    data[attr] = new
    data.setdefault("log", []).append({"attr": attr, "delta": new - old, "scale": "set",
                                       "reason": reason, "kind": "set", "value_after": new})
    save(campaign, data)
    print(f"= {attr.upper()} set {old} → {new}  (rank {rank(old)}→{rank(new)})  — {reason}")
    for c in crossings(attr, old, new): print(f"   ⚠ {c}")


# ----- titles ------------------------------------------------------------------
def cmd_title(campaign, args):
    data = load(campaign)
    data.setdefault("titles", [])
    sub = args.title_cmd
    if sub == "list":
        if not data["titles"]:
            print("  (no titles)"); return
        for t in data["titles"]:
            done = "✓ complete" if t.get("complete") else f"{t.get('xp_progress',0)}/{t.get('xp_to_completion','?')} XP"
            act = "" if t.get("active", True) else " [inactive]"
            cap = f" (cap {t['status_cap']})" if t.get("status_cap") is not None else ""
            print(f"  • {t['name']}{act} — Status award {t.get('status_award',0):+d}{cap} — {done}")
            if t.get("assigned_by"): print(f"      by: {t['assigned_by']}")
            if t.get("ability"):     print(f"      ability: {t['ability']}")
        return
    if sub == "add":
        name = args.name
        if any(t["name"] == name for t in data["titles"]):
            sys.exit(f"title '{name}' already exists")
        if any(not t.get("complete") for t in data["titles"]):
            print("   note: a character may hold only ONE INCOMPLETE title at a time (others must be complete).")
        t = {"name": name, "assigned_by": args.by or "", "status_award": args.award,
             "status_cap": args.cap, "xp_to_completion": args.xp, "xp_progress": 0,
             "ability": args.ability or "", "complete": False, "active": True}
        data["titles"].append(t)
        # apply the Status award, honouring the cap
        old = int(data.get("status", 0))
        new = old + args.award
        if args.cap is not None:
            new = min(new, args.cap) if args.award > 0 else new
        new = max(0, min(100, new))
        data["status"] = new
        data.setdefault("log", []).append({"attr": "status", "delta": new - old, "scale": "title",
                                           "reason": f"title assigned: {name}", "kind": "title", "value_after": new})
        save(campaign, data)
        print(f"★ TITLE assigned: {name}" + (f" (by {args.by})" if args.by else ""))
        print(f"   Status {old} → {new}  ({new-old:+d}" + (f", capped at {args.cap}" if args.cap is not None else "") + ")")
        if args.xp: print(f"   completion: 0/{args.xp} XP → unlocks: {args.ability or '(ability TBD)'}")
        return
    if sub == "xp":
        name = args.name
        t = next((t for t in data["titles"] if t["name"] == name), None)
        if not t: sys.exit(f"no title '{name}'")
        if t.get("complete"): sys.exit(f"title '{name}' already complete")
        t["xp_progress"] = t.get("xp_progress", 0) + int(args.points)
        msg = f"   {name}: {t['xp_progress']}/{t.get('xp_to_completion','?')} XP"
        if t.get("xp_to_completion") and t["xp_progress"] >= t["xp_to_completion"]:
            t["complete"] = True
            msg += "\n   ✓ TITLE COMPLETE — ability unlocked: " + (t.get("ability") or "(see title)")
        save(campaign, data)
        print(msg); return
    if sub == "remove":
        name = args.name
        before = len(data["titles"])
        data["titles"] = [t for t in data["titles"] if t["name"] != name]
        if len(data["titles"]) == before: sys.exit(f"no title '{name}'")
        save(campaign, data)
        print(f"removed title '{name}' (Status not auto-reverted — adjust with `set` if intended)")
        return


# ----- show / log --------------------------------------------------------------
STATUS_BANDS = [(0,"outcast/ronin-low"),(15,"low samurai / monk 25"),(30,"established samurai"),
                (40,"senior vassal / minor officer"),(50,"daimyō-tier / hatamoto"),
                (70,"clan champion-tier"),(90,"Imperial-tier")]

def cmd_show(campaign):
    data = load(campaign)
    print(f"— Social standing: {data.get('character','(PC)')} —")
    for a in ATTRS:
        v = int(data.get(a, 0))
        flags = []
        if a != "status":
            if v >= 65: flags.append("64+ → has a virtue/fame advantage")
            if v < 30:  flags.append("<30 → has a flaw/infamy")
        band = ""
        if a == "status":
            band = " — " + [d for t,d in STATUS_BANDS if v >= t][-1]
        print(f"  {a.capitalize():7} {v:3}  (rank {rank(v)}){band}" + (("   ⚠ " + "; ".join(flags)) if flags else ""))
    titles = [t for t in data.get("titles", []) if t.get("active", True)]
    if titles:
        print("  Titles:")
        for t in titles:
            done = "✓" if t.get("complete") else f"{t.get('xp_progress',0)}/{t.get('xp_to_completion','?')}xp"
            print(f"    ★ {t['name']} ({done})")
    n = len(data.get("log", []))
    if n: print(f"  ({n} ledger entries — social.py log {campaign})")

def cmd_log(campaign, nshow):
    data = load(campaign)
    log = data.get("log", [])
    if not log: print("  (no changes logged)"); return
    for e in log[-int(nshow):]:
        print(f"  {e['attr']:7} {e['delta']:+3d} → {e['value_after']:3}  [{e.get('scale','')}] {e.get('reason','')}")


# ----- init / cli --------------------------------------------------------------
def cmd_init(campaign, name, honor, glory, status):
    p = _path(campaign)
    if os.path.exists(p): sys.exit(f"{p} already exists — refusing to overwrite.")
    os.makedirs(campaign, exist_ok=True)
    data = {"kind": "social", "character": name or "", "honor": honor, "glory": glory,
            "status": status, "titles": [], "stakes": [], "log": []}
    save(campaign, data)
    print(f"Initialised {p}")
    cmd_show(campaign)


def main():
    ap = argparse.ArgumentParser(description="L5R Honor/Glory/Status/Titles ledger")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("init"); p.add_argument("campaign"); p.add_argument("--name", default="")
    p.add_argument("--honor", type=int, default=40); p.add_argument("--glory", type=int, default=30)
    p.add_argument("--status", type=int, default=30)

    for c in ("award", "forfeit"):
        p = sub.add_parser(c); p.add_argument("campaign"); p.add_argument("attr")
        p.add_argument("amount"); p.add_argument("reason")

    p = sub.add_parser("stake"); p.add_argument("campaign"); p.add_argument("attr")
    p.add_argument("amount"); p.add_argument("reason")
    p = sub.add_parser("resolve-stake"); p.add_argument("campaign"); p.add_argument("index")
    p.add_argument("outcome", choices=["kept", "lost"])

    p = sub.add_parser("set"); p.add_argument("campaign"); p.add_argument("attr")
    p.add_argument("value", type=int); p.add_argument("reason")

    p = sub.add_parser("show"); p.add_argument("campaign")
    p = sub.add_parser("log"); p.add_argument("campaign"); p.add_argument("--n", default=20)
    p = sub.add_parser("rank"); p.add_argument("value", type=int)

    p = sub.add_parser("title"); p.add_argument("campaign")
    tsub = p.add_subparsers(dest="title_cmd", required=True)
    ta = tsub.add_parser("add"); ta.add_argument("name"); ta.add_argument("--award", type=int, required=True)
    ta.add_argument("--cap", type=int, default=None); ta.add_argument("--xp", type=int, default=0)
    ta.add_argument("--ability", default=""); ta.add_argument("--by", default="")
    tx = tsub.add_parser("xp"); tx.add_argument("name"); tx.add_argument("points")
    tsub.add_parser("list"); tr = tsub.add_parser("remove"); tr.add_argument("name")

    a = ap.parse_args()
    if a.cmd == "init":        cmd_init(a.campaign, a.name, a.honor, a.glory, a.status)
    elif a.cmd == "award":     cmd_award(a.campaign, a.attr, a.amount, a.reason)
    elif a.cmd == "forfeit":   cmd_forfeit(a.campaign, a.attr, a.amount, a.reason)
    elif a.cmd == "stake":     cmd_stake(a.campaign, a.attr, a.amount, a.reason)
    elif a.cmd == "resolve-stake": cmd_resolve_stake(a.campaign, a.index, a.outcome)
    elif a.cmd == "set":       cmd_set(a.campaign, a.attr, a.value, a.reason)
    elif a.cmd == "show":      cmd_show(a.campaign)
    elif a.cmd == "log":       cmd_log(a.campaign, a.n)
    elif a.cmd == "rank":      print(f"value {a.value} → rank {rank(a.value)}")
    elif a.cmd == "title":     cmd_title(a.campaign, a)


if __name__ == "__main__":
    main()
