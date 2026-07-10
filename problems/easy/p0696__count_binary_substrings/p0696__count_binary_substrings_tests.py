import unittest
from p0696__count_binary_substrings import Solution


class TestCountBinarySubstring(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()
        return super().setUp()

    def test1(self):
        self.assertEqual(self.sol.countBinarySubstrings("00110011"), 6)

    def test2(self):
        self.assertEqual(self.sol.countBinarySubstrings("10101"), 4)

    def test3(self):
        self.assertEqual(self.sol.countBinarySubstrings("100111001"), 6)
