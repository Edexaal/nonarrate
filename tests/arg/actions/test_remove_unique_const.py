import unittest
from lib.arg.cli_parser import CLIParser
import tests.fixture as fixture


class TestRemoveUniqueConst(unittest.TestCase):
    def setUp(self):
        self.parser = CLIParser()

    def test_action(self):
        option = '--no-basic-narr'
        args = fixture.get_args(self.parser, f'game/ {option}')
        self.assertNotIn(option, args.narr_types)

    def test_multiple(self):
        options = ['--no-basic-narr', '--no-italic-narr']
        args = fixture.get_args(self.parser, f'game/ {options[0]} {options[1]}')
        for i in range(len(options)):
            with self.subTest(name=options[i]):
                self.assertNotIn(options[i], args.narr_types)
        self.assertIn('--no-basic-char-obj',args.narr_types)