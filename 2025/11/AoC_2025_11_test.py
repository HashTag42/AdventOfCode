from AoC_2025_11 import solve_part1, solve_part2, get_data
import pytest

test_cases = [
    # file, expected
    ('./2025/11/example.txt', [5, 0]),
    ('./2025/11/input.txt', [494, 0]),
]


@pytest.mark.parametrize("filename, expected", test_cases)
def test_solve_part1(filename, expected):
    assert solve_part1(get_data(filename)) == expected[0]


@pytest.mark.parametrize("filename, expected", test_cases)
def test_solve_part2(filename, expected):
    assert solve_part2(get_data(filename)) == expected[1]
