import re
from ..ivalidator_chain import IValidatorChain


class BasicCharacterStrategy(IValidatorChain):
    """Validator that validates a character/speaker is a basic narrator.

    The speaker must be surrounded by quotes, followed by their dialogue.

    Example:
        "Narrator" "The man grabs his bag and flashes his I.D."
    """

    def __init__(self, next_validator: "IValidatorChain | None" = None) -> None:
        super().__init__(next_validator)
        narrators = ["thinking", "thought", "narrator"]
        self._regexPat = re.compile(
            rf'".*(?:{"|".join(narrators)}).*"\s*"[^"]+"', re.IGNORECASE
        )
