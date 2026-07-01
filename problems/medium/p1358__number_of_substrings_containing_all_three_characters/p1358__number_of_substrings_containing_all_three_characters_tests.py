import unittest
from p1358__number_of_substrings_containing_all_three_characters\
    import Solution
from long_string import long_string, long_string2
import signal


class TestNumberOfSubstrings(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()
        return super().setUp()

    def test1(self):
        self.assertEqual(self.sol.numberOfSubstrings("abcabc"), 10)

    def test2(self):
        self.assertEqual(self.sol.numberOfSubstrings("aaacb"), 3)

    def test3(self):
        self.assertEqual(self.sol.numberOfSubstrings("abc"), 1)

    def test4(self):
        self.assertEqual(self.sol.numberOfSubstrings(long_string), 37291218)

    def _timeout_handler(self, signum, frame):
        raise TimeoutError()

    def test5_no_timeout(self):
        signal.signal(signal.SIGALRM, self._timeout_handler)
        signal.alarm(5)
        try:
            result = self.sol.numberOfSubstrings(long_string2)
            self.assertIsInstance(result, int)
        finally:
            signal.alarm(0)
