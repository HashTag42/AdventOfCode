from day_2025_09 import solve_part1, solve_part2, get_data
import pytest

test_cases = [
    # file, expected
    ('./2025/09/example.txt', [50, 0]),
    ('./2025/09/input.txt', [4752484112, 0]),
]


@pytest.mark.parametrize("file, expected", test_cases)
def test_solve_part1(file, expected):
    assert solve_part1(get_data(file)) == expected[0]


@pytest.mark.parametrize("file, expected", test_cases)
def test_solve_part2(file, expected):
    assert solve_part2(get_data(file)) == expected[1]
