from .rule import Rule
from . import common_patterns as common


class ObjectRule(Rule):
    """Holds rules for custom speaker names in Character object."""

    def __init__(self, char_object_item: str):
        super().__init__(rf"{common.CHARACTER}[^)]*(?:{char_object_item})[^)]*\)")
