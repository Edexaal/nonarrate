import argparse
class UniqueConst(argparse.Action):
    def __init__(self, option_strings, dest, const=None, default=None, type=None, choices=None,
                 required=False, help=None, metavar=None, deprecated=False):
        self._shared_list = None
        if const is None:
            raise ValueError(f'{self.__class__.__name__} requires "const" to have a value!')
        super().__init__(option_strings, dest, 0, const, default, type, choices, required, help, metavar,
                         deprecated)

    def __call__(self, parser, namespace, values, option_string=None):
        self._shared_list = getattr(namespace,self.dest,None)
        if self._shared_list is not None and not isinstance(self._shared_list,set):
            self._shared_list = set(self._shared_list)