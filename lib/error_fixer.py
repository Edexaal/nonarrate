from typing import final
import re
import pathlib
import os

from lib.custom_types import FileInfo, RenpyError
from lib.file.deleter import Deleter
from lib.file.reader import Reader
from lib.file.writer import Writer
from lib.narrator_handler import NarratorHandler


@final
class ErrorFixer:
    """Handles fixing common errors caused by nonarrate.

    Errors are most likely to occur when using nonarrate. ErrorFixer
    attempts to fix these errors cause by the tool.
    """

    _dest_pat: re.Pattern = re.compile(r"(?:and )?File\s+.+(game/.+\.rpy)")
    _line_num_pat: re.Pattern = re.compile(r".+line (\d+):")
    _type_pat: re.Pattern = re.compile(r".+(non-empty|Line is indented|expected statement)")
    _project_dir: str | None = None

    @staticmethod
    def __add_error(errors: dict[str, list[RenpyError]], error: RenpyError):
        if not error.file_loc:
            return
        if error.file_loc not in errors:
            errors[error.file_loc] = [error]
        else:
            errors[error.file_loc].append(error)

    @classmethod
    def __get_error(cls, line: str) -> RenpyError:
        file_url = cls._dest_pat.match(line).group(1) if cls._dest_pat.match(line) else None
        line_num = int(cls._line_num_pat.match(line).group(1)) if cls._line_num_pat.match(line) else None
        category = cls._type_pat.match(line).group(1) if cls._type_pat.match(line) else None
        if not category and line.startswith("and File"):
            category = "duplicate"
        return RenpyError(file_url, line_num, category)

    @classmethod
    def get_errors(cls, errors_txt: pathlib.Path, reader: Reader) -> dict[str, list[RenpyError]]:
        """Parse the errors from Ren'Py's errors.txt file.

        This method needs to be used first as it initializes important properties
        and retrieves all error information needed to operate on.

        Args:
            errors_txt: a path to Ren'Py's errors.txt file.
            reader: class for reading file information.

        Returns:
            a list of Ren'Py errors acquired from errors.txt file.
        """

        cls._project_dir = os.path.dirname(errors_txt)
        file_info = reader.read_lines(errors_txt)
        errors = {}
        for line in file_info.lines:
            strip_line = line.strip()
            if not strip_line.startswith("File") and not strip_line.startswith("and File"):
                continue
            error = cls.__get_error(line)
            cls.__add_error(errors, error)
        return errors

    def __dedent_lines(self, file_info: FileInfo, start_index: int) -> list[str]:
        """Correct indentation by decreasing indent level by 1.

        indentation will be decreased by 1 level (4 spaces) until a line with the
        same indentation level as the first indented dedented line is reached.

        Args:
            file_info: represents file information.
            start_index: the index of the line with the starting indentation problem specified by errors.txt

        Returns:
            a list including dedented lines.
        """
        min_indent = None
        for i, line in enumerate(file_info.lines[start_index:], start_index):
            if min_indent is None:
                file_info.lines[i] = line[4:]
                min_indent = NarratorHandler.get_indent_num(file_info.lines[i])
            elif NarratorHandler.get_indent_num(line) > min_indent:
                file_info.lines[i] = line[4:]
            else:
                return file_info.lines
        return file_info.lines

    def fix(self, errors: list[RenpyError], reader: Reader, writer: Writer, deleter: Deleter):
        """Attempts to fix an error generated from 'errors.txt'.

        Args:
            error: error information
            reader: class for extracting content from a file.
        """
        if not self._project_dir:
            return
        temp_err_loc = errors[0].file_loc if errors[0].file_loc else ""
        current_file_loc = os.path.join(self._project_dir, temp_err_loc)
        file_info = reader.read_lines(current_file_loc)
        errors.reverse()
        for error in errors:
            if error.category:
                if "non-empty" in error.category or "expected statement" in error.category:
                    if error.line_num:
                        file_info.lines.pop(error.line_num - 1)
                elif "Line is indented" in error.category:
                    if error.line_num:
                        file_info.lines = self.__dedent_lines(file_info, error.line_num - 1)
                elif "duplicate" in error.category:
                    deleter.delete(current_file_loc)
            writer.write_lines(file_info)
