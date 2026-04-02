import abc
from ..ivalidator_chain_solo import IValidatorChainSolo
from ..ivalidator_chain import IValidatorChain


class ExpressionCueStrategy(IValidatorChainSolo,abc.ABC):
    """Filter for removing lines that is only expression cue(s)."""

    def __init__(self, next_validator: "IValidatorChain | None" = None) -> None:
        super().__init__(next_validator)