'''
Advent of Code 2015 - Day 12: JSAbacusFramework.io
Puzzle: https://adventofcode.com/2015/day/12
'''
from pathlib import Path
import json
import re


def solve_2015_12(filename: Path) -> tuple[int, int]:
    data, json_data = get_data(filename)
    return solve_part1(data), solve_part2(json_data)


def solve_part1(data) -> int:
    matches = re.findall(r"-?\d+", data)
    return sum(int(match) for match in matches)


def solve_part2(json_data) -> int:
    if isinstance(json_data, int):
        return json_data
    elif isinstance(json_data, dict):
        # Skip entire object if any value is "red"
        if "red" in json_data.values():
            return 0
        return sum(solve_part2(v) for v in json_data.values())
    elif isinstance(json_data, list):
        return sum(solve_part2(item) for item in json_data)
    return 0  # strings and other types


def get_data(filename: Path) -> tuple[str, str]:
    with open(filename, 'r') as file:
        data = file.read()
    with open(filename, 'r') as file:
        json_data = json.load(file)
    return data, json_data


if __name__ == "__main__":
    import pytest
    import sys
    sys.exit(pytest.main(['-v', './2015/2015-12/AoC_2015_12_test.py']))
