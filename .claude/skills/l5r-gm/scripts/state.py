#!/usr/bin/env python3
"""Campaign/character/conflict state helpers. campaign-state.md is the source of truth.

  state.py init [--dir .]         # write starter campaign-state.md + character-sheet.md from templates
  state.py validate <file>        # check required structure (active_set, character sheet)
"""
import argparse, os, re, shutil

TPL = os.path.join(os.path.dirname(__file__), "..", "assets", "templates")

def cmd_init(a):
    os.makedirs(a.dir, exist_ok=True)
    for t in ("campaign-state.md", "character-sheet.md", "conflict-tracker.md"):
        src = os.path.join(TPL, t); dst = os.path.join(a.dir, t)
        if os.path.exists(src) and not os.path.exists(dst):
            shutil.copy(src, dst); print("wrote", dst)
        elif os.path.exists(dst):
            print("exists (kept):", dst)

def cmd_validate(a):
    txt = open(a.file, encoding="utf-8").read()
    checks = {
        "active_set block": "active_set" in txt,
        "Chaos Factor": re.search(r"chaos", txt, re.I) is not None,
        "Threads list": re.search(r"thread", txt, re.I) is not None,
        "a PC / character ref": re.search(r"character|PC|samurai", txt, re.I) is not None,
    }
    ok = all(checks.values())
    for k, v in checks.items():
        print(f"  [{'OK' if v else '!!'}] {k}")
    print("VALID" if ok else "INCOMPLETE — fill the missing fields before play")

def main():
    p = argparse.ArgumentParser(); sub = p.add_subparsers(dest="cmd", required=True)
    i = sub.add_parser("init"); i.add_argument("--dir", default="."); i.set_defaults(func=cmd_init)
    v = sub.add_parser("validate"); v.add_argument("file"); v.set_defaults(func=cmd_validate)
    a = p.parse_args(); a.func(a)

if __name__ == "__main__":
    main()
