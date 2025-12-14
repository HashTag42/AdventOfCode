'''
Advent of Code YEAR - Day DAY:
Puzzle: https://adventofcode.com/YEAR/day/DAY
'''
from pathlib import Path


def solve_YEAR_DAY(filename: Path) -> tuple[int, int]:
    data = get_data(filename)
    return solve_part1(data), solve_part2(data)


def solve_part1(data) -> int:
    result = 0
    return result


def solve_part2(data) -> int:
    result = 0
    return result


def get_data(filename: Path) -> list[str]:
    with open(filename, 'r') as f:
        data = f.readlines()
    return data


if __name__ == "__main__":
    import pytest
    import sys
    sys.exit(pytest.main(['-v', './YEAR/DAY/YEAR_DAY_test.py']))
