# Contributing

Thanks for helping improve this project! Bug reports, ideas, and pull requests are welcome.

## Reporting bugs

Open an issue and include:
- Your Python version (`python --version`) and OS
- The exact command you ran and the error message
- Whether the export was JSON (HTML isn't supported)

**Never attach your real export.** Instagram's JSON layout changes occasionally; if
parsing breaks, share a small anonymized snippet of the structure with fake usernames.

## Pull requests

1. Fork the repo and create a branch: `git checkout -b my-change`
2. Keep the tool dependency-free (standard library only) unless there's a strong reason.
3. Run the tests and the sample data:
   ```
   python -m unittest discover -s tests
   python not_following_back.py sample_data
   ```
4. Update `CHANGELOG.md` and the README if behavior changes.
5. Open a PR describing what and why.

## Ideas welcome

- Support for Instagram's HTML export format
- A Go port
- Ignore-list for accounts you intentionally don't follow back (brands, celebrities)
- Comparing two exports to see who recently unfollowed you

## Out of scope

Features that need your Instagram login, scrape profiles, or automate unfollowing.
These violate Instagram's Terms of Use and risk users' accounts.

## License

By contributing, you agree that your contributions are licensed under the
[Apache License 2.0](LICENSE), as described in section 5 of that license.
