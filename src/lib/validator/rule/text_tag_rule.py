from .rule import Rule

class TextTagRule(Rule):
    """Triple quote rule for text tags."""

    def __init__(self, tag_name: str):
        super().__init__(rf'[^=]+([\'"]){{(?:{tag_name})(?:=[^}}]+)?}}.+(?:{{/?(?:{tag_name})}})?[.?!]?\s*(?:\1|\1\s*with .+)?')


