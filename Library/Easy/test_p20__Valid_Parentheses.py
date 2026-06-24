import unittest
from p20__Valid_Parentheses import Solution


class TestValidParentheses(unittest.TestCase):
    def test_parenthesis_pair(self):
        sol = Solution()
        self.assertTrue(sol.isValid('()'))
        self.assertTrue(sol.isValid("()[]{}"), True)
        self.assertFalse(sol.isValid('(]'), False)
        self.assertTrue(sol.isValid("([])"))
        self.assertFalse(sol.isValid("([)]"))


if __name__ == "__main__":
    unittest.main()
