import json

from lib.stat import Stat
from lib.custom_types import FileInfo


class Writer:
    """Tools for writing content to files."""

    def write_lines(self, file_info: FileInfo):
        """Write lines to a file.

        Args:
            file_info: Class that holds file information.
        """
        with open(file_info.url, "w", encoding="utf-8") as f:
            f.writelines(file_info.lines)

    def dump_stats(self):
        results = {
            "stats": {
                "removed_lines_total": Stat.total_lines - Stat.total_cleaned_lines,
                "removed_lines_percent": (Stat.total_lines - Stat.total_cleaned_lines) / Stat.total_lines * 100,
                "remaining_lines_percent": (Stat.total_cleaned_lines / Stat.total_lines) * 100,
                "file_urls": Stat.file_urls,
            }
        }
        with open("./stats.json", "w", encoding="utf-8") as f:
            json.dump(results, f)
