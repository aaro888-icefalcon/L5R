#!/usr/bin/env python3
"""L5R 5E roll-and-keep dice engine. Honest dice, shown — never invent a result.

Commands:
  check   --ring R --skill S --tn T [--keep auto|i,j,..] [--add-ring N] [--add-skill N]
          [--reroll i,j] [--void-keep] [--json]
  simulate --ring R --skill S --tn T [--trials N]        # Monte-Carlo success probability
  roll    NdM[+k]                                         # generic dice for tables (e.g. 1d10)

A "check" rolls (ring [+add]) Ring dice and (skill [+add]) Skill dice, explodes explosive
successes, then keeps up to <ring> dice. Only KEPT dice contribute successes / strife / opportunity
(this is the core L5R tension). Success = #(success+explosive) on kept dice vs TN.
"""
import argparse, json, os, sys, itertools, re
from random import SystemRandom

RNG = SystemRandom()
FACES = json.load(open(os.path.join(os.path.dirname(__file__), "..", "data", "dice_faces.json")))
SYM = {"success": "▲", "explosive": "❂", "opportunity": "●", "strife": "✷"}

def roll_die(kind):
    faces = FACES[kind]["faces"]
    idx = RNG.randint(0, FACES[kind]["sides"] - 1)
    return {"kind": kind, "face": idx + 1, "symbols": list(faces[idx])}

def roll_pool(n_ring, n_skill, explode=True, _cap=200):
    pool = [roll_die("ring") for _ in range(n_ring)] + [roll_die("skill") for _ in range(n_skill)]
    if explode:
        queue = list(pool)
        while queue and _cap > 0:
            d = queue.pop()
            if "explosive" in d["symbols"]:
                nd = roll_die(d["kind"]); nd["exploded"] = True
                pool.append(nd); queue.append(nd); _cap -= 1
    return pool

def die_tally(d):
    s = d["symbols"]
    return (s.count("success") + s.count("explosive"),  # successes
            s.count("strife"),
            s.count("opportunity"))

def recommend_keep(pool, ring_value, tn):
    """Play-to-win: maximize successes, then minimize strife, then maximize opportunity."""
    n = len(pool)
    cap = min(ring_value, n)
    best, best_key = (), None
    for size in range(0, cap + 1):
        for combo in itertools.combinations(range(n), size):
            su = st = op = 0
            for i in combo:
                a, b, c = die_tally(pool[i]); su += a; st += b; op += c
            key = (su, -st, op)
            if best_key is None or key > best_key:
                best_key, best = key, combo
    return list(best)

def resolve(pool, kept_idx, tn):
    su = st = op = 0
    for i in kept_idx:
        a, b, c = die_tally(pool[i]); su += a; st += b; op += c
    return {"successes": su, "strife": st, "opportunity": op, "tn": tn,
            "result": "SUCCESS" if su >= tn else "FAILURE",
            "bonus_successes": max(0, su - tn) if su >= tn else 0,
            "shortfall": max(0, tn - su) if su < tn else 0}

def fmt_die(d, i, kept):
    syms = " ".join(SYM[s] for s in d["symbols"]) or "·"
    mark = "*" if i in kept else " "
    ex = "!" if d.get("exploded") else " "
    return f"  [{mark}] d{i}{ex} {d['kind'][0].upper()}{d['face']:<2} {syms}"

def cmd_check(a):
    n_ring = a.ring + a.add_ring
    n_skill = a.skill + a.add_skill
    pool = roll_pool(n_ring, n_skill)
    # optional one-time rerolls (distinctions/adversities), by index, before keep
    if a.reroll:
        for i in [int(x) for x in a.reroll.split(",") if x.strip().isdigit()]:
            if 0 <= i < len(pool):
                pool[i] = roll_die(pool[i]["kind"])
        # exploded dice from rerolls
        for d in list(pool):
            while "explosive" in d["symbols"]:
                nd = roll_die(d["kind"]); nd["exploded"] = True; pool.append(nd); d = nd
    keep_cap = a.ring + (1 if a.void_keep else 0)
    if a.keep == "auto":
        kept = recommend_keep(pool, keep_cap, a.tn)
    elif a.keep:
        kept = [int(x) for x in a.keep.split(",") if x.strip().isdigit()]
    else:
        kept = None  # show recommendation, let player choose
    rec = recommend_keep(pool, keep_cap, a.tn)
    shown = kept if kept is not None else rec
    res = resolve(pool, shown, a.tn)
    if a.json:
        print(json.dumps({"pool": pool, "kept": shown, "result": res}, ensure_ascii=False)); return
    print("[Adjudication: roll-and-keep]")
    print(f"  Pool: {n_ring} Ring + {n_skill} Skill dice | TN {a.tn} | keep up to {keep_cap}"
          + ("  (+1 Void)" if a.void_keep else ""))
    print(f"  Symbols: {SYM['success']} success  {SYM['explosive']} explosive(success+explodes)  "
          f"{SYM['opportunity']} opportunity  {SYM['strife']} strife   ! = exploded   * = kept")
    for i, d in enumerate(pool):
        print(fmt_die(d, i, shown))
    if kept is None:
        print(f"  Recommended keep (play-to-win): {rec}  — PLAYER CHOOSES; re-run with --keep i,j,..")
    print(f"  => Kept {shown}: {res['successes']} successes vs TN {a.tn} -> {res['result']}"
          + (f" (+{res['bonus_successes']} bonus)" if res['bonus_successes'] else "")
          + (f" (short {res['shortfall']})" if res['shortfall'] else ""))
    print(f"     Opportunity available: {res['opportunity']}   Strife gained: {res['strife']}")
    if res['strife']:
        print(f"     -> add {res['strife']} strife to the character; check against composure (unmask if exceeded)")

def cmd_simulate(a):
    wins = 0
    for _ in range(a.trials):
        pool = roll_pool(a.ring, a.skill)
        kept = recommend_keep(pool, a.ring, a.tn)
        if resolve(pool, kept, a.tn)["successes"] >= a.tn:
            wins += 1
    p = wins / a.trials
    print(f"P(success) ring {a.ring}, skill {a.skill}, TN {a.tn}, keep-to-win: "
          f"{p:.3f}  ({wins}/{a.trials})")

def cmd_roll(a):
    m = re.fullmatch(r"(\d+)d(\d+)([+-]\d+)?", a.expr)
    if not m:
        print("usage: roll NdM[+k]"); return
    n, sides, mod = int(m.group(1)), int(m.group(2)), int(m.group(3) or 0)
    rolls = [RNG.randint(1, sides) for _ in range(n)]
    print(f"[Adjudication] {a.expr}: {rolls} + {mod} = {sum(rolls) + mod}")

def main():
    p = argparse.ArgumentParser(description="L5R roll-and-keep engine")
    sub = p.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("check"); c.add_argument("--ring", type=int, required=True)
    c.add_argument("--skill", type=int, required=True); c.add_argument("--tn", type=int, required=True)
    c.add_argument("--keep", default=None); c.add_argument("--add-ring", type=int, default=0)
    c.add_argument("--add-skill", type=int, default=0); c.add_argument("--reroll", default=None)
    c.add_argument("--void-keep", action="store_true"); c.add_argument("--json", action="store_true")
    c.set_defaults(func=cmd_check)
    s = sub.add_parser("simulate"); s.add_argument("--ring", type=int, required=True)
    s.add_argument("--skill", type=int, required=True); s.add_argument("--tn", type=int, required=True)
    s.add_argument("--trials", type=int, default=20000); s.set_defaults(func=cmd_simulate)
    r = sub.add_parser("roll"); r.add_argument("expr"); r.set_defaults(func=cmd_roll)
    a = p.parse_args(); a.func(a)

if __name__ == "__main__":
    main()
