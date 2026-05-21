from lib.arg.cli_parser import CLIParser
from lib.validator.rule import Rule
from lib.validator import ObjectStrategy, IValidatorChain,IValidatorChainSolo
from lib.arg import ArgChecker

DUMMY_PATH = "tests/dummy"  # Path to dummy file directory
ALT_DUMMY_PATH = "dummy"


def get_args(parser: CLIParser, arguments: str | list):
    if isinstance(arguments, str):
        return parser.parse_args(arguments.split())
    return parser.parse_args(arguments)


def get_dialogue_list(valid_indexes: list[int], dialogues: dict[int, str]):
    valid_lines = []
    invalid_lines = []
    for i, line in dialogues.items():
        if i in valid_indexes:
            valid_lines.append(line)
        else:
            invalid_lines.append(line)
    return valid_lines, invalid_lines

def validate_solo(rule: Rule) -> IValidatorChainSolo:
    return IValidatorChainSolo(rule)

def validate_obj(rule: Rule, chain: IValidatorChain = None) -> ObjectStrategy:
    return ObjectStrategy(rule,chain)

def check_args(parser: CLIParser,command: str):
    args = get_args(parser, command)
    ArgChecker.check_args(args)

def get_dummy_path(parser: CLIParser) -> str:
    """Also checks if dummy path actually exists."""
    path = DUMMY_PATH
    try:
        check_args(parser,f"{path}/")
    except Exception:
        path = ALT_DUMMY_PATH
        check_args(parser,f"{path}/")
    return path
