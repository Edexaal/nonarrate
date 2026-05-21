from .ivalidator_chain_solo import IValidatorChainSolo
from .ivalidator_chain import IValidatorChain
from typing import final



@final
class NullStrategy(IValidatorChainSolo):
    """An empty strategy for a null object pattern."""

    def __init__(self, next_validator: "IValidatorChain | None" = None) -> None:
        super().__init__(None, next_validator)


