from .rule import Rule
from . import common_patterns as common


class QuoteCueRule(Rule):
    """Quote rule for expression cues."""

    def __init__(self, cue_symbol: str):
        super().__init__(
            rf"^{common.OPEN_TEXT_TAG}({cue_symbol}+)[^{cue_symbol}]+\1?\s*(?:(?:{{/\w+}})*[.?!]?|[.?!]?(?:{{/\w+}})*)$"
        )
