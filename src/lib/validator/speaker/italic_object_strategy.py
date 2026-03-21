from .object_strategy import ObjectStrategy
from ..ivalidator_chain import IValidatorChain


class ItalicObjectStrategy(ObjectStrategy):
    """Italic styling saved to a Character object."""

    def __init__(self, next_validator: "IValidatorChain | None" = None) -> None:
        super().__init__(r"what_italic\s*=\s*True", next_validator)
