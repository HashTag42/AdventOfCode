from day_02 import (
    sum_invalid_IDs,
    is_valid_ID_part1,
    is_valid_ID_part2,
)
import pytest


sum_invalid_IDs_test_cases = [
    # file, expected_part1, expected_part2
    ('./2025/02/example.txt', 1227775554, 4174379265),
    ('./2025/02/input.txt', 38158151648, 45283684555),
]


@pytest.mark.parametrize("file, expected_part1, expected_part2", sum_invalid_IDs_test_cases)
def test_sum_invalid_IDs(file, expected_part1, expected_part2):
    part1, part2 = sum_invalid_IDs(file)
    assert part1 == expected_part1
    assert part2 == expected_part2


is_valid_ID_test_cases = [
    # id_int, expected_part1, expected_part2
    (11, False, False),
    (12, True, True),
    (22, False, False),
    (99, False, False),
    (111, True, False),
    (999, True, False),
    (1010, False, False),
    (1234, True, True),
    (222222, False, False),
    (446443, True, True),
    (446446, False, False),
    (446449, True, True),
    (565653, True, True),
    (565656, True, False),
    (565659, True, True),
    (1698522, True, True),
    (1698528, True, True),
    (38593856, True, True),
    (38593859, False, False),
    (38593862, True, True),
    (824824821, True, True),
    (824824824, True, False),
    (824824827, True, True),
    (1188511885, False, False),
    (2121212118, True, True),
    (2121212121, True, False),
    (2121212124, True, True),
]


@pytest.mark.parametrize("id_int, expected_part1, expected_part2", is_valid_ID_test_cases)
def test_is_valid_ID(id_int, expected_part1, expected_part2):
    assert is_valid_ID_part1(id_int) == expected_part1
    assert is_valid_ID_part2(id_int) == expected_part2
