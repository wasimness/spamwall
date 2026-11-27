"""CI checks: regexes compile, no allow/block overlap on official series,
no personal-looking data, and import files match the rule lists."""
import json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors = []
for txt in (ROOT / "rules").rglob("*.txt"):
    for n, line in enumerate(txt.read_text(encoding="utf-8").splitlines(), 1):
        s = line.split("#")[0].strip()
        if not s or txt.name == "allow-apps.txt":
            continue
        try:
            re.compile(s)
        except re.error as e:
            errors.append(f"{txt}:{n} bad regex: {e}")
        if txt.name == "block.txt" and re.match(s, "1600000000") or txt.name == "block.txt" and re.match(s, "1601000000"):
            errors.append(f"{txt}:{n} blocks an official 1600/1601 number")
secret = re.compile(r"github_pat_|ghp_|sk-[A-Za-z0-9]{10}|Bearer |password=|api[_-]?key", re.I)
for f in ROOT.rglob("*"):
    if f.is_file() and ".git" not in f.parts and f.suffix in {".txt", ".md", ".json", ".yml", ".py"}:
        t = f.read_text(encoding="utf-8", errors="ignore")
        if f.name != "check.py" and secret.search(t):
            errors.append(f"{f}: looks like a secret")
before = {p.name: p.read_bytes() for p in (ROOT / "spamblocker").glob("*")}
subprocess.run([sys.executable, "-I", str(ROOT / "tools" / "build_spamblocker.py")], check=True, capture_output=True)
after = {p.name: p.read_bytes() for p in (ROOT / "spamblocker").glob("*")}
if before != after:
    errors.append("spamblocker/ is out of date: run tools/build_spamblocker.py and commit")
print("\n".join(errors) or "all checks passed")
sys.exit(1 if errors else 0)
