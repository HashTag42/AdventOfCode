from day_2025_07 import solve_part1, solve_part2, get_data
import pytest


test_cases = [
    # file, expected
    ('./2025/07/example.txt', [21, 40]),
    ('./2025/07/input.txt', [1656, 76624086587804]),
]


@pytest.mark.parametrize("file, expected", test_cases)
def test_solve_part1(file, expected):
    actual1 = solve_part1(get_data(file))
    assert actual1 == expected[0]


@pytest.mark.parametrize("file, expected", test_cases)
def test_solve_part2(file, expected):
    actual2 = solve_part2(get_data(file))
    assert actual2 == expected[1]
