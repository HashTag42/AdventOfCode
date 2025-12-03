from day_02 import sum_invalid_IDs
import pytest


test_cases = [
    # file, expected_part1
    ('./2025/02/example.txt', 1227775554),
    ('./2025/02/input.txt', 38158151648),
]


@pytest.mark.parametrize("file, expected_part1", test_cases)
def test_sum_invalid_IDs(file, expected_part1):
    assert sum_invalid_IDs(file) == expected_part1
