import pathlib
import unittest
from lib.arg.cli_parser import CLIParser
import tests.fixture as fixture

class TestCLIParser(unittest.TestCase):

    def setUp(self):
        self.parser = CLIParser()

    def test_positional(self):
        positional = fixture.get_args(self.parser,'game/')
        self.assertEqual(positional.folder_or_file, pathlib.Path('game/'))

    def test_custom_tag_arg(self):
        args = fixture.get_args(self.parser,'game/ --custom-tag t --ct scan')
        self.assertEqual(args.custom_tag,['t','scan'])
