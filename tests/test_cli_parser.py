import pathlib
import unittest
from lib.arg.cli_parser import CLIParser
from argparse import Namespace


class TestCLIParser(unittest.TestCase):
    def get_args(self, arguments: str):
        return self.parser.parse_args(arguments.split())

    def setUp(self):
        self.parser = CLIParser()

    def test_positional(self):
        positional = self.get_args('game/')
        self.assertEqual(positional.folder_or_file, pathlib.Path('game/'))

    def test_custom_tag_arg(self):
        args = self.get_args('game/ --custom-tag t --ct scan')
        self.assertEqual(args.custom_tag,['t','scan'])
