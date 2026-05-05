from typing import final


@final
class LineInfo:
    """Holds line information from a file."""

    def __init__(self, line: str | None = None) -> None:
        if line is not None:
            self._strip_line = line.strip()
            self._is_triple_quote = LineInfo.__is_triple_quote(self._strip_line)
            self._is_triple_quote_end = (
                True if self._is_triple_quote else LineInfo.__endswith_triple_quote(self._strip_line)
            )
            self._is_menu = LineInfo.__is_choice_menu(self._strip_line)

    @staticmethod
    def __is_triple_quote(strip_line: str) -> bool:
        return strip_line == '"""' or strip_line == "'''"

    @staticmethod
    def __endswith_triple_quote(strip_line: str) -> bool:
        return strip_line.endswith("'''") or strip_line.endswith('"""')

    @staticmethod
    def __is_choice_menu(strip_line:str) -> bool:
        return strip_line.startswith("menu") and strip_line.endswith(":")

    def setup(self, line: str):
        self._strip_line = line.strip()
        self._is_triple_quote = LineInfo.__is_triple_quote(self._strip_line)
        self._is_triple_quote_end = (
            True if self._is_triple_quote else LineInfo.__endswith_triple_quote(self._strip_line)
        )
        self._is_menu = LineInfo.__is_choice_menu(self._strip_line)

    @property
    def strip_line(self):
        return self._strip_line

    @property
    def is_triple_quote(self):
        return self._is_triple_quote

    @property
    def is_triple_quote_end(self):
        return self._is_triple_quote_end

    @property
    def is_menu(self):
        """Checks if line is a choice menu."""
        return self._is_menu
