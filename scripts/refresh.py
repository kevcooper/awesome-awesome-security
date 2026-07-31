#!/usr/bin/env python3
"""Refresh the generated metadata annotations in README.md.

Every list entry ends with a generated annotation:

    - [owner/repo](https://github.com/owner/repo) — Description. — ★14.7k · 2026-01 · 💤 dormant

This script reads each GitHub link out of README.md, queries the repository API, rewrites that
trailing segment in place, and re-sorts the entries within each section by star count descending.
Descriptions are never touched.

Because ordering is generated, entry prose must not refer to other entries by position
("the list above"). Name the repository instead.

Set GITHUB_TOKEN to raise the rate limit from 60 to 5000 requests/hour.
"""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

README = Path(__file__).resolve().parent.parent / "README.md"
API = "https://api.github.com/repos/"

# Entries look like: "- [owner/repo](https://github.com/owner/repo) — prose"
ENTRY = re.compile(r"^- \[[^\]]+\]\(https://github\.com/([^/)]+)/([^/)#?]+)\)")
# The generated tail begins at the first " — ★" and runs to end of line.
TAIL = re.compile(r" — ★.*$")

DORMANT_DAYS = 548  # ~18 months


def stars(n: int) -> str:
    if n >= 1000:
        return f"{n / 1000:.1f}k".replace(".0k", "k")
    return str(n)


def fetch(owner: str, repo: str) -> dict | None:
    req = urllib.request.Request(
        f"{API}{owner}/{repo}",
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "awesome-awesome-security-refresh",
            **(
                {"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"}
                if os.environ.get("GITHUB_TOKEN")
                else {}
            ),
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as e:
        if e.code == 403 and "rate limit" in e.read().decode("utf-8", "replace").lower():
            sys.exit("error: GitHub rate limit hit. Set GITHUB_TOKEN and retry.")
        print(f"  !! {owner}/{repo}: HTTP {e.code}", file=sys.stderr)
    except (urllib.error.URLError, TimeoutError) as e:
        print(f"  !! {owner}/{repo}: {e}", file=sys.stderr)
    return None


def annotate(data: dict) -> str:
    pushed = datetime.strptime(data["pushed_at"], "%Y-%m-%dT%H:%M:%SZ").replace(
        tzinfo=timezone.utc
    )
    parts = [f"★{stars(data['stargazers_count'])}", pushed.strftime("%Y-%m")]
    if data.get("archived"):
        parts.append("⚠️ archived")
    elif (datetime.now(timezone.utc) - pushed).days > DORMANT_DAYS:
        parts.append("💤 dormant")
    return " — " + " · ".join(parts)


def sort_sections(lines: list[str], ranks: dict[int, int]) -> list[str]:
    """Sort each contiguous run of entry lines by star count, descending.

    Entries whose lookup failed keep no rank; they sort last so a transient network error
    can't silently promote them to the top of a section.
    """
    out = list(lines)
    run: list[int] = []

    def flush() -> None:
        if len(run) > 1:
            ordered = sorted(run, key=lambda i: -ranks.get(i, -1))
            for slot, src in zip(run, ordered):
                out[slot] = lines[src]
        run.clear()

    for i, line in enumerate(lines):
        if ENTRY.match(line):
            run.append(i)
        else:
            flush()
    flush()
    return out


def main() -> int:
    lines = README.read_text(encoding="utf-8").split("\n")
    ranks: dict[int, int] = {}
    moved: list[tuple[str, str]] = []
    missing: list[str] = []
    updated = 0

    for i, line in enumerate(lines):
        m = ENTRY.match(line)
        if not m:
            continue
        owner, repo = m.group(1), m.group(2)
        data = fetch(owner, repo)
        if data is None:
            missing.append(f"{owner}/{repo}")
            continue

        # The API follows renames/transfers; surface them so links can be corrected.
        canonical = data["full_name"]
        if canonical.lower() != f"{owner}/{repo}".lower():
            moved.append((f"{owner}/{repo}", canonical))

        lines[i] = TAIL.sub("", line).rstrip() + annotate(data)
        ranks[i] = data["stargazers_count"]
        updated += 1
        print(f"  {canonical}")

    lines = sort_sections(lines, ranks)
    README.write_text("\n".join(lines), encoding="utf-8")

    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    text = README.read_text(encoding="utf-8")
    README.write_text(
        re.sub(
            r"Metadata last refreshed \*\*[\d-]+\*\*",
            f"Metadata last refreshed **{stamp}**",
            text,
        ),
        encoding="utf-8",
    )

    print(f"\nrefreshed {updated} entries")
    if moved:
        print("\nrenamed or transferred — update the links:")
        for old, new in moved:
            print(f"  {old} -> {new}")
    if missing:
        print("\nunreachable (deleted, private, or network error):")
        for name in missing:
            print(f"  {name}")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
