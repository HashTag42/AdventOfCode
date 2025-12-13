from AoC_2015_13 import solve_part1, solve_part2, get_data
import pytest

test_cases = [
    # file, expected
    ('./2015/2015-13/example.txt', [330, 286]),
    ('./2015/2015-13/input.txt', [709, 668]),
]


@pytest.mark.parametrize("file, expected", test_cases)
def test_solve_part1(file, expected):
    assert solve_part1(get_data(file)) == expected[0]


@pytest.mark.parametrize("file, expected", test_cases)
def test_solve_part2(file, expected):
    assert solve_part2(get_data(file)) == expected[1]
