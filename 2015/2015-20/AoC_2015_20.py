'''
Advent of Code 2015 - Day 20 Infinite Elves and Infinite Houses:
Puzzle: https://adventofcode.com/2015/day/20
'''


def solve(target, multiplier=10, max_visits=None) -> int:
    limit = target // 10
    presents = [0] * (limit + 1)
    for elf in range(1, limit + 1):
        max_house = limit if max_visits is None else min(max_visits * elf, limit)
        for house in range(elf, max_house + 1, elf):
            presents[house] += elf * multiplier
    for house in range(1, limit + 1):
        if presents[house] >= target:
            return house
    return -1


def solve_part1(target) -> int:
    return solve(target, multiplier=10)


def solve_part2(target) -> int:
    return solve(target, multiplier=11, max_visits=50)


if __name__ == "__main__":
    import pytest
    import sys
    sys.exit(pytest.main(['-v', './2015/2015-20/AoC_2015_20_test.py']))
