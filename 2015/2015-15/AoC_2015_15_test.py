from AoC_2015_15 import solve_part, get_data
import pytest

test_cases = [
    # filename, expected
    ('./2015/2015-15/example.txt', [62842880, 57600000]),
    ('./2015/2015-15/input.txt', [21367368, 1766400]),
]


@pytest.mark.parametrize("filename, expected", test_cases)
def test_solve_part1(filename, expected):
    assert solve_part(get_data(filename), 1) == expected[0]


@pytest.mark.parametrize("filename, expected", test_cases)
def test_solve_part2(filename, expected):
    assert solve_part(get_data(filename), 2) == expected[1]
