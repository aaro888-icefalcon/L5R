#!/usr/bin/env python3
"""
bridge.py — discover / validate / summarize a companion bridge.

A bridge is a folder with a bridge.md manifest (containing a fenced ```json block)
that declares which engine hooks the companion overrides and where its files are.
The engine reads the manifest at load and uses an override where present, else the
Mythic/AC default.

Commands:
  summary <bridge_dir>     Print overrides-vs-defaults for the 9 hooks
  brief <bridge_dir>       Print each overridden hook's OPERATIVE DIGEST (load contents, not names)
  validate <bridge_dir>    Check the manifest + declared files + that overrides surface a digest; roll-test tables
  manifest <bridge_dir>    Print the parsed JSON manifest
"""
import json, os, re, sys, glob

HOOKS = ["resolve","generate:character","generate:element","meaning","chaos",
         "themes","world-tick","seeds","adventure-ingest"]

def read_manifest(bdir):
    p = os.path.join(bdir, "bridge.md")
    if not os.path.exists(p): sys.exit(f"No bridge.md in {bdir}")
    txt = open(p, encoding="utf-8").read()
    m = re.search(r"```json\s*(\{.*?\})\s*```", txt, re.DOTALL)
    if not m: sys.exit("bridge.md has no ```json manifest block")
    try: return json.loads(m.group(1))
    except Exception as e: sys.exit(f"manifest JSON error: {e}")

def _manifest_safe(bdir):
    """read_manifest without exiting — returns {} when there's no usable bridge."""
    try: return read_manifest(bdir)
    except SystemExit: return {}

def char_gen(bdir):
    """Resolve the companion's NEW-character generation override, or None for the engine
    default (AC Character Crafter). Reads manifest.generators_map.character:
      {"mode": "replace"|"conjunction"|"default", "table": "generators/x.json", "note": "<lore>"}
    'replace' uses the companion generator INSTEAD of the AC Crafter; 'conjunction' uses BOTH;
    a bare note (no table) = lore-based generation the GM performs from setting-canon. Table
    paths are returned absolute. Only honored when 'generate:character' is in overrides."""
    if not bdir: return None
    man = _manifest_safe(bdir)
    if not man: return None
    gm = (man.get("generators_map") or {}).get("character")
    if not gm or "generate:character" not in man.get("overrides", []): return None
    out = dict(gm); out.setdefault("mode", "conjunction")
    if out.get("table"): out["table"] = os.path.join(bdir, out["table"])
    return out

# ── Operative digests: load a hook's IMPERATIVE (contents), not just its name ──────────────
DIGEST_RE = re.compile(r"operative digest", re.I)

def _digest(path):
    """Return (digest_text, error). Reads a file's '> **Operative digest:**' blockquote (or the
    immediately-following non-heading paragraph) so boot can load the hook's imperative, not just
    learn that an override exists. The map names a door; this opens it."""
    if not os.path.exists(path): return None, "missing file"
    lines = open(path, encoding="utf-8").read().split("\n")
    for i, l in enumerate(lines):
        if DIGEST_RE.search(l):
            out = []
            if l.lstrip().startswith(">"):                  # a blockquote digest
                j = i
                while j < len(lines) and lines[j].lstrip().startswith(">"):
                    s = lines[j].lstrip()[1:].strip()
                    if s: out.append(s)
                    j += 1
            else:                                           # a heading/marker → take following paragraph
                j = i + 1
                while j < len(lines) and not lines[j].strip(): j += 1
                while j < len(lines) and lines[j].strip() and not lines[j].lstrip().startswith("#"):
                    out.append(lines[j].strip()); j += 1
            return ("\n".join(out) if out else None), (None if out else "empty digest")
    return None, "no operative digest"

# Load-bearing hooks whose imperative MUST be surfaced (and the manifest 'files' key each lives in)
HOOK_FILE = [("resolve","system_profile"), ("world-tick","subsystems"), ("meaning","interpretation"),
             ("chaos","chaos"), ("themes","themes"), ("seeds","seeds")]

def cmd_brief(bdir):
    """Print each overridden hook's operative digest — load CONTENTS into working context, not just
    names. Boot should run this (not only `summary`), so the resolve/world-tick imperatives are
    actually present at the moment of resolution instead of merely pointed-to."""
    man = read_manifest(bdir); ov = man.get("overrides", []); files = man.get("files", {})
    print(f"OPERATIVE DIGEST — {man.get('companion','?')}")
    print("  (the imperatives BEHIND the overrides — read them; `summary` only names the hooks)")
    shown = set()
    for hook, key in HOOK_FILE:
        if hook in ov and key in files:
            dig, err = _digest(os.path.join(bdir, files[key]))
            print(f"\n▶ {hook}  [{files[key]}]")
            print("  " + dig.replace("\n", "\n  ") if dig
                  else f"  ⚠ {err} — add a '> **Operative digest:**' blockquote to this file")
            shown.add(key)
    for key, rel in files.items():
        if key in shown: continue
        dig, _e = _digest(os.path.join(bdir, rel))
        if dig: print(f"\n▶ {key}  [{rel}]\n  " + dig.replace("\n", "\n  "))

def cmd_summary(bdir):
    man = read_manifest(bdir); ov = set(man.get("overrides", []))
    print(f"Companion: {man.get('companion','?')}   engine: {man.get('engine','?')}")
    for h in HOOKS:
        hit = h in ov or any(o.startswith("generate:") for o in ov) if h.startswith("generate:") else h in ov
        print(f"  {'OVERRIDE' if h in ov else 'default ':8}  {h}")

def cmd_validate(bdir):
    man = read_manifest(bdir); problems = []
    for key, rel in man.get("files", {}).items():
        if not os.path.exists(os.path.join(bdir, rel)):
            problems.append(f"missing file '{rel}' (declared as {key})")
    for h in man.get("overrides", []):
        if h not in HOOKS and not h.startswith("generate:"):
            problems.append(f"unknown hook '{h}'")
    # roll-test any generator tables
    tested = 0
    for f in glob.glob(os.path.join(bdir, "generators", "*.json")):
        try:
            t = json.load(open(f))
            if t.get("type","").startswith("list_"):
                cov = sum(e["max"]-e["min"]+1 for e in t["entries"])
                need = 100 if t["type"]=="list_d100" else 10
                if cov != need: problems.append(f"{os.path.basename(f)}: coverage {cov}/{need}")
                tested += 1
        except Exception as e:
            problems.append(f"{os.path.basename(f)}: {e}")
    # enforcement: an overridden load-bearing hook MUST surface its imperative (a digest boot can load)
    warnings = []
    for hook, key in [("resolve","system_profile"), ("world-tick","subsystems")]:
        if hook in man.get("overrides", []) and key in man.get("files", {}):
            dig, _e = _digest(os.path.join(bdir, man["files"][key]))
            if not dig:
                warnings.append(f"{hook} override '{man['files'][key]}' has no Operative digest — boot "
                                "can't load its imperative (add a '> **Operative digest:**' blockquote)")
    if problems:
        print("INVALID:"); [print("  X", p) for p in problems]; sys.exit(1)
    tail = f"({len(man.get('overrides',[]))} overrides, {tested} generator tables roll-tested)"
    if warnings:
        print(f"Bridge valid ⚠  {tail} — {len(warnings)} enforcement warning(s):")
        [print("  ⚠", w) for w in warnings]
    else:
        print(f"Bridge valid ✓  {tail}")

def cmd_manifest(bdir):
    print(json.dumps(read_manifest(bdir), indent=2))

def main():
    a = sys.argv[1:]
    if not a or a[0] in ("-h","--help"): print(__doc__); return
    if len(a) < 2: sys.exit("Need a bridge directory.")
    {"summary":cmd_summary,"brief":cmd_brief,"validate":cmd_validate,"manifest":cmd_manifest}.get(
        a[0], lambda d: sys.exit(f"Unknown command '{a[0]}'"))(a[1])

if __name__ == "__main__":
    main()
