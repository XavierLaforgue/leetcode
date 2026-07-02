import unittest
from p2812__find_the_safest_path_in_a_grid import Solution


class TestFindSafestPathInGrid(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()
        return super().setUp()

    def test1(self):
        self.assertEqual(self.sol.maximumSafenessFactor(
            [[1, 0, 0], [0, 0, 0], [0, 0, 1]]), 0)

    def test2(self):
        self.assertEqual(self.sol.maximumSafenessFactor(
            [[0, 0, 1], [0, 0, 0], [0, 0, 0]]), 2)

    def test3(self):
        self.assertEqual(self.sol.maximumSafenessFactor(
            [[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]]), 2)
