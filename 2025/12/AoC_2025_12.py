'''
Advent of Code 2025 - Day 12: Christmas Tree Farm
Puzzle: https://adventofcode.com/2025/day/12
'''


def solve_2025_12(file: str) -> tuple[int, int]:
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
    sys.exit(pytest.main(['-v', './2025/12/AoC_2025_12_test.py']))
