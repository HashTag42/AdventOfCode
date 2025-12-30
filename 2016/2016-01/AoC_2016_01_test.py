from AoC_2016_01 import solve_part1, solve_part2, get_data
import pytest

test_cases = [
    # filename, expected
    ('./2016/2016-01/example.txt', [12, 0]),
    ('./2016/2016-01/input.txt', [271, 0]),
]


@pytest.mark.parametrize("filename, expected", test_cases)
def test_solve_part1(filename, expected):
    assert solve_part1(get_data(filename)) == expected[0]


@pytest.mark.parametrize("filename, expected", test_cases)
def test_solve_part2(filename, expected):
    assert solve_part2(get_data(filename)) == expected[1]
