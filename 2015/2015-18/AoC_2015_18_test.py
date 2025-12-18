from AoC_2015_18 import solve_part1, solve_part2, get_data
import pytest

test_cases = [
    # filename, steps, expected
    ('./2015/2015-18/example1.txt', 4, [4, 0]),
    ('./2015/2015-18/input.txt', 100, [821, 0]),
]


@pytest.mark.parametrize("filename, steps, expected", test_cases)
def test_solve_part1(filename, steps, expected):
    assert solve_part1(get_data(filename), steps) == expected[0]


@pytest.mark.parametrize("filename, steps, expected", test_cases)
def test_solve_part2(filename, steps, expected):
    assert solve_part2(get_data(filename)) == expected[1]
