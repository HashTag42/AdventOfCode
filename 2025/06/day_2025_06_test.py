from day_2025_06 import solve_2025_06
import pytest


test_cases = [
    # file, expected
    ('./2025/06/example.txt', [4277556, 3263827]),
    ('./2025/06/input.txt', [5667835681547, 9434900032651]),
]


@pytest.mark.parametrize("file, expected", test_cases)
def test_solve_2025_06(file, expected):
    actual1, actual2 = solve_2025_06(file)
    assert actual1 == expected[0]
    assert actual2 == expected[1]
