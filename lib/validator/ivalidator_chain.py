from abc import ABC
import re


class IValidatorChain(ABC):
    """Provide an abstract interface for processing validation requests through a chain of handlers."""

    def __init__(self, next_validator: "IValidatorChain | None" = None) -> None:
        self._next_validator = next_validator
        self._validate_pat: "re.Pattern | None" = None

    def is_valid(self, line: str) -> bool:
        """Validate the given line and forward it to the next chain of validators if applicable.

        Subclasses implement their own specific validation rule(s). If the line fails, it will
        be passed to the next validator in the chain or return False.

        Args:
            line(str): line of text to validate.

        Returns:
            True if line passes validations set by a validator in the chain; False if all
            validators cannot validate the line.
        """
        if self._validate_pat and self._validate_pat.match(line):
            return True
        elif self._next_validator:
            return self._next_validator.is_valid(line)
        return False

    @property
    def next_validator(self) -> "IValidatorChain | None":
        """Get the next validator after this current one.

        Returns:
            The subsequent validator in the chain.
        """
        return self._next_validator

    @next_validator.setter
    def next_validator(self, next_validator: "IValidatorChain | None"):
        """Set the next validator to use after this current one.

        Args:
            next_validator: The subsequent validator to use if current one fails.
        """
        self._next_validator = next_validator
