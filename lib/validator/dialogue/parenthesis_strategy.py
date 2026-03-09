import re
from ..ivalidator_chain import IValidatorChain


class ParenthesisStrategy(IValidatorChain):
    """Validator that checks if dialogue line is surrounded by a parenthesis pair.

    Dialogue surrounded by a `()` pair are known to indicate the speaker is thinking.

    Example:
        mc "(It's got to be here somewhere.)"
    """

    def __init__(self, next_validator: "IValidatorChain | None" = None) -> None:
        super().__init__(next_validator)
        self._regexPat = re.compile(r'^[^=]+"\([^()]+\)"$')
