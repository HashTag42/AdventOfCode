'''
Advent of Code 2025 - Day DAY:
Puzzle: https://adventofcode.com/2025/day/DAY
'''


def solve_2025_DAY(file: str) -> tuple[int, int]:
    data1, data2 = get_data(file)
    return solve_part1(data1), solve_part2(data2)


def solve_part1(data) -> int:
    result = 0
    return result


def solve_part2(data) -> int:
    result = 0
    return result


def get_data(file) -> tuple[list[str], list[str]]:
    with open(file, 'r') as f:
        data1 = data2 = f.readlines()
    return data1, data2


if __name__ == "__main__":
    import pytest
    import sys
    sys.exit(pytest.main(['-v', './2025/DAY/day_2025_DAY_test.py']))
