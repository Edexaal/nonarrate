import re
from .object_strategy import ObjectStrategy
from ..ivalidator_chain import IValidatorChain


class ObjectNoneItemStrategy(ObjectStrategy):
    """Validator that validates a Character(None) object.

    Speakers saved with, Character(None), are narrators as only the dialogue of the speaker will
    be present.
    """

    def __init__(
        self,
        next_validator: "IValidatorChain | None" = None,
    ) -> None:
        super().__init__(None, next_validator)
        self._char_item_pat = re.compile(r"Character\((?:name\s?=\s?)?None\)")
