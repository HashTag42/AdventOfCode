from AoC_YEAR_DAY import solve_part1, solve_part2, get_data
import pytest

test_cases = [
    # filename, expected
    ('./YEAR/DAY/example.txt', [0, 0]),
    ('./YEAR/DAY/input.txt', [0, 0]),
]


@pytest.mark.parametrize("filename, expected", test_cases)
def test_solve_part1(filename, expected):
    assert solve_part1(get_data(filename)) == expected[0]


@pytest.mark.parametrize("filename, expected", test_cases)
def test_solve_part2(filename, expected):
    assert solve_part2(get_data(filename)) == expected[1]
