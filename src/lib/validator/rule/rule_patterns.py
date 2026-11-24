from . import common_patterns as common
from .dialogue_rule import DialogueRule
from .cue_parenthesis_rule import CueParenthesisRule
from .basic_parenthetical_rule import BasicParentheticalRule
from .parenthetical_rule import ParentheticalRule
from .builtin_rule import BuiltinRule
from .rule import Rule
from .cue_rule import CueRule
from .basic_char_rule import BasicCharRule
from .basic_object_rule import BasicObjectRule
from .quote_cue_rule import QuoteCueRule
from .quote_text_tag_rule import QuoteTextTagRule
from .surround_rule import SurroundRule
from .var_object_rule import VarObjectRule
from .object_rule import ObjectRule
from .char_rule import CharRule
from .text_tag_rule import TextTagRule
from .quote_surround_rule import QuoteSurroundRule
from .var_rule import VarRule
from enum import Enum


class DialogueRules(Enum):
    # "Hey! I'm actually a narrator."
    # centered "Hey! I'm actually a narrator."
    BASIC = Rule(
        r'^(?:centered\s)?(["\'])(?![^"\']*\.(?:png|jpe?g|webp|avif|bmp|gif)\1$)(?:(?!\1|\\).|\\.)+(?:\1\s*(?:with|id) .+|\1\s*\([^)]+)?[^:]$'
    )
    # mc "{i}Maybe there's food left over.{/i}"
    # mc "{tag}{i}Maybe there's food left over.{/i}{/tag}"
    # mc "{i}Maybe there's food{i} left over.{/i}"
    ITALIC = DialogueRule(rf"\{{i\}}(?:((?:(?!\{{/?i\}}).)+)(?:\{{/?i\}})?|.+?\{{/?i\}}){common.CLOSING_CLAUSES}$")
    # mc "............."
    # mc "{tag}........................{/tag}"
    # mc "!!!"
    # mc "????"
    ONLY_PUNCTUATION = DialogueRule(rf"[.?!]+{common.CLOSING_CLAUSES}$")
    # mc "(It's got to be here somewhere.)"
    # mc "{tag}(It's got to be here somewhere.){/tag}"
    PARENTHESIS = DialogueRule(rf'(?:\\|\\[\'"])?\([^()]+(?:\\?\)(?:\\[\'"])?)?{common.CLOSING_CLAUSES}$')
    # mc "(Whispers) At least I'm safe inside my mind."
    PARENTHETICAL = ParentheticalRule
    # mc "(Thoughts) I am thinking right now."
    PARENTHETICAL_BASIC = BasicParentheticalRule()
    # mc "~yawns~"
    # mc "{tag}~yawns~{/tag}"
    EXPRESSION_CUE_TILDA = CueRule("~")
    # mc *smiles*
    # mc "{tag}*smiles*{/tag}"
    EXPRESSION_CUE_ASTERISK = CueRule(r"\*")
    # mc "«I am currently thinking right now!»"
    GUILLEMET_DOUBLE = SurroundRule("«", "»")
    # mc "‹I am currently thinking right now!›"
    GUILLEMET_SINGLE = SurroundRule("‹", "›")
    # elnor "{fzs}This is a small bold font tag.{/fzs}"
    # gabby "{ba=100}Big bold asterisk text!{/ba}"
    TEXT_TAG = TextTagRule
    # cap "*gasp* (Maybe this is a bad idea after all...)"
    # cap "{fzs}*gasp* (Maybe this is a bad idea after all...){/fzs}"
    CUE_ASTERISK_PARENTHESIS = CueParenthesisRule(r"\*")
    CUE_TILDA_PARENTHESIS = CueParenthesisRule("~")


# NOTE: DynamicCharacter() is an outdated variant of Character()
# REF: https://www.renpy.org/wiki/renpy/doc/reference/functions/DynamicCharacter
class SpeakerRules(Enum):
    CHARACTER = CharRule
    # "My Thoughts" "Hey there!"
    CHARACTER_BASIC = BasicCharRule()
    # " " "Hey there!"
    CHARACTER_NONE = Rule(r'([\'"])\s*\1\s*([\'"])[^\2]+\2?')
    OBJECT = ObjectRule
    # Character("My Thoughts")
    OBJECT_BASIC = BasicObjectRule()
    OBJECT_ITALIC = [
        Rule(r"what_italic\s*=\s*True"),
        Rule(r"what_prefix\s*=\s*([\"'])\{i}\1"),
        Rule(rf"{common.CHARACTER}\s*(['\"])\s*\{{i\}}[^\"']+\{{/?i\}}\s*\1"),
    ]
    # Character(None)
    OBJECT_NONE = [
        Rule(rf"{common.CHARACTER}\s*(?:name\s*=\s*)?None.*\)"),
        Rule(rf"{common.CHARACTER}\s*name\s*=\s*([\"'])\s*\1[^)]*\)"),
        Rule(rf"{common.CHARACTER}\s*\)"),
        Rule(rf"{common.CHARACTER}\s*[\"']\s*[\"']\s*(?:,.*)?\)"),
        Rule(rf"{common.CHARACTER}(?!\s*[\"']{{2}}|\s*name\s?=|\s*None)(?:\s*[\w_]+\s*=\s*.+)+\)"),
        # Filters empty translation function, '_()' and '_("")'
        # Ref: https://www.renpy.org/doc/html/translation.html#menu-and-string-translations
        Rule(rf"{common.CHARACTER}\s*_\(\s*(?:[\"']\s*[\"']\s*)?\)"),
    ]
    # define narrator_variable = Character(...)
    # default narrator_variable = Character(...)
    # define narrator_variable = "narrator"
    # default narrator_variable = "narrator"
    OBJECT_VAR = VarObjectRule
    # $ narrator_variable = Character(...)
    # $ narrator_variable = "narrator"
    VAR = VarRule
    # NVL Mode narrator: define/default v = nvl_narrator
    # Ref: https://www.renpy.org/doc/html/nvl_mode.html#getting-started
    NVL_BASIC = Rule(r" = nvl_narrator\s*$")


class BuiltInSpeakerRules(Enum):
    # nvl_narrator "Hey there im an nvl narrator"
    NVL = BuiltinRule("nvl_narrator")
    # narrator "Hey there im a narrator"
    NARRATOR = BuiltinRule("narrator")


class QuoteRules(Enum):
    EXPRESSION_CUE_TILDA = QuoteCueRule("~")
    EXPRESSION_CUE_ASTERISK = QuoteCueRule(r"\*")
    ITALIC = Rule(rf"^{common.OPEN_TEXT_TAG}\{{i\}}((?:(?!\{{/?i\}}).)+)(?:\{{/?i\}})?{common.QUOTE_END}")
    ONLY_PUNCTUATION = Rule(rf"^{common.OPEN_TEXT_TAG}[.?!]+\s*(?:{{/\w+}})*$")
    PARENTHESIS = Rule(rf'^{common.OPEN_TEXT_TAG}(?:\\|\\[\'"])?\([^()]+(?:\\?\)(?:\\[\'"])?)?{common.QUOTE_END}')
    TEXT_TAG = QuoteTextTagRule
    GUILLEMET_DOUBLE = QuoteSurroundRule("«", "»")
    GUILLEMET_SINGLE = QuoteSurroundRule("‹", "›")
