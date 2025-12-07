"""Provides an AppendUniqueConst class for appending constant values.

This module includes an argparse Action class, AppendUniqueConst, for adding a unique constant
value to a set collection.
"""
from .unique_const import UniqueConst

class AppendUniqueConst(UniqueConst):
    """Represents an argparse Action for appending unique constant values.

    This class provides an argument parsing Action for adding new and unique constant values
    to a collection. Similar to how the argument parsing action 'append_const' works.
    """

    def _modify_set(self, option_string: str):
        """Appends a constant value to a set of constant values.

        Args:
            option_string: the name of the argument used to call this action
        """
        if self._shared_list is None:
            self._shared_list = set()
        self._shared_list.add(self.const)
