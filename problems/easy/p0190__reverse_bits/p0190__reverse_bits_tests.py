import pytest
from p0190__reverse_bits import Solution

@pytest.fixture
def reverseBits():
    return Solution().reverseBits

def test_1(reverseBits):
    assert reverseBits(43261596) == 964176192

def test_2(reverseBits):
    assert reverseBits(2147483644) == 1073741822
