from typing import final

from .object_rule import ObjectRule

@final
class BasicObjectRule(ObjectRule):
    """Holds rules involving default narrators found in character object."""

    def __init__(self):
        narrators = ["[Tt]hinking", "[Tt]houghts?", "[Nn]arrator", "[Mm]ind", "[Ii]nner [Vv]oice", "[Ii]nner [Mm]onologue"]
        narrator_names = "|".join(narrators)
        super().__init__(narrator_names)

