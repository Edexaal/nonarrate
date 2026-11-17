from .rule import Rule
from . import common_patterns as common


class QuoteSurroundRule(Rule):
    """Quote rule for dialogue surrounded by open/close symbol."""

    def __init__(self, open_symbol: str, close_symbol: str):
        super().__init__(
            rf"^{common.OPEN_TEXT_TAG}{open_symbol}[^{open_symbol}]+{close_symbol}\s*(?:(?:{{/\w+}})*[.?!]?|[.?!]?(?:{{/\w+}})*)$"
        )
