import argparse
import pathlib
from typing import Any
from lib.arg.actions import *


class CLIParser:
    def __init__(self):
        self.__version_num = '0.1'
        self.__setup()

    def __setup(self):
        self.__init_parser()
        self.__init_parser_groups()
        self.__configure_opts()

    def __init_parser(self):
        self.__parser = argparse.ArgumentParser(
            prog="nonarrate",
            description="Remove narration & thoughts from Ren'Py visual novel games.")

    def __init_parser_groups(self):
        self.__filter_group = self.__parser.add_argument_group('Filters', 'Types of narration to remove. (choose 1+)')

    def __configure_opts(self):
        self.__add_arg("folder_or_file", metavar='game/ folder OR errors.txt', type=pathlib.Path,
                       help='Removes narration from .rpy files OR fix errors from errors.txt file')
        self.__add_arg("-p", "--pauses", action="store_true",
                       help='Replace removed narration with a pause to see narrated scenes without narration.')
        self.__add_arg("-v", "--version", action="version", version="%(prog)s " + self.__version_num)
        # TODO: Replace const of narr_types with actual classes
        no_filters: dict[str, str] = {'--no-basic-narr': "Do not remove dialogues that don't have a speaker",
                                      '--no-basic-char-obj': 'Do not remove default narrators saved to a Character object',
                                      '--no-italic-narr': 'Do not remove dialogues that are fully italic',
                                      '--no-parenthesis-narr': 'Do not remove dialogue fully wrapped in a parenthesis'}
        self.__add_no_filters(no_filters)
        # TODO: This option should be allowed many uses. Right now its in a set(), so only 1 usage is possible.
        # This should be fixed when 'const' is replaced with class object
        self.__add_filter_arg('--basic-char', dest='narr_types', action=AppendUniqueConst,
                              const='--basic-char', help='Removes default narrators not in a Character object')
        self.__add_filter_arg('--custom-tag', '--ct', metavar='TAG_NAME', action='append', help="Removes dialogue wrapped entirely in a custom text tag. Ex:{t}..{/t}")
        self.__add_filter_arg('--custom-basic-char', '--cbc', metavar='SPEAKER_NAME', action='append', help='Removes a speaker not in a Character object')
        self.__add_filter_arg('--custom-basic-char-obj', '--cbco', metavar='SPEAKER_NAME', action='append', help='Removes a speaker saved to a Character object')

    def __add_no_filters(self, optnames: dict[str, str]):
        has_default = False
        for optname, helpMsg in optnames.items():
            if not has_default:
                self.__add_filter_arg(optname, dest='narr_types', action=RemoveUniqueConst, const=optname,
                                      default=optnames, help=helpMsg)
                has_default = True
            else:
                self.__add_filter_arg(optname, dest='narr_types', action=RemoveUniqueConst, const=optname, help=helpMsg)

    def __add_arg(self, *args, **kwargs: Any):
        self.__parser.add_argument(*args, **kwargs)

    def __add_filter_arg(self, *args, **kwargs: Any):
        self.__filter_group.add_argument(*args, **kwargs)

    def parse_args(self, *args):
        return self.__parser.parse_args(*args)

if __name__ == "__main__":
    parser = CLIParser()
    parser.parse_args()