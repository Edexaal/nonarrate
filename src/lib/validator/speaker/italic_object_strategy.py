import re
from .object_strategy import ObjectStrategy
from ..ivalidator_chain import IValidatorChain


class ItalicObjectStrategy(ObjectStrategy):
    """Italic styling saved to a Character object."""

    def __init__(self, next_validator: "IValidatorChain | None" = None) -> None:
        super().__init__(None, next_validator)
        ItalicObjectStrategy._char_item_pats.append(re.compile(r"what_italic\s*=\s*True"))
        ItalicObjectStrategy._char_item_pats.append(re.compile(r"Character\(\s*(['\"])\s*\{i\}[^\"']+\{/?i\}\s*\1"))
