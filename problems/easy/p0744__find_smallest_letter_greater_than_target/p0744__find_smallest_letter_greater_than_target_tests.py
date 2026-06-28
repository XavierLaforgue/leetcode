import unittest
from p0744__find_smallest_letter_greater_than_target import Solution


class TestSmallestLetterGreaterThanTarget(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()
        return super().setUp()

    def test1(self):
        self.assertEqual(self.sol.nextGreatestLetter(
            ["c", "f", "j"], "a"), "c")
        self.assertEqual(self.sol.nextGreatestLetter(
            ["c", "f", "j"], "c"), "f")
        self.assertEqual(self.sol.nextGreatestLetter(
            ["x", "x", "y", "y"], "z"), "x")
