from lib.arg import CLIParser, ArgChecker, WrongFileError
import tests.fixture as fixture
import unittest


class TestArgChecker(unittest.TestCase):
    """The tests here rely on real files and folders"""

    def setUp(self):
        self.parser = CLIParser()
        self.path = fixture.get_dummy_path(self.parser)

    def test_folder_or_file_not_exists(self):
        for command in ["tests/jrajj/", f"{self.path}/file.txt"]:
            with self.subTest(name=command):
                with self.assertRaises(FileNotFoundError):
                    fixture.check_args(self.parser,command)

    def test_valid_file(self):
        self.assertIsNone(fixture.check_args(self.parser,f"{self.path}/errors.txt"))

    def test_invalid_file(self):
        """Tests against an actual file in dummy folder called real.txt"""
        with self.assertRaises(WrongFileError):
            fixture.check_args(self.parser,f"{self.path}/real.txt")
