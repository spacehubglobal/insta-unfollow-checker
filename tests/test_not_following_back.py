import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import not_following_back as nfb  # noqa: E402

SAMPLE = Path(__file__).resolve().parent.parent / "sample_data"


class ParsingTests(unittest.TestCase):
    def test_followers_layout(self):
        data = [{"title": "", "string_list_data": [{"value": "Alice"}]}]
        self.assertEqual(nfb.usernames_from(data), {"alice"})

    def test_following_layout(self):
        data = {"relationships_following": [
            {"title": "Dave", "string_list_data": [{"href": "x"}]}]}
        self.assertEqual(nfb.usernames_from(data), {"dave"})

    def test_empty_entries_ignored(self):
        self.assertEqual(nfb.usernames_from([{"string_list_data": []}]), set())


class LoadTests(unittest.TestCase):
    def test_sample_data(self):
        followers = nfb.load(SAMPLE, "followers")
        following = nfb.load(SAMPLE, "following")
        self.assertEqual(sorted(following - followers), ["dave", "erin"])
        self.assertEqual(sorted(followers - following), ["bob", "carol"])

    def test_multiple_follower_files_merged(self):
        with tempfile.TemporaryDirectory() as tmp:
            for i, name in enumerate(["a", "b"], 1):
                (Path(tmp) / f"followers_{i}.json").write_text(json.dumps(
                    [{"string_list_data": [{"value": name}]}]))
            self.assertEqual(nfb.load(Path(tmp), "followers"), {"a", "b"})

    def test_missing_files_exit(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(SystemExit):
                nfb.load(Path(tmp), "followers")


if __name__ == "__main__":
    unittest.main()
