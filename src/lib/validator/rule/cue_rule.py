from .rule import Rule
from . import common_patterns as common


class CueRule(Rule):
    """Holds validator filter rule for expression cue rule."""

    def __init__(self, cue_symbol: str):
        super().__init__(
            rf"{common.DIALOGUE_START}({cue_symbol}+)[^{cue_symbol}]+(?:\3\s*(?:(?:{{/\w+}})*[.?!]?|[.?!]?(?:{{/\w+}})*)\s*\2(?:\s*(?:with|id) .+|\s*\([^)]+\))?)?$"
        )
