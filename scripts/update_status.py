#!/usr/bin/env python3
"""Validate data/resources.json, refresh GitHub metadata, regenerate README.md.

Stdlib only. Uses GITHUB_TOKEN if set (raises API rate limit).
Status: archived or no push in 180 days -> "stale"; 404 -> "missing"; otherwise "active".
Exit code 1 if the data file breaks the schema (see SCHEMA in CONTRIBUTING.md).
"""
import datetime as dt
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "resources.json"
README = ROOT / "README.md"
STALE_DAYS = 180

SECTIONS = ["Core AI", "Foundation Models", "Core ML", "MLX", "Runtimes",
            "Speech", "Evals and benchmarks", "Curated lists"]
RESULTS = {"passed", "failed", "not_tested", "n/a"}
STATUSES = {"active", "stale", "missing"}
REQUIRED = ["name", "url", "section", "what", "min_ios", "build", "status", "added", "last_checked", "stars"]


def validate(entries):
    errors = []
    for e in entries:
        label = e.get("name", "?")
        for key in REQUIRED:
            if key not in e:
                errors.append(f"{label}: missing '{key}'")
        if e.get("section") not in SECTIONS:
            errors.append(f"{label}: unknown section {e.get('section')!r}")
        if e.get("build", {}).get("result") not in RESULTS:
            errors.append(f"{label}: build.result must be one of {sorted(RESULTS)}")
        if e.get("status") not in STATUSES:
            errors.append(f"{label}: status must be one of {sorted(STATUSES)}")
        if e.get("build", {}).get("result") in {"passed", "failed"} and not e["build"].get("xcode"):
            errors.append(f"{label}: a passed/failed build needs build.xcode and build.date")
    return errors


def repo_path(url: str) -> str:
    return url.rstrip("/").split("github.com/")[1]


def fetch_repo(path: str):
    req = urllib.request.Request(f"https://api.github.com/repos/{path}")
    req.add_header("Accept", "application/vnd.github+json")
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


def cell(text):
    return str(text).replace("|", "\\|") if text not in (None, "") else "—"


def min_ios_cell(version):
    return f"iOS {version}" if version else "—"


def build_cell(b):
    result = b["result"]
    if result == "n/a":
        return "—"
    if result == "not_tested":
        return "not tested"
    word = "passed" if result == "passed" else "failed"
    return f"{word} (Xcode {b['xcode']}, {b['date']})"


def render_table(entries):
    lines = ["| Project | What it does | Min iOS | Build | License | Status | Stars |",
             "|---|---|---|---|---|---|---|"]
    for e in sorted(entries, key=lambda x: (-x["stars"], x["name"].lower())):
        badge = "" if e["status"] == "active" else f" _({e['status']})_"
        note = f" _{e['build']['note']}_" if e["build"].get("note") else ""
        lines.append(
            f"| [{e['name']}]({e['url']}){badge} | {cell(e['what'])}{note} | "
            f"{min_ios_cell(e['min_ios'])} | "
            f"{build_cell(e['build'])} | {cell(e['license'])} | {e['status']} | {e['stars']:,} |")
    return lines


def main() -> int:
    data = json.loads(DATA.read_text())
    errors = validate(data["entries"])
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1

    today = dt.date.today()
    for entry in data["entries"]:
        repo = fetch_repo(repo_path(entry["url"]))
        if repo is None:
            entry["status"] = "missing"
            continue
        pushed = dt.date.fromisoformat(repo["pushed_at"][:10])
        stale = repo["archived"] or (today - pushed).days > STALE_DAYS
        entry["status"] = "stale" if stale else "active"
        entry["last_checked"] = today.isoformat()
        entry["stars"] = repo["stargazers_count"]
        spdx = (repo.get("license") or {}).get("spdx_id")
        entry["license"] = None if spdx in (None, "NOASSERTION") else spdx
    DATA.write_text(json.dumps(data, indent=2) + "\n")

    lines = ["# Awesome iOS AI", "",
             "Curated iOS on-device and Apple AI resources. Build results are from Xcode 27.1; status is refreshed weekly.", ""]
    for section in SECTIONS:
        items = [e for e in data["entries"] if e["section"] == section]
        if not items:
            continue
        lines += [f"## {section}", ""] + render_table(items) + [""]
    lines += ["## Contributing", "",
              "Not sure which option to use? See [COMPARISON.md](COMPARISON.md).", "",
              "Adding a project? See [CONTRIBUTING.md](CONTRIBUTING.md)."]
    README.write_text("\n".join(lines) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
