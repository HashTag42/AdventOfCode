from day_2025_DAY import solve_2025_DAY
import pytest


test_cases = [
    # file, expected_part1, expected_part2
    ('./2025/DAY/example.txt', 0, 0),
    ('./2025/DAY/input.txt', 0, 0),
]


@pytest.mark.parametrize("file, expected_part1, expected_part2", test_cases)
def test_solve_2025_DAY(file, expected_part1, expected_part2):
    actual_part1, actual_part2 = solve_2025_DAY(file)
    assert actual_part1 == expected_part1
    assert actual_part2 == expected_part2
