from AoC_2015_19 import solve_part1, solve_part2, get_data
import pytest

test_cases_part1 = [
    # filename, expected
    ('./2015/2015-19/example1.txt', 4),
    ('./2015/2015-19/example2.txt', 7),
    ('./2015/2015-19/input.txt', 576),
]


test_cases_part2 = [
    # filename, expected
    ('./2015/2015-19/example3.txt', 3),
    ('./2015/2015-19/example4.txt', 6),
    ('./2015/2015-19/input.txt', 207),
]


@pytest.mark.parametrize("filename, expected", test_cases_part1)
def test_solve_part1(filename, expected):
    assert solve_part1(get_data(filename)) == expected


@pytest.mark.parametrize("filename, expected", test_cases_part2)
def test_solve_part2(filename, expected):
    assert solve_part2(get_data(filename)) == expected
