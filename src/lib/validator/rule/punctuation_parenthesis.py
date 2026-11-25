from .dialogue_rule import DialogueRule


class PunctuationParenthesisRule(DialogueRule):
    """Holds validator filter rule for punctuations + parenthesis combination."""

    def __init__(self):
        super().__init__(
            r"[.!?]+\s*\([^)]+(?:\)\s*(?:(?:{/\w+})*[.?!]?|[.?!]?(?:{/\w+})*)\s*\2(?:\s*(?:with|id) .+|\s*\([^)]+\))?)?$"
        )
