import unittest
from ..fixture import get_dialogue_list
from lib.validator.speaker import BasicCharacterStrategy, CharacterStrategy
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
            9: '"Mira Thinking" "Today I heard something new and unmemorable."',
            10: '"Leon\'s thoughts" "Today I heard something new and unmemorable."',
            11: '"angela\'s Thoughts" "Today I heard something new and unmemorable."',
            12: '"angela\'s Thought" "Today I heard something new and unmemorable."',
            13: '"My Mind" "Today I heard something new and unmemorable."',
            14: '"My mind" "Today I heard something new and unmemorable."',
            15: '"Mymind" "Today I heard something new and unmemorable."',
            16: '"MyMind" "Today I heard something new and unmemorable."',
            17: 'narrator" "Today I heard something new and unmemorable."',
            18: '"narrator "Today I heard something new and unmemorable."',
            19: 'narrator "Today I heard something new and unmemorable."',
            # Custom basic
            20: '"mayaa" "Today I heard something new and unmemorable."',
            21: '"maya" "Today I heard something new and unmemorable."',
            22: '"maya thinking" "Today I heard something new and unmemorable."',
            23: '"maya Thinking" "Today I heard something new and unmemorable."',
            24: '"maya thoughts" "Today I heard something new and unmemorable."',
            25: '"maya Thoughts" "Today I heard something new and unmemorable."',
            26: '"maya\'s mind" "Today I heard something new and unmemorable."',
            27: '"maya\'s Mind" "Today I heard something new and unmemorable."',
            28: 'maya" "Today I heard something new and unmemorable."',
            29: '"maya "Today I heard something new and unmemorable."',
            30: 'maya "Today I heard something new and unmemorable."',
            31: '"maya cornstarke" "Today I heard something new and unmemorable."',
            32: '"Maya" "Today I heard something new and unmemorable."',
            33: '"Maya\'s Mind" "Today I heard something new and unmemorable."',
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
        self.start(
            BasicCharacterStrategy(),
            [3, 7, 8, 9, 10, 11, 12, 13, 14, 22, 23, 24, 25, 26, 27, 33],
        )

    def test_custom_char(self):
        self.start(CharacterStrategy("maya"), [21, 22, 23, 24, 25, 26, 27, 31, 32, 33])
