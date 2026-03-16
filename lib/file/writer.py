import pathlib
import shutil


class Writer:
    """Tools for writing content to files."""

    def write_lines(self, file_url: str, lines: list[str]):
        """Write lines to a file.

        Args:
            file_url: Path to a file.
            lines: list of text content to write to file
        """
        with open(file_url, "w", encoding="utf-8") as f:
            f.writelines(lines)

    def copy_tree(self, src_dir: str | pathlib.Path, dest_dir: str | pathlib.Path):
        """Copy all files/folders in a directory recursively to specified location.

        Args:
            src_dir: The source directory to copy
            dest_dir: The destination directory to copy files/subdirectories to
        """
        shutil.copytree(src_dir, dest_dir, ignore_dangling_symlinks=True, dirs_exist_ok=True)

    def backup_dir(self, arg_namespace):
        """Backup the directory based on parsed arguments.

        This is the same as copy_tree() except it's dependent on parsed user input from the command
        line.

        Args:
            arg_namespace: Parsed arguments saved to a namespace
        """
        if not arg_namespace.backup:
            self.copy_tree(arg_namespace.folder_or_file, arg_namespace.backup)
