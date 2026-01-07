from AoC_2016_08 import solve_part1, get_data
import pytest

test_cases = [
    # filename, cols, rows, expected
    ('./2016/2016-08/example.txt', 7, 3, 6),
    ('./2016/2016-08/input.txt', 50, 6, 123),
]


@pytest.mark.parametrize("filename, cols, rows, expected", test_cases)
def test_solve_part1(filename, cols, rows, expected):
    assert solve_part1(get_data(filename), cols, rows) == expected
