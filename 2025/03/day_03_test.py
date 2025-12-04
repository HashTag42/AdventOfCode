from day_03 import get_total_ouput, get_bank_max_joltage
import pytest

get_bank_max_joltage_test_cases = [
    # bank, expected_part1, expected_part2
    ("987654321111111", 98, 987654321111),
    ("811111111111119", 89, 811111111119),
    ("234234234234278", 78, 434234234278),
    ("818181911112111", 92, 888911112111),
]


get_total_output_test_cases = [
    # file, expected_part1, expected_part2
    ('./2025/03/example.txt', 357, 3121910778619),
    ('./2025/03/input.txt', 17346, 172981362045136),
]


@pytest.mark.parametrize("bank, expected_part1, expected_part2", get_bank_max_joltage_test_cases)
def test_get_bank_max_joltage(bank, expected_part1, expected_part2):
    assert get_bank_max_joltage(bank, 2) == expected_part1
    assert get_bank_max_joltage(bank, 12) == expected_part2


@pytest.mark.parametrize("file, expected_part1, expected_part2", get_total_output_test_cases)
def test_get_total_output(file, expected_part1, expected_part2):
    part1, part2 = get_total_ouput(file)
    assert part1 == expected_part1
    assert part2 == expected_part2
