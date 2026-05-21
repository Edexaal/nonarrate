from .char_rule import CharRule
from typing import final

@final
class BasicCharRule(CharRule):
    """Holds validator rule for basic character strategy filter."""

    def __init__(self):
        narrators = ["thinking", "thoughts?", "narrator", "mind", "inner voice", "inner monologue"]
        narrator_names = "|".join(narrators)
        super().__init__(narrator_names)
