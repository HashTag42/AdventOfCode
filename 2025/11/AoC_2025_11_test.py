from AoC_2025_11 import solve_part1, solve_part2, get_data
import pytest

test_cases_part1 = [
    # filename, expected
    ('./2025/11/example1.txt', 5),
    ('./2025/11/input.txt', 494),
]

test_cases_part2 = [
    # filename, expected
    ('./2025/11/example2.txt', 2),
    ('./2025/11/input.txt', 296006754704850),
]


@pytest.mark.parametrize("filename, expected", test_cases_part1)
def test_solve_part1(filename, expected):
    assert solve_part1(get_data(filename)) == expected


@pytest.mark.parametrize("filename, expected", test_cases_part2)
def test_solve_part2(filename, expected):
    assert solve_part2(get_data(filename)) == expected
