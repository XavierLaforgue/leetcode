import pytest
from p0026__remove_duplicates_from_sorted_array import Solution


@pytest.fixture
def removeDuplicates():
    return Solution().removeDuplicates


def test_1(removeDuplicates):
    nums = [1, 1, 2]
    assert removeDuplicates(nums) == 2
    assert nums == [1, 2]


def test_2(removeDuplicates):
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    assert removeDuplicates(nums) == 5
    assert nums == [0, 1, 2, 3, 4]
