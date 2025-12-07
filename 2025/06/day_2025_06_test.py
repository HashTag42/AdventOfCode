from day_2025_06 import solve_2025_06
import pytest


test_cases = [
    # file, expected_part1, expected_part2
    ('./2025/06/example.txt', 4277556, 3263827),
    ('./2025/06/input.txt', 5667835681547, 9434900032651),
]


@pytest.mark.parametrize("file, expected_part1, expected_part2", test_cases)
def test_solve_2025_06_part1(file, expected_part1, expected_part2):
    actual_part1, actual_part2 = solve_2025_06(file)
    assert actual_part1 == expected_part1


@pytest.mark.parametrize("file, expected_part1, expected_part2", test_cases)
def test_solve_2025_06_part2(file, expected_part1, expected_part2):
    actual_part1, actual_part2 = solve_2025_06(file)
    assert actual_part2 == expected_part2
