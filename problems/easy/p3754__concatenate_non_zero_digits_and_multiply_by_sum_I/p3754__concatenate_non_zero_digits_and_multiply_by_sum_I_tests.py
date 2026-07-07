from p3754__concatenate_non_zero_digits_and_multiply_by_sum_I import Solution
import pytest


@pytest.fixture
def sumAndMultiply():
    return Solution().sumAndMultiply


def test1(sumAndMultiply):
    n = 10203004
    assert sumAndMultiply(n) == 12340


def test2(sumAndMultiply):
    n = 1000
    assert sumAndMultiply(n) == 1

def test3(sumAndMultiply):
    n = 0
    assert sumAndMultiply(n) == 0
