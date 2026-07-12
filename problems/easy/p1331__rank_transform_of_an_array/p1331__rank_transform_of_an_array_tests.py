import signal

import pytest
from p1331__rank_transform_of_an_array import Solution
from long_array import long_array


@pytest.fixture
def arrayRankTransform():
    return Solution().arrayRankTransform


def test_1(arrayRankTransform):
    assert arrayRankTransform([40, 10, 20, 30]) == [4, 1, 2, 3]


def test_2(arrayRankTransform):
    assert arrayRankTransform([100, 100, 100]) == [1, 1, 1]


def test_3(arrayRankTransform):
    arr = [37, 12, 28, 9, 100, 56, 80, 5, 12]
    assert arrayRankTransform(arr) == [5, 3, 4, 2, 8, 6, 7, 1, 3]


def _raise_timeout(signum, frame):
    raise TimeoutError("arrayRankTransform took longer than 3 seconds")


def test_4(arrayRankTransform):
    previous_handler = signal.signal(signal.SIGALRM, _raise_timeout)
    signal.alarm(3)
    try:
        arrayRankTransform(long_array)
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, previous_handler)

if __name__ == "__main__":
    print(Solution().arrayRankTransform([37, 12, 28, 9, 100, 56, 80, 5, 12]))
