from day_2025_05 import solve_2025_05
import pytest


test_cases = [
    # file, expected_part1, expected_part2
    ('./2025/05/example.txt', 3, 0),
    ('./2025/05/input.txt', 679, 0),
]


@pytest.mark.parametrize("file, expected_part1, expected_part2", test_cases)
def test_solve_2025_05(file, expected_part1, expected_part2):
    actual_part1, actual_part2 = solve_2025_05(file)
    assert actual_part1 == expected_part1
    # assert actual_part2 == expected_part2
