import unittest
from ..fixture import get_dialogue_list
from lib.validator.speaker import BasicCharacterStrategy
from lib.validator.ivalidator_chain import IValidatorChain


class TestCharacter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dialogues = {
            0: '"Jim liked driving around town with his hazard lights on."',
            1: 'mc "Today I heard something new and unmemorable."',
            2: 'my_var = "Today I heard something new and unmemorable."',
            3: '"Narrator" "Today I heard something new and unmemorable."',
            4: '"developer" "Today I heard something new and unmemorable."',
            5: 'dev" "Today I heard something new and unmemorable."',
            6: '"dev "Today I heard something new and unmemorable."',
            7: '"narrator" "Today I heard something new and unmemorable."',
            8: '"nichole thinking" "Today I heard something new and unmemorable."',
            9: '"Leon\'s thoughts" "Today I heard something new and unmemorable."',
            10: 'narrator" "Today I heard something new and unmemorable."',
            11: '"narrator "Today I heard something new and unmemorable."',
            12: 'narrator "Today I heard something new and unmemorable."',
        }

    def validate_lines(self):
        valid_lines, invalid_lines = get_dialogue_list(
            self.valid_indexes, TestCharacter.dialogues
        )
        for line in valid_lines:
            with self.subTest(line=line):
                self.assertTrue(self.validator.is_valid(line), line)
        for line in invalid_lines:
            with self.subTest(line=line):
                self.assertFalse(self.validator.is_valid(line), line)

    def start(self, strategy: IValidatorChain, valid_indexes: list[int]):
        self.validator = strategy
        self.valid_indexes = valid_indexes
        self.validate_lines()

    def test_basic_char(self):
        self.start(BasicCharacterStrategy(), [3, 7, 8, 9])
