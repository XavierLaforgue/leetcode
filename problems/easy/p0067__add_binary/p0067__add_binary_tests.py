import pytest
from p0067__add_binary import Solution

@pytest.fixture
def addBinary():
    return Solution().addBinary

def test_1(addBinary):
    assert addBinary("11", "1") == "100"

def test_2(addBinary):
    assert addBinary("1010", "1011") == "10101"
