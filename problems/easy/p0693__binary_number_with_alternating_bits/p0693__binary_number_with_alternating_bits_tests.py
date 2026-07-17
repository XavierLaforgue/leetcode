import pytest
from p0693__binary_number_with_alternating_bits import Solution

@pytest.fixture
def hasAlternatingBits():
    return Solution().hasAlternatingBits

def test_1(hasAlternatingBits):
    assert hasAlternatingBits(5)

def test_2(hasAlternatingBits):
    assert not hasAlternatingBits(7)

def test_3(hasAlternatingBits):
    assert not hasAlternatingBits(11)

