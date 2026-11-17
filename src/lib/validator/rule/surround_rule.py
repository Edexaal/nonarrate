from .rule import Rule
from . import common_patterns as common


class SurroundRule(Rule):
    """Holds generic validator filter rule for surrounding an entire dialogue with a single open/close symbol."""

    def __init__(self, open_symbol: str, close_symbol: str):
        super().__init__(
            rf"{common.DIALOGUE_START}{open_symbol}[^{open_symbol}]+{close_symbol}{common.CLOSING_CLAUSES}$"
        )
