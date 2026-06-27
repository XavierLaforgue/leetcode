import unittest
import importlib.util
from pathlib import Path
from LongTestCase import extreme_input

# path = Path(__file__).with_name(
#     "3020_find-the-maximum-number-of-elements-in-subset.py"
#     )

path = Path.cwd() / ("3020_find-the-maximum-number-of-elements-in-subset"
                     "_CounterNoHelper.py")

spec = importlib.util.spec_from_file_location("subset_module", path)
if spec is None or spec.loader is None:
    raise ImportError(f"Could not load module from {path}")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

Solution = module.Solution


class TestMaximumLength(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution()

    def testCase1ASet(self):
        self.assertEqual(self.sol.maximumLength([5, 4, 1, 2, 2]), 3)

    def testCase2NoSet(self):
        self.assertEqual(self.sol.maximumLength([1, 3, 2, 4]), 1)

    def testCase3SetOfOnes(self):
        self.assertEqual(self.sol.maximumLength([1, 1]), 1)

    def testCase4LargeSetOfOnes(self):
        self.assertEqual(self.sol.maximumLength(
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 4, 8, 16, 32, 64, 128, 256,
             512, 1024]), 9)

    def testCase4HugeDataSet(self):
        self.assertEqual(self.sol.maximumLength(extreme_input), 5)
