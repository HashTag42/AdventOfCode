from day_2025_06 import solve_part1, solve_part2, get_data
import pytest


test_cases = [
    # file, expected
    ('./2025/06/example.txt', [4277556, 3263827]),
    ('./2025/06/input.txt', [5667835681547, 9434900032651]),
]


@pytest.mark.parametrize("file, expected", test_cases)
def test_solve_part1(file, expected):
    assert solve_part1(get_data(file)[0]) == expected[0]


@pytest.mark.parametrize("file, expected", test_cases)
def test_solve_part2(file, expected):
    assert solve_part2(get_data(file)[1]) == expected[1]
