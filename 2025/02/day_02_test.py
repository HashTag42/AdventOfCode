from day_02 import (
    sum_invalid_IDs,
    is_valid_ID_part1,
    is_valid_ID_part2,
)
import pytest


test_cases = [
    # file, expected_part1, expected_part2
    ('./2025/02/example.txt', 1227775554, 4174379265),
    ('./2025/02/input.txt', 38158151648, 45283684555),
]


@pytest.mark.parametrize("file, expected_part1, expected_part2", test_cases)
def test_sum_invalid_IDs(file, expected_part1, expected_part2):
    part1, part2 = sum_invalid_IDs(file)
    assert part1 == expected_part1
    assert part2 == expected_part2


is_valid_ID_part1_test_cases = [
    # id_int, expected

    # invalid IDs
    (11, False),
    (22, False),
    (99, False),
    (1010, False),
    (1188511885, False),
    (222222, False),
    (446446, False),
    (38593859, False),

    # valid IDs
    (1698522, True),
    (1698528, True),
    (446443, True),
    (446449, True),
    (38593856, True),
    (38593862, True),
    (565653, True),
    (565659, True),
    (824824821, True),
    (824824827, True),
    (2121212118, True),
    (2121212124, True),
]


@pytest.mark.parametrize("id_int, expected", is_valid_ID_part1_test_cases)
def test_is_valid_ID_part1(id_int, expected):
    assert is_valid_ID_part1(id_int) == expected


is_valid_ID_part2_test_cases = [
    # id_int, expected

    # invalid IDs
    (11, False),
    (22, False),
    (99, False),
    (111, False),
    (999, False),
    (1010, False),
    (1188511885, False),
    (222222, False),
    (446446, False),
    (38593859, False),
    (565656, False),
    (824824824, False),
    (2121212121, False),

    # valid IDs
    (12, True),
    (1234, True),
    (1698522, True),
    (1698528, True),
    (446443, True),
    (446449, True),
    (38593856, True),
    (38593862, True),
    (565653, True),
    (565659, True),
    (824824821, True),
    (824824827, True),
    (2121212118, True),
    (2121212124, True),
]


@pytest.mark.parametrize("id_int, expected", is_valid_ID_part2_test_cases)
def test_is_valid_ID_part2(id_int, expected):
    assert is_valid_ID_part2(id_int) == expected
