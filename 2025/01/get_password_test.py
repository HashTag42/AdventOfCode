from get_password import get_password
import pytest

test_cases = [
    ('./2025/01/input0.txt', 3),
    ('./2025/01/input.txt', 1059),
]


@pytest.mark.parametrize("input, expected", test_cases)
def test_get_password(input, expected):
    assert get_password(input) == expected
