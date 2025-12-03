'''
Advent of Code 2025 - Day 2: Gift Shop
Puzzle: https://adventofcode.com/2025/day/2
'''


def add_invalid_IDs(file: str) -> int:
    part1 = 0
    with open(file, 'r') as input:
        ranges = input.read().split(',')
        for r in ranges:
            first_ID, last_ID = r.split('-')
            start, stop = int(first_ID), int(last_ID) + 1
            for id in range(start, stop):
                if not is_valid_ID(id):
                    part1 += id
    return part1


def is_valid_ID(id: int) -> bool:
    id_str = str(id)
    cut = len(id_str) // 2
    if id_str[0:cut] == id_str[cut:]:
        return False
    return True
