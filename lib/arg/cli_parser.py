import argparse
import pathlib
from typing import Any


class CLIParser:
    def __init__(self):
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
        self.__filter_group = self.__parser.add_argument_group('Filters','Types of narration to remove. (choose 1 or more)')

    def __configure_opts(self):
        self.__add_arg("folder_or_file", metavar='game/ folder OR errors.txt', type=pathlib.Path)
        # TODO: Replace const of narr_types with actual classes
        self.__add_filter_arg('--no-basic-narr',dest='narr_types', action="append_const", const='basic-narr')
        self.__add_filter_arg('--no-basic-char',dest='narr_types', action="append_const", const='basic-char')
        self.__add_filter_arg('--no-italic-narr',dest='narr_types', action="append_const", const='italic-narr')
        self.__add_filter_arg('--no-parenthesis-narr',dest='narr_types', action="append_const", const='parenthesis-narr')
        self.__add_filter_arg('--custom-tag','--ct', action='append')


    def __add_arg(self, *args, **kwargs:Any):
        self.__parser.add_argument(*args, **kwargs)

    def __add_filter_arg(self, *args, **kwargs:Any):
        self.__filter_group.add_argument(*args, **kwargs)


    def parse_args(self,*args):
        return self.__parser.parse_args(*args)