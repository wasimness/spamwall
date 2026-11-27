"""CI checks: regexes compile, no allow/block overlap on official series,
no personal-looking data, every pattern file is well formed, and generated
files match the rule sources."""
import json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors = []
ids = {}
for txt in (ROOT / "rules").rglob("*.txt"):
    folder = txt.parent.name
    n_rules = 0
    text = txt.read_text(encoding="utf-8")
    for n, line in enumerate(text.splitlines(), 1):
        s = line.split("#")[0].strip()
        if not s or txt.name == "allow-apps.txt":
            continue
        n_rules += 1
        try:
            re.compile(s)
        except re.error as e:
            errors.append(f"{txt}:{n} bad regex: {e}")
        parts = [p.strip() for p in line.partition("#")[2].split("|")]
        if len(parts) < 3 or not all(parts):
            errors.append(f"{txt}:{n} needs a '# ID | what | source' comment")
            continue
        if parts[0] != txt.stem:
            errors.append(f"{txt}:{n} ID {parts[0]} does not match file name")
        if parts[0] in ids:
            errors.append(f"{txt}:{n} duplicate ID {parts[0]}")
        ids[parts[0]] = txt
        if folder == "block" and (re.match(s, "1600000000") or re.match(s, "1601000000")):
            errors.append(f"{txt}:{n} blocks an official 1600/1601 number")
    if folder in {"allow", "block", "optional"}:
        if n_rules != 1:
            errors.append(f"{txt}: must hold exactly one pattern line")
        for key in ("Source:", "False-positive risk:"):
            if f"# {key}" not in text:
                errors.append(f"{txt}: header comment missing '{key}'")
secret = re.compile(r"github_pat_|ghp_|sk-[A-Za-z0-9]{10}|Bearer |password=|api[_-]?key", re.I)
for f in ROOT.rglob("*"):
    if f.is_file() and ".git" not in f.parts and f.suffix in {".txt", ".md", ".json", ".yml", ".py"}:
        t = f.read_text(encoding="utf-8", errors="ignore")
        if f.name != "check.py" and secret.search(t):
            errors.append(f"{f}: looks like a secret")


def gen():
    paths = list((ROOT / "spamblocker").glob("*")) + list((ROOT / "rules").rglob("patterns.md"))
    return {str(p.relative_to(ROOT)): p.read_bytes() for p in paths}


before = gen()
subprocess.run([sys.executable, "-I", str(ROOT / "tools" / "build_spamblocker.py")], check=True, capture_output=True)
after = gen()
if before != after:
    errors.append("generated files are out of date: run tools/build_spamblocker.py and commit")
d = json.loads((ROOT / "spamblocker" / "complete.json").read_text(encoding="utf-8"))
rl = d["numberRules"]["rules"]
shared = {r["priority"] for r in rl if r["isBlacklist"]} & {r["priority"] for r in rl if not r["isBlacklist"]}
if shared:
    errors.append(f"allow and block share priority {shared}")
print("\n".join(errors) or "all checks passed")
sys.exit(1 if errors else 0)
