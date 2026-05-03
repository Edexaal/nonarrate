import re

from lib.validator.ivalidator_chain_solo import IValidatorChainSolo
from ..ivalidator_chain import IValidatorChain


class CharacterNoneStrategy(IValidatorChainSolo):
    """Validator for validating characters/speakers with empty quotation marks.

    Example:
        "" "Thank you for playing my Ren'Py game!"
    """

    def __init__(self, next_validator: "IValidatorChain | None" = None) -> None:
        super().__init__(next_validator)
        self._validate_pat = re.compile(rf'([\'"])\s*\1\s*([\'"])[^\2]+\2?')