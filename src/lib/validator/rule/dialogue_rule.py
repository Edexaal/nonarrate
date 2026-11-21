from __future__ import annotations
import typing
from .rule import Rule
from .common_patterns import OPEN_TEXT_TAG, SPEAKER


class DialogueRule(Rule):
    """Common regex pattern for handling the speaker portion of a 'say' dialogue.

    Typically, a say expression contains the speaker and dialogue. However, say expressions could
    also include image attributes. Common placement is found between the speaker and dialogue.

    REF: https://www.renpy.org/doc/html/dialogue.html#say-with-image-attributes

    Example:
    mc "This is a dialogue."
    mc smile "This is a dialogue"
    mc -smile "This is a dialogue"
    mc @ concerned "This is a dialogue"
    mc @ -concerned "This is a dialogue"

    Currently does NOT support:
    mc happy @ concerned "This is a dialogue"
    mc @ left sad "This is a dialogue"
    mc @ right -concerned "This is a dialogue"
    """

    def __init__(self, regex: str, ignore_case: bool = True):
        self._regex = regex
        super().__init__(rf'{SPEAKER}([\'"]){OPEN_TEXT_TAG}{regex}', ignore_case)

    def _add_img_attr(self, new_img_attr_pat: str) -> typing.Self:
        self._new_regex(rf'{SPEAKER}{new_img_attr_pat}([\'"]){OPEN_TEXT_TAG}{self._regex}', self._is_ignore_case)
        return self

    def with_img_attr(self, img_attr_pat: str) -> DialogueRule:
        new_image_attr_pat = rf"(?:(?:@\s)?-?(?:{img_attr_pat}))\s"
        return DialogueRule(self._regex)._add_img_attr(new_image_attr_pat)
