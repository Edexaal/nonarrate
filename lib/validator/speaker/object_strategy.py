import re
from lib.custom_types import FileInfo
from ..ivalidator_chain import IValidatorChain


class ObjectStrategy(IValidatorChain):
    """Base validator for validating speakers/characters stored in a Character() object.

    This validator will need to first look through all files where the Character object is initially defined
    to work properly.

    """

    def __init__(
        self,
        speakers: list[str],
        next_validator: "IValidatorChain | None" = None,
    ) -> None:
        super().__init__(next_validator)
        self._speakers = speakers
        self._regexPat = re.compile(r"^(?:define|default)\s+(\w+)")

    # TODO: Create function to retrieve character object(s) for speaker(s)
    def define_speakers(self, file_infos: list[FileInfo]):
        self._speaker_objects = []
