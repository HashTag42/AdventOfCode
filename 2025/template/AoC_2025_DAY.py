'''
Advent of Code 2025 - Day DAY:
Puzzle: https://adventofcode.com/2025/day/DAY
'''


def solve_2025_DAY(file: str) -> tuple[int, int]:
    data = get_data(file)
    return solve_part1(data), solve_part2(data)


def solve_part1(data) -> int:
    result = 0
    return result


def solve_part2(data) -> int:
    result = 0
    return result


def get_data(file) -> list[str]:
    with open(file, 'r') as f:
        data = f.readlines()
    return data


if __name__ == "__main__":
    import pytest
    import sys
    sys.exit(pytest.main(['-v', './2025/DAY/AoC_2025_DAY_test.py']))
