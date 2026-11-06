#!/usr/bin/env python3
# Copyright 2026 Amal Benny (https://amalbenny.github.io)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Find who you follow that doesn't follow you back, using Instagram's
official data export (no login, no scraping, no ban risk).

How to get the data:
  Instagram > Settings > Accounts Center > Your information and permissions
  > Download your information > Select "Followers and following"
  > Format: JSON > Create export. Unzip it when it arrives.

Usage:
  python not_following_back.py path/to/export_folder
  python not_following_back.py path/to/export_folder --csv out.csv
"""
import argparse
import csv
import json
import sys
from pathlib import Path


def usernames_from(obj):
    """Extract usernames from either export layout (followers or following)."""
    if isinstance(obj, dict):
        # following.json wraps the list in "relationships_following"
        for value in obj.values():
            if isinstance(value, list):
                obj = value
                break
    names = set()
    for item in obj:
        data = item.get("string_list_data", [])
        # followers: username in string_list_data[0].value
        # following: username in item["title"]
        name = item.get("title") or (data[0].get("value") if data else None)
        if name:
            names.add(name.strip().lower())
    return names


def load(folder: Path, prefix: str):
    files = sorted(folder.rglob(f"{prefix}*.json"))
    if not files:
        sys.exit(f"No {prefix}*.json found in {folder}. Export as JSON, not HTML.")
    names = set()
    for f in files:
        with open(f, encoding="utf-8") as fh:
            names |= usernames_from(json.load(fh))
    return names


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder", type=Path, help="Unzipped Instagram export folder")
    ap.add_argument("--csv", type=Path, help="Optional CSV output path")
    args = ap.parse_args()

    followers = load(args.folder, "followers")
    following = load(args.folder, "following")

    not_back = sorted(following - followers)
    fans = sorted(followers - following)  # they follow you, you don't follow them

    print(f"Followers: {len(followers)} | Following: {len(following)}")
    print(f"\nNot following you back ({len(not_back)}):")
    for u in not_back:
        print(f"  https://instagram.com/{u}")
    print(f"\nYou don't follow back ({len(fans)}):")
    for u in fans:
        print(f"  https://instagram.com/{u}")

    if args.csv:
        with open(args.csv, "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(["username", "status"])
            w.writerows((u, "not_following_back") for u in not_back)
            w.writerows((u, "you_dont_follow_back") for u in fans)
        print(f"\nSaved to {args.csv}")


if __name__ == "__main__":
    main()
