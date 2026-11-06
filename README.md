# Insta Unfollow Checker

Find out who you follow on Instagram that doesn't follow you back, using your own official data export. No login, no scraping, no ban risk.

![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue)
![License: Apache 2.0](https://img.shields.io/badge/license-Apache%202.0-blue)
![Dependencies: none](https://img.shields.io/badge/dependencies-none-brightgreen)

## Why an export instead of scraping?

Instagram doesn't show follower lists for public profiles to logged-out visitors, and tools that log in with your password or automate the app often get accounts flagged or banned. Instagram's built-in data export gives you the same lists, officially and safely. See [PRIVACY.md](PRIVACY.md).

## Features

- Lists accounts that **don't follow you back**
- Lists accounts that **follow you, but you don't follow back**
- Handles multi-file exports (`followers_1.json`, `followers_2.json`, ...)
- Optional CSV output
- Pure Python standard library, nothing to install
- Runs fully offline

## Requirements

Python 3.8 or newer.

## Get your data from Instagram

1. Open Instagram and go to **Settings → Accounts Center → Your information and permissions → Download your information**.
2. Choose **Download or transfer information**, select your profile, then **Some of your information**.
3. Tick **Followers and following**.
4. Choose **Download to device**, set the format to **JSON**, and submit.
5. Instagram emails you when it's ready (minutes to a day). Download and **unzip** it.

> Menu names change from time to time. If something looks different, search Instagram's Help Center for "download your information".

## Usage

```bash
python not_following_back.py path/to/unzipped_export
```

Save results to CSV:

```bash
python not_following_back.py path/to/unzipped_export --csv results.csv
```

The script searches the folder (including subfolders) for `followers*.json` and `following*.json`.

### Try it with sample data

```bash
python not_following_back.py sample_data
```

Output:

```
Followers: 3 | Following: 3

Not following you back (2):
  https://instagram.com/dave
  https://instagram.com/erin

You don't follow back (2):
  https://instagram.com/bob
  https://instagram.com/carol
```

## Troubleshooting

| Problem | Fix |
|---|---|
| `No followers*.json found` | You probably exported as HTML. Re-export as **JSON**. |
| `No following*.json found` | Make sure "Followers and following" was ticked. |
| Counts look too low | Pass the top-level unzipped folder so every `followers_N.json` part is found. |
| `KeyError` or odd results | Instagram may have changed the layout. Open an issue with an anonymized snippet. |

## Limitations

- Only reads your export, so results are as fresh as the export you downloaded.
- JSON only. HTML exports aren't supported yet.
- Usernames are compared case-insensitively.

## Project files

| File | Purpose |
|---|---|
| `not_following_back.py` | The program |
| `sample_data/` | Fake data for testing |
| `tests/` | Unit tests (`python -m unittest discover -s tests`) |
| `.github/` | Issue templates, PR template, CI workflow |
| `PRIVACY.md` | What the tool does and doesn't touch |
| `CONTRIBUTING.md` | How to report bugs and contribute |
| `CHANGELOG.md` | Version history |
| `LICENSE` | Apache License 2.0 |
| `NOTICE` | Attribution notice |

## Disclaimer

This project isn't affiliated with or endorsed by Instagram or Meta. Use it only on your own account's data.

## License

Licensed under the [Apache License 2.0](LICENSE).

Copyright 2026 [Amal Benny](https://amalbenny.github.io).

## Acknowledgments
* Thanks to [Cheap Pro SMM Panel -The Cheapest Instagram SMM Service](https://cheapprosmmpanel.com/instagram-smm-services) for inspiration and core utilities.