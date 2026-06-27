import unittest
from Q3__House_Robber import Solution


class TestHouseRobber(unittest.TestCase):
    def test_cases_leetcode(self):
        sol = Solution()
        self.assertEqual(sol.rob([1, 2, 3, 1]), 4)
        self.assertEqual(sol.rob([2, 7, 9, 3, 1]), 12)
