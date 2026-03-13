from ..ivalidator_chain import IValidatorChain
import re


class BasicStrategy(IValidatorChain):
    """Validator that checks if a line is a default narrator.

    The validated line must have dialogue without a speaker being explicitly stated. In Renpy, by default,
    if a dialogue does not have a speaker stated, it will automatically be seen as a narrator speaking.

    Example of a default narrator:
        "Hey! I'm actually a narrator."
    """

    def __init__(self, next_validator: "IValidatorChain | None" = None) -> None:
        super().__init__(next_validator)
        self._validate_pat = re.compile(r'^"[^"]+"$')
