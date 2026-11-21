import unittest
from lib.arg.cli_parser import CLIParser
from lib.custom_types import SearchTag
import tests.fixture as fixture


class TestAppendUnique(unittest.TestCase):
    def setUp(self) -> None:
        self._parser = CLIParser()

    def test_action(self):
        args = fixture.get_args(self._parser, ["game/", SearchTag.INVALID_DIRS.value, "backend", "waterfall"])
        self.assertIs(type(args.invalid_dirs), set)
        self.assertIn("backend", args.invalid_dirs)
        self.assertIn("waterfall", args.invalid_dirs)
        self.assertNotEqual(len(args.invalid_dirs), 2)
