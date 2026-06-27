import unittest
from Q2__Merge_Intervals import Solution


class TestMergeIntervals(unittest.TestCase):
    def test_overlapping_intervals(self):
        sol = Solution()
        self.assertEqual(sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]]),
                         [[1, 6], [8, 10], [15, 18]])
        self.assertEqual(sol.merge([[1, 4], [4, 5]]), [[1, 5]])
        self.assertEqual(sol.merge([[4, 7], [1, 4]]), [[1, 7]])
