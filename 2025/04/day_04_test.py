from day_04 import day_04
import pytest

test_cases = [
    # file, expected1
    ('./2025/04/example.txt', 13),
    ('./2025/04/input.txt', 1495),
]


@pytest.mark.parametrize("file, expected1", test_cases)
def test_day_04(file, expected1):
    assert day_04(file) == expected1
