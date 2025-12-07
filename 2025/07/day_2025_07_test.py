from day_2025_07 import solve_2025_07
import pytest


test_cases = [
    # file, expected
    ('./2025/07/example.txt', [21, 0]),
    ('./2025/07/input.txt', [1656, 0]),
]


@pytest.mark.parametrize("file, expected", test_cases)
def test_solve_2025_06(file, expected):
    actual1, actual2 = solve_2025_07(file)
    assert actual1 == expected[0]
    assert actual2 == expected[1]
