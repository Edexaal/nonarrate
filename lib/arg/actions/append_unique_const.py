from .unique_const import UniqueConst


class AppendUniqueConst(UniqueConst):

    def __call__(self, parser, namespace, values, option_string=None):
        super().__call__(parser,namespace,values,option_string)
        if self._shared_list is None:
            self._shared_list = set()
        self._shared_list.add(self.const)
        setattr(namespace,self.dest,self._shared_list)