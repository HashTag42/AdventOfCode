from day_2025_DAY import solve_part1, solve_part2, get_data
import pytest

test_cases = [
    # file, expected
    ('./2025/DAY/example.txt', [0, 0]),
    ('./2025/DAY/input.txt', [0, 0]),
]


@pytest.mark.parametrize("file, expected", test_cases)
def test_solve_part1(file, expected):
    assert solve_part1(get_data(file)[0]) == expected[0]


@pytest.mark.parametrize("file, expected", test_cases)
def test_solve_part2(file, expected):
    assert solve_part2(get_data(file)[1]) == expected[1]
