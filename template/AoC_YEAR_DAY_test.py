from AoC_YEAR_DAY import solve_part1, solve_part2, get_data
import pytest

test_cases = [
    # file, expected
    ('./YEAR/DAY/example.txt', [0, 0]),
    # ('./YEAR/DAY/input.txt', [0, 0]),
]


@pytest.mark.parametrize("file, expected", test_cases)
def test_solve_part1(file, expected):
    assert solve_part1(get_data(file)) == expected[0]


@pytest.mark.parametrize("file, expected", test_cases)
def test_solve_part2(file, expected):
    assert solve_part2(get_data(file)) == expected[1]
