import unittest
from p2812__find_the_safest_path_in_a_grid import Solution
from collections import deque


class TestFindSafestPathInGrid(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()
        return super().setUp()

    def test_thief_queue(self):
        self.assertEqual(
            self.sol.create_thief_queue_and_grid(
                [[1, 0, 0], [0, 0, 0], [0, 0, 1]]),
            ([[0, -1, -1], [-1, -1, -1], [-1, -1, 0]], deque([(0, 0), (2, 2)]))
        )

    def test_get_neighbours(self):
        neighbours = self.sol.get_neighbours(0, 0, 3)
        expected = [(0, 1), (1, 0)]
        self.assertCountEqual(neighbours, expected)
        self.assertEqual(set(neighbours), set(expected))
        neighbours = self.sol.get_neighbours(1, 1, 3)
        expected = [(0, 1), (1, 0), (1, 2), (2, 1)]
        self.assertCountEqual(neighbours, expected)
        self.assertEqual(set(neighbours), set(expected))

    def test_get_safeness_per_cell(self):
        grid = [[1, 0, 0], [0, 0, 0], [0, 0, 1]]
        safeness_grid = [[0, 1, 2],
                         [1, 2, 1],
                         [2, 1, 0]]
        self.assertEqual(self.sol.get_safeness_per_cell(grid, len(grid)),
                         safeness_grid)

    def test1(self):
        self.assertEqual(self.sol.maximumSafenessFactor(
            [[1, 0, 0], [0, 0, 0], [0, 0, 1]]), 0)

    def test2(self):
        self.assertEqual(self.sol.maximumSafenessFactor(
            [[0, 0, 1], [0, 0, 0], [0, 0, 0]]), 2)

    def test3(self):
        self.assertEqual(self.sol.maximumSafenessFactor(
            [[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]]), 2)


if __name__ == '__main__':
    unittest.main()
