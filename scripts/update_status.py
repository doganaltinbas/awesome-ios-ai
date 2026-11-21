#!/usr/bin/env python3
"""Refresh GitHub status for each entry in data/resources.json and regenerate README.md.

Stdlib only. Uses GITHUB_TOKEN if set (raises API rate limit).
Status rules: archived or no push in 180 days -> "stale"; otherwise "active".
Entries whose repo returns 404 are marked "missing" for manual review.
"""
import json
import os
import datetime as dt
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "resources.json"
README = ROOT / "README.md"
STALE_DAYS = 180


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


def main() -> None:
    data = json.loads(DATA.read_text())
    today = dt.date.today()
    for entry in data["entries"]:
        repo = fetch_repo(repo_path(entry["url"]))
        if repo is None:
            entry["status"] = "missing"
            continue
        pushed = dt.date.fromisoformat(repo["pushed_at"][:10])
        stale = repo["archived"] or (today - pushed).days > STALE_DAYS
        entry["status"] = "stale" if stale else "active"
        entry["last_verified"] = today.isoformat()
        entry["stars"] = repo["stargazers_count"]
    DATA.write_text(json.dumps(data, indent=2) + "\n")

    lines = ["# Awesome iOS AI", "", "Curated iOS on-device and Apple AI resources. Status is checked weekly.", ""]
    by_cat = {}
    for e in data["entries"]:
        by_cat.setdefault(e["category"], []).append(e)
    for cat in sorted(by_cat):
        lines += [f"## {cat}", ""]
        for e in by_cat[cat]:
            badge = "" if e["status"] == "active" else f" _({e['status']})_"
            lines.append(f"- [{e['name']}]({e['url']}) - {e['why']}{badge}")
        lines.append("")
    lines += ["## Contributing", "", "See [CONTRIBUTING.md](CONTRIBUTING.md)."]
    README.write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
