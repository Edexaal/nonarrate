import unittest
from lib.arg.cli_parser import CLIParser
import tests.fixture as fixture
from lib.custom_types import SearchTag


class TestAppendUniqueLower(unittest.TestCase):
    def setUp(self) -> None:
        self._parser = CLIParser()

    def test_action(self):
        files = ["random", "INITIAL", "liONs"]
        args = fixture.get_args(self._parser, ["game/", SearchTag.INVALID_FILES.value, *files])
        self.assertIs(type(args.invalid_files), set)
        self.assertIn("random", args.invalid_files)
        self.assertIn("initial", args.invalid_files)
        self.assertIn("lions", args.invalid_files)
        self.assertNotIn("Random", args.invalid_files)
        self.assertNotIn("INITIAL", args.invalid_files)
        self.assertNotIn("liONs", args.invalid_files)
