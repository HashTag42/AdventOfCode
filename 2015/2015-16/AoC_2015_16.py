'''
Advent of Code 2015 - Day 16: Aunt Sue
Puzzle: https://adventofcode.com/2015/day/16
'''
from Sue import Sue


def solve_2015_16(filename: str) -> tuple[int, int]:
    sues: list[Sue] = get_data(filename)
    return solve_part1(sues), solve_part2(sues)


the_sue = Sue()
the_sue.update_category("children", 3)
the_sue.update_category("cats", 7)
the_sue.update_category("samoyeds", 2)
the_sue.update_category("pomeranians", 3)
the_sue.update_category("akitas", 0)
the_sue.update_category("vizslas", 0)
the_sue.update_category("goldfish", 5)
the_sue.update_category("trees", 3)
the_sue.update_category("cars", 2)
the_sue.update_category("perfumes", 1)


def solve_part1(sues: list[Sue]) -> int:
    for s in sues:
        if s.compare1(the_sue) == 3:
            return s.id
    return -1


def solve_part2(sues) -> int:
    for s in sues:
        if s.compare2(the_sue) == 3:
            return s.id
    return -1


def get_data(filename: str) -> list[Sue]:
    with open(filename, 'r') as file:
        return [Sue(line) for line in file]


if __name__ == "__main__":
    import pytest
    import sys
    sys.exit(pytest.main(['-v', './2015/2015-16/AoC_2015_16_test.py']))
