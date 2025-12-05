'''
Advent of Code 2025 - Day DAY:
Puzzle: https://adventofcode.com/2025/day/DAY
'''


def solve_2025_DAY(file: str) -> tuple[int, int]:
    with open(file, 'r') as f:
        data = f.readlines()
    part1, part2 = solve_part1(), solve_part2()
    return part1, part2


def solve_part1() -> int:
    return 0


def solve_part2() -> int:
    return 0


if __name__ == "__main__":
    import pytest
    import sys
    sys.exit(pytest.main(['-v', './2025/DAY/day_2025_DAY_test.py']))
