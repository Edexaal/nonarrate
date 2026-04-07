from typing import final


@final
class Log:
    """Provides tools for writing message to the terminal."""

    @staticmethod
    def log(text: str):
        print(text)

    @classmethod
    def wait(cls, text: str):
        cls.log(f"{text}...")

    @classmethod
    def mark(cls,text: str):
        dashes = '-' * 8
        cls.log(f"{dashes}> {text} <{dashes}")

    @classmethod
    def info(cls,title:str,value):
        cls.log(f"[{title}]: {value}")