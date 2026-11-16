from .rule import Rule


class CueParenthesisRule(Rule):
    """Holds validator filter rule for expression cue + parenthesis combination."""

    def __init__(self, cue_symbol: str):
        super().__init__(
            rf"^(?:(['\"])(?:(?!\1).)+\1|\w+?)\s?([\"'])(?:{{\w+(?:=[^}}]+)?}})*\s*({cue_symbol}+)[^{cue_symbol}(]+\3\s*\([^)]+(?:\)\s*(?:(?:{{/\w+}})*[.?!]?|[.?!]?(?:{{/\w+}})*)\s*\2(?:\s*(?:with|id) .+|\s*\([^)]+\))?)?$"
        )
