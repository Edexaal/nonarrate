from .dialogue_rule import DialogueRule


class ParentheticalRule(DialogueRule):
    """Filter for words/phrases found within parentheses at the beginning of a dialogue.

    Some dialogues are written in the form of screenwriting. This is where at the beginning of a dialogue
    a descriptor is enclosed within a parenthesis describing how it should be acted or directed onscreen.

    Example:
    mc "(Mumbles) Maybe if they went shopping yesterday we wouldn't be out of food."
    """

    def __init__(self, custom_phrases: str):
        super().__init__(
            rf"\\?\(\s*(?:{custom_phrases})\s*\\?\)\s*(?:(?!\\?\2).)+(?:\2|\2\s*(?:with|id) .+|\2\s*\([^)]+\))?$",
        )
