"""Report GitHub entries in readme.md that break the maintenance rules.

Tools must not be archived and must have a push in the last 365 days.
Other entries are only checked for being archived, moved or gone.
"""

import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone

TOOL_SECTIONS = {"Fetch and Render", "Navigate", "Cleaning Tools", "Extraction Tools"}
MAX_AGE_DAYS = 365
REPO_LINK = re.compile(r"^- \[([^\]]+)\]\(https://github\.com/([\w.-]+/[\w.-]+?)(?:#readme)?\)")


def parse_entries(path):
    section = None
    entries = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            heading = re.match(r"^#{2,3} (.+)", line)
            if heading:
                section = heading.group(1).strip()
                continue
            match = REPO_LINK.match(line)
            if match and section not in (None, "Contents"):
                entries.append((match.group(1), match.group(2), section))
    return entries


def fetch_repo(full_name, token):
    req = urllib.request.Request(f"https://api.github.com/repos/{full_name}")
    req.add_header("Accept", "application/vnd.github+json")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as err:
        if err.code == 404:
            return None
        raise


def check(entries, token, now):
    problems = []
    for name, full_name, section in entries:
        repo = fetch_repo(full_name, token)
        if repo is None:
            problems.append((name, section, "repository not found"))
            continue
        if repo["full_name"].lower() != full_name.lower():
            problems.append((name, section, f"moved to {repo['full_name']}"))
        if repo["archived"]:
            problems.append((name, section, "archived"))
        if section in TOOL_SECTIONS:
            pushed = datetime.fromisoformat(repo["pushed_at"].replace("Z", "+00:00"))
            age = (now - pushed).days
            if age > MAX_AGE_DAYS:
                problems.append((name, section, f"no push for {age} days"))
    return problems


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "readme.md"
    entries = parse_entries(path)
    problems = check(entries, os.environ.get("GITHUB_TOKEN"), datetime.now(timezone.utc))
    print(f"Checked {len(entries)} GitHub entries.\n")
    if not problems:
        print("No problems found.")
        return 0
    print("| Entry | Section | Problem |")
    print("| --- | --- | --- |")
    for name, section, problem in problems:
        print(f"| {name} | {section} | {problem} |")
    return 1


if __name__ == "__main__":
    sys.exit(main())
