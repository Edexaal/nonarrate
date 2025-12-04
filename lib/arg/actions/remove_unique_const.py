from .unique_const import UniqueConst
class RemoveUniqueConst(UniqueConst):
    def __call__(self, parser, namespace, values, option_string=None):
        super().__call__(parser,namespace,values,option_string)
        if self._shared_list is None:
            raise ValueError(f"RemoveConst requires at least 1 dest={self.dest} to have a 'default' list set")
        self._shared_list.remove(option_string)
        setattr(namespace,self.dest,self._shared_list)
