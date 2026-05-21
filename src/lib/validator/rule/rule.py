import re

class Rule:
    """Holds validator filter rules in regular expression format."""

    def __init__(self, regex:str, is_ignore_case: bool = False):
        if not is_ignore_case:
            self._pattern = re.compile(regex)
        else:
            self._pattern = re.compile(regex,re.IGNORECASE)

    @property
    def pattern(self) -> re.Pattern:
        return self._pattern