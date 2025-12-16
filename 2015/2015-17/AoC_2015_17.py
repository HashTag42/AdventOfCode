'''
Advent of Code 2015 - Day 17: No Such Thing as Too Much
Puzzle: https://adventofcode.com/2015/day/17
'''
from itertools import combinations

EGGNOG = 150


def solve_2015_17(filename: str) -> tuple[int, int]:
    containers = get_data(filename)
    return solve_part1(containers), solve_part2(containers)


def solve_part1(containers) -> int:
    total = 0
    for i in range(len(containers)):
        subtotal = 0
        for combination in combinations(containers, i):
            if sum(combination) == 150:
                subtotal += 1
        total += subtotal
    return total


def solve_part2(data) -> int:
    result = 0
    return result


def get_data(filename: str) -> list[int]:
    containers: list[int] = []
    with open(filename, 'r') as file:
        for line in file.readlines():
            containers.append(int(line))
        return sorted(containers)


if __name__ == "__main__":
    import pytest
    import sys
    sys.exit(pytest.main(['-v', './2015/2015-17/AoC_2015_17_test.py']))
