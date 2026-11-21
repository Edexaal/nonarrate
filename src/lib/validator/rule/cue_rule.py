from .dialogue_rule import DialogueRule


class CueRule(DialogueRule):
    """Holds validator filter rule for expression cue rule."""

    def __init__(self, cue_symbol: str):
        super().__init__(
            rf"({cue_symbol}+)[^{cue_symbol}]+(?:\3\s*(?:(?:{{/\w+}})*[.?!]?|[.?!]?(?:{{/\w+}})*)\s*\2(?:\s*(?:with|id) .+|\s*\([^)]+\))?)?$"
        )
