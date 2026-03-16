import shutil
from lib.arg.cli_parser import CLIParser
import tests.fixture as fixture
import unittest
from lib.file import Writer


class TestWriter(unittest.TestCase):
    def setUp(self) -> None:
        self._parser = CLIParser()

    def tearDown(self) -> None:
        if self.backup_folder and self.backup_folder.exists():
            shutil.rmtree(self.backup_folder, ignore_errors=True)

    def count_files(self, dir_path):
        total = 0
        for _ in dir_path.iterdir():
            total += 1
        return total

    def test_backup(self):
        backup_loc = f"{fixture.DUMMY_PATH}/_BACKUP"
        arg_namespace = fixture.get_args(self._parser, [fixture.DUMMY_PATH, "--backup", backup_loc])
        writer = Writer()
        correct_total = self.count_files(arg_namespace.folder_or_file)
        writer.backup_dir(arg_namespace)
        self.assertTrue(arg_namespace.backup.exists(), f"Backup folder doesn't exist at {backup_loc}")
        self.backup_folder = arg_namespace.backup
        backup_total = self.count_files(arg_namespace.backup)
        self.assertEqual(
            backup_total,
            correct_total,
            "The contents of backup folder does not equal the total number of items in folder",
        )
