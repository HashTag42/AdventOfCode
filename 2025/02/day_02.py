'''
Advent of Code 2025 - Day 2: Gift Shop
Puzzle: https://adventofcode.com/2025/day/2
'''
import re


def sum_invalid_IDs(file: str) -> tuple[int, int]:
    with open(file, 'r') as f:
        ranges = f.read().strip().split(',')
    part1 = part2 = 0
    for range_str in ranges:
        start, end = map(int, range_str.split('-'))
        part1 += sum(id for id in range(start, end + 1) if not is_valid_ID_part1(id))
        for current_id in range(start, end + 1):
            if not is_valid_ID_part2(current_id):
                part2 += current_id
    return part1, part2


def is_valid_ID_part1(id_num: int) -> bool:
    id_str = str(id_num)
    mid = len(id_str) // 2
    if id_str[:mid] == id_str[mid:]:
        return False
    return True


def is_valid_ID_part2(id_num: int) -> bool:
    id_str = str(id_num)
    return not re.match(r'^(.+?)\1+$', id_str)


sum_invalid_IDs_test_cases = [
    # file, expected_part1, expected_part2
    ('./2025/02/example.txt', 1227775554, 4174379265),
    ('./2025/02/input.txt', 38158151648, 45283684555),
]

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

if __name__ == "__main__":
    for test in sum_invalid_IDs_test_cases:
        part1, part2 = sum_invalid_IDs(test[0])
        assert part1 == test[1], f"sum_invalid_IDs: part1: {part1} is not equal to {test[1]}"
        assert part2 == test[2], f"sum_invalid_IDs: part2: {part2} is not equal to {test[2]}"
    for test in is_valid_ID_test_cases:
        assert is_valid_ID_part1(test[0]) == test[1], f"is_valid_ID_part1({test[0]}) is not equal to {test[1]}"
        assert is_valid_ID_part2(test[0]) == test[2], f"is_valid_ID_part2({test[0]}) is not equal to {test[2]}"
