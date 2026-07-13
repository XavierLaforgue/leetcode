import pytest
from p1291__sequential_digits import Solution

@pytest.fixture
def sequentialDigits():
    return Solution().sequentialDigits

def test_1(sequentialDigits):
    assert sequentialDigits(100, 300) == [123, 234]

def test_2(sequentialDigits):
    assert sequentialDigits(1000, 13000) == [1234, 2345, 3456, 4567, 5678, 6789, 12345]
