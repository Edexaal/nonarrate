from .rule import Rule
from . import common_patterns as common


class TextTagRule(Rule):
    """Triple quote rule for text tags."""

    def __init__(self, tag_name: str):
        super().__init__(
            rf'{common.SPEAKER}([\'"]){{(?:{tag_name})(?:=[^}}]+)?}}.+(?:{{/?(?:{tag_name})}})?[.?!]?\s*(?:\2|\2\s*(?:with|id) .+|\2\s*\([^)]+\))?'
        )
