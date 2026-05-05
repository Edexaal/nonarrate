class PrevInfo:
    """Holds previous line information of a file.

    Attributes:
        line: the most recent previous line.
    """

    def __init__(self):
        self.reset()

    def reset(self):
        """Reset all previous information back to default values."""
        self.line = ""
