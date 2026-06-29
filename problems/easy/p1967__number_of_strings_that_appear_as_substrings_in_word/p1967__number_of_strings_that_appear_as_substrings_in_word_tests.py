import unittest
from p1967__number_of_strings_that_appear_as_substrings_in_word import Solution


class TestNumberOsStringsInWord(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()
        return super().setUp()

    def test1(self):
        self.assertEqual(self.sol.numOfStrings(["a","abc","bc","d"], "abc"), 3)

    def test2(self):
        self.assertEqual(self.sol.numOfStrings(["a", "b", "c"], "aaaaabbbbb"), 2)
    
    def test3(self):
        self.assertEqual(self.sol.numOfStrings(["a", "a", "a"], "ab"), 3)
