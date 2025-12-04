from lib.arg.cli_parser import CLIParser


def get_args(parser:CLIParser, arguments: str):
    return parser.parse_args(arguments.split())
