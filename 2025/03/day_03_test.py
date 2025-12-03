from day_03 import get_bank_max_joltage, get_file_total_ouput
import pytest

get_bank_max_joltage_test_cases = [
    # bank, expected_max_joltage
    ("987654321111111", 98),
    ("811111111111119", 89),
    ("234234234234278", 78),
    ("818181911112111", 92),
]


@pytest.mark.parametrize("bank, expected_max_joltage", get_bank_max_joltage_test_cases)
def test_get_bank_max_joltage(bank, expected_max_joltage):
    actual = get_bank_max_joltage(bank)
    expected = expected_max_joltage
    assert actual == expected, f"{actual} != {expected}"


get_file_total_output_test_cases = [
    # file, expected_part1
    ('./2025/03/example.txt', 357),
    ('./2025/03/input.txt', 17346),
]


@pytest.mark.parametrize("file, expected_part1", get_file_total_output_test_cases)
def test_get_file_total_output(file, expected_part1):
    actual = get_file_total_ouput(file)
    expected = expected_part1
    assert actual == expected, f"{actual} != {expected}"
