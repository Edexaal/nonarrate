"""Provides common regular expression patterns for rule creation.

This module defines several regular expressions constants that are commonly used
when creating a new rule pattern.
"""

# \1 -> speaker quotation mark
# \2 -> dialogue quotation mark
SPEAKER = r'^(?:([\'"])(?:(?!\1).)+\1|\w+?)\s?'
OPEN_TEXT_TAG = r"(?:{\w+(?:=[^}]+)?})*\s*"
CLOSING_CLAUSES = r"\s*(?:[.?!]?(?:{/\w+})*|(?:{/\w+})*[/?!]?)\s*(?:\2|\2\s*(?:with|id) .+|\2\s*\([^)]+\))?"

CHARACTER = r"(?:Dynamic)?Character\s*\("

QUOTE_END = r"\s*(?:[.?!]?(?:{/\w+})*|(?:{/\w+})*[/?!]?)$"
