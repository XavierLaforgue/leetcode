import pytest
from p2685__count_the_number_of_complete_components import Solution


@pytest.fixture
def countCompleteComponents():
    return Solution().countCompleteComponents


def test_1(countCompleteComponents):
    assert countCompleteComponents(6, [[0, 1], [0, 2], [1, 2], [3, 4]]) == 3


def test_2(countCompleteComponents):
    assert countCompleteComponents(6, [[0, 1], [0, 2], [1, 2], [3, 4],
                                       [3, 5]]) == 1
