from AoC_2015_25 import solve_part1, solve_part2, get_data
import pytest

test_cases = [
    # filename, expected
    ('./2015/2015-25/input.txt', [2650453, 0]),
]


@pytest.mark.parametrize("filename, expected", test_cases)
def test_solve_part1(filename, expected):
    row, col = get_data(filename)
    assert solve_part1(row, col) == expected[0]


@pytest.mark.parametrize("filename, expected", test_cases)
def test_solve_part2(filename, expected):
    row, col = get_data(filename)
    assert solve_part2(row, col) == expected[1]
