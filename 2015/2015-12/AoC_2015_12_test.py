from AoC_2015_12 import solve_part1, solve_part2, get_data
import pytest

test_cases = [
    # file, expected
    ('./2015/2015-12/input.txt', [191164, 0]),
]


@pytest.mark.parametrize("file, expected", test_cases)
def test_solve_part1(file, expected):
    assert solve_part1(get_data(file)) == expected[0]


@pytest.mark.parametrize("file, expected", test_cases)
def test_solve_part2(file, expected):
    assert solve_part2(get_data(file)) == expected[1]
