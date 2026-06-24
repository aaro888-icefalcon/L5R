#!/usr/bin/env python3
"""
render_lists.py — make the JSON Lists the SINGLE SOURCE OF TRUTH and GENERATE the
human-readable Markdown snapshot from them, so the snapshot can never drift.

The engine rolls the dice over threads.json / characters.json (machine source). The
"## Threads" / "## Characters & Factions" sections in campaign-state.md are a *derived*
view. Edit the JSON (weight via mythic-gm state.py thread|char; prose via `set-note`
here), then re-render — never hand-edit the snapshot.

Entry schema (extends the engine's {name, weight} with an optional prose note):
    {"name": "...", "weight": 1..3, "note": "<the human annotation>"}

Commands (run from the repo root):
  render <campaign> [--in-place] [--check]
        no flag      → print the two regenerated snapshot blocks to stdout (preview)
        --in-place   → splice them into <campaign>/campaign-state.md (the drift-killer)
        --check      → exit 1 if the file's snapshot differs from what render would emit
                       (a forcing function: wire into bookkeeping / pre-commit)
  set-note <campaign> thread|character "<name>" "<note>"
        set/replace the prose note on a JSON entry (so the JSON stays the single source)

Examples:
  python3 .claude/skills/l5r-gm/scripts/render_lists.py render campaigns/<slug> --in-place
  python3 .claude/skills/l5r-gm/scripts/render_lists.py render campaigns/<slug> --check
  python3 .claude/skills/l5r-gm/scripts/render_lists.py set-note campaigns/<slug> thread "The Mark" "contained; the leash"
"""
import json, os, sys

KIND_FILE = {"thread": "threads.json", "character": "characters.json"}
HEADERS = {
    "thread":    "## Threads — snapshot of `threads.json` · GENERATED (edit the JSON + re-render; do not hand-edit)",
    "character": "## Characters & Factions — snapshot of `characters.json` · GENERATED (NPC/force — want — disposition; PC NOT listed)",
}

def _load(campaign, kind):
    p = os.path.join(campaign, KIND_FILE[kind])
    if not os.path.exists(p):
        sys.exit(f"No {KIND_FILE[kind]} in {campaign} — run the engine's state.py to create the JSON Lists first.")
    obj = json.load(open(p, encoding="utf-8"))
    obj.setdefault("kind", kind); obj.setdefault("entries", [])
    for e in obj["entries"]:
        e.setdefault("weight", 1)
    return obj

def _save(campaign, obj):
    p = os.path.join(campaign, KIND_FILE[obj["kind"]])
    json.dump(obj, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

def _block(campaign, kind):
    """Return the generated snapshot block (list of lines) for one List."""
    obj = _load(campaign, kind)
    lines = [HEADERS[kind]]
    bullet = (lambda i: f"{i}.") if kind == "thread" else (lambda i: "-")
    if not obj["entries"]:
        lines.append("_(empty)_")
    for i, e in enumerate(obj["entries"], 1):
        note = (e.get("note") or "").strip()
        tail = f" — {note}" if note else ""
        lines.append(f"{bullet(i)} **{e['name']}** *(w{int(e.get('weight',1))})*{tail}")
    lines.append("")   # trailing blank before the next "## " section
    return lines

def _splice(text, header_prefix, new_block):
    """Replace the section whose header startswith header_prefix (header line through the
    line before the next '## ') with new_block. Returns (text, replaced?)."""
    lines = text.split("\n"); out = []; i = 0; n = len(lines); replaced = False
    while i < n:
        if not replaced and lines[i].startswith(header_prefix):
            out.extend(new_block); i += 1
            while i < n and not lines[i].startswith("## "):
                i += 1
            replaced = True
            continue
        out.append(lines[i]); i += 1
    return "\n".join(out), replaced

def cmd_render(campaign, in_place=False, check=False):
    blocks = {k: _block(campaign, k) for k in ("thread", "character")}
    if not in_place and not check:
        for k in ("thread", "character"):
            print("\n".join(blocks[k]))
        return
    path = os.path.join(campaign, "campaign-state.md")
    if not os.path.exists(path): sys.exit(f"No campaign-state.md in {campaign}")
    orig = open(path, encoding="utf-8").read()
    text = orig
    prefixes = {"thread": "## Threads", "character": "## Characters & Factions"}
    missing = []
    for k in ("thread", "character"):
        text, ok = _splice(text, prefixes[k], blocks[k])
        if not ok: missing.append(prefixes[k])
    if missing:
        sys.exit("Could not find section header(s) to replace: " + ", ".join(missing))
    if check:
        if text != orig:
            print("DRIFT: campaign-state.md snapshot is OUT OF SYNC with the JSON Lists.")
            print("  Fix: render_lists.py render %s --in-place" % campaign)
            sys.exit(1)
        print("In sync ✓  (snapshot matches threads.json / characters.json)")
        return
    open(path, "w", encoding="utf-8").write(text)
    print(f"Rendered snapshot → {path}")
    for k in ("thread", "character"):
        print(f"  {prefixes[k]}: {len(_load(campaign,k)['entries'])} entr(y/ies)")

def cmd_set_note(campaign, kind, name, note):
    kind = {"thread": "thread", "threads": "thread", "char": "character",
            "character": "character", "characters": "character"}.get(kind, kind)
    if kind not in KIND_FILE: sys.exit("kind must be thread|character")
    obj = _load(campaign, kind); key = name.strip().lower()
    hit = next((e for e in obj["entries"] if e["name"].strip().lower() == key), None)
    if hit is None:
        # tolerant: match on startswith so short handles work
        hit = next((e for e in obj["entries"] if e["name"].strip().lower().startswith(key)), None)
    if hit is None:
        sys.exit(f"No {kind} entry matching '{name}'. Existing: " +
                 ", ".join(e["name"] for e in obj["entries"]))
    hit["note"] = note.strip(); _save(campaign, obj)
    print(f"{kind} '{hit['name']}': note set ({len(note.strip())} chars). Re-render to update the snapshot.")

def main():
    a = sys.argv[1:]
    if not a or a[0] in ("-h", "--help"): print(__doc__); return
    c = a[0]
    if c == "render":
        if len(a) < 2: sys.exit("render <campaign> [--in-place] [--check]")
        cmd_render(a[1], "--in-place" in a, "--check" in a)
    elif c == "set-note":
        if len(a) < 5: sys.exit('set-note <campaign> thread|character "<name>" "<note>"')
        cmd_set_note(a[1], a[2], a[3], a[4])
    else:
        sys.exit(f"Unknown command '{c}'. See --help.")

if __name__ == "__main__":
    main()
