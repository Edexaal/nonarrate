from typing import override
from lib.custom_types import MultiLineType
from .prev_info import PrevInfo
from .multi_line_info import MultiLineInfo


class PrevMultiInfo(PrevInfo):
    """Holds multiple previous line information of a file.

    Attributes:
        is_narr: determines if recent previous line is narration
    """

    def __init__(self):
        super().__init__()
        self.is_narr = False
        self._multi_info = MultiLineInfo()

    @property
    def is_choice_menu(self) -> bool:
        return self._multi_info.is_choice_menu

    @is_choice_menu.setter
    def is_choice_menu(self, value: bool):
        self._multi_info.is_choice_menu = value

    @property
    def multi_type(self) -> MultiLineType:
        return self._multi_info.multi_type

    @multi_type.setter
    def multi_type(self, value: MultiLineType):
        self._multi_info.multi_type = value

    def append_line(self, line: str):
        """Add line to a collection of previous lines.

        Args:
            line: a line from a file.
        """
        self._multi_info.append(line)

    def clear_list(self):
        """Remove all previous lines stored in a collection."""
        self._multi_info.clear()

    def is_empty_list(self) -> bool:
        """Check if collection of stored previous lines is empty."""
        return self._multi_info.is_empty()

    def get_lines(self) -> list[str]:
        return self._multi_info._lines

    @override
    def reset(self):
        super().reset()
        self.is_narr = False
        self.clear_list()
