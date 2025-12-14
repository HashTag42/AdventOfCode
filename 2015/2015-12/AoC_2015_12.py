'''
Advent of Code 2015 - Day 12: JSAbacusFramework.io
Puzzle: https://adventofcode.com/2015/day/12
'''
from pathlib import Path
import re


def solve_2015_12(filename: Path) -> tuple[int, int]:
    data = get_data(filename)
    return solve_part1(data), solve_part2(data)


def solve_part1(data) -> int:
    matches = re.findall(r"-?\d+", data)
    return sum(int(match) for match in matches)


def solve_part2(data) -> int:
    result = 0
    return result


def get_data(filename: Path) -> str:
    with open(filename, 'r') as f:
        data = f.read()
    return data


if __name__ == "__main__":
    import pytest
    import sys
    sys.exit(pytest.main(['-v', './2015/2015-12/AoC_2015_12_test.py']))
