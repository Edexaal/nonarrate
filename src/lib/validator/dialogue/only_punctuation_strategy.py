import re
from ..ivalidator_chain_solo import IValidatorChainSolo


class OnlyPunctuationStrategy(IValidatorChainSolo):
    """Validator that checks if dialogue only consists of punctuation marks.

    Example:
        mc "............."
        mc "{tag}........................{/tag}"
        mc "!!!"
        mc "????"
    """

    def __init__(self, next_validator: "IValidatorChainSolo | None" = None) -> None:
        super().__init__(next_validator)
        self._validate_pat = re.compile(r'^[^=]+([\'"])(?:{\w+(?:=[^}]+)?})*[.?!]+(?:{/\w+})*\s*(?:\1|\1\s*with .+)?$')
