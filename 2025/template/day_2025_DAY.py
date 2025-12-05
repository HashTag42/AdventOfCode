'''
Advent of Code 2025 - Day DAY:
Puzzle: https://adventofcode.com/2025/day/DAY
'''


def solve_2025_DAY(file: str) -> tuple[int, int]:
    data = get_data(file)
    part1, part2 = solve_part1(data), solve_part2(data)
    return part1, part2


def solve_part1(data) -> int:
    return 0


def solve_part2(data) -> int:
    return 0


def get_data(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    return lines


if __name__ == "__main__":
    import pytest
    import sys
    sys.exit(pytest.main(['-v', './2025/DAY/day_2025_DAY_test.py']))
