'''file: day_04_test.py'''
from day_04 import day_04
import pytest

test_cases = [
    # file, expected_part1, expected_part2
    ('./2025/04/example.txt', 13, 43),
    ('./2025/04/input.txt', 1495, 8768),
]


@pytest.mark.parametrize("file, expected_part1, expected_part2", test_cases)
def test_day_04(file, expected_part1, expected_part2):
    actual_part1, actual_part2 = day_04(file)
    assert actual_part1 == expected_part1
    assert actual_part2 == expected_part2
