import argparse
import pathlib
from typing import Any


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
        self.__add_arg("folder_or_file", metavar='game/ folder OR errors.txt', type=pathlib.Path)
        self.__add_arg("-p", "--pauses", action="store_true")
        self.__add_arg("-v", "--version", action="version", version="%(prog)s "+self.__version_num)
        # TODO: Replace const of narr_types with actual classes
        no_filters: list[str] = ['--no-basic-narr', '--no-basic-char-obj', '--no-italic-narr', '--no-parenthesis-narr']
        self.__add_no_filters(no_filters)
        self.__add_filter_arg('--basic-char', dest='narr_types', action="append_const", const='basic-char')
        self.__add_filter_arg('--custom-tag', '--ct', action='append')
        self.__add_filter_arg('--custom-basic-char', '--cbc', action='append')
        self.__add_filter_arg('--custom-basic-char-obj', '--cbco', action='append')

    def __add_no_filters(self, optnames: list[str]):
        for optname in optnames:
            self.__add_filter_arg(optname, dest='narr_types', action="append_const", const=optname)

    def __add_arg(self, *args, **kwargs: Any):
        self.__parser.add_argument(*args, **kwargs)

    def __add_filter_arg(self, *args, **kwargs: Any):
        self.__filter_group.add_argument(*args, **kwargs)

    def parse_args(self, *args):
        return self.__parser.parse_args(*args)
