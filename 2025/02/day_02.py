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


if __name__ == "__main__":
    import pytest
    import sys
    sys.exit(pytest.main(['-v', './2025/02/day_02_test.py']))
