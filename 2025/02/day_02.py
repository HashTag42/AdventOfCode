'''
Advent of Code 2025 - Day 2: Gift Shop
Puzzle: https://adventofcode.com/2025/day/2
'''


def sum_invalid_IDs(file: str) -> int:
    with open(file, 'r') as f:
        ranges = f.read().strip().split(',')
    part1 = 0
    for r in ranges:
        start, end = map(int, r.split('-'))
        part1 += sum(id for id in range(start, end + 1) if not is_valid_ID(id))
    return part1


def is_valid_ID(id: int) -> bool:
    id_str = str(id)
    mid = len(id_str) // 2
    if id_str[:mid] == id_str[mid:]:
        return False
    return True
