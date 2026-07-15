import pytest
from p3658__gcd_of_odd_and_even_sums import Solution

@pytest.fixture
def gcdOfOddEvenSums():
    return Solution().gcdOfOddEvenSums

def test_1(gcdOfOddEvenSums):
    assert gcdOfOddEvenSums(4) == 4

def test_2(gcdOfOddEvenSums):
    assert gcdOfOddEvenSums(5) == 5
