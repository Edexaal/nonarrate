from .rule import Rule

class CharRule(Rule):
    """Holds validator rule for custom character strategy filter."""

    def __init__(self,custom_names:str):
        super().__init__(rf'([\'"]).*?\b(?:{custom_names})\b.*?\1\s*([\'"])[^\2]+\2?', True)
