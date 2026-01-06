'''
Advent of Code 2016 - Day 7: Internet Protocol Version 7
Puzzle: https://adventofcode.com/2016/day/7
'''
from IPv7Address import IPv7Address


###############################################################################
# region Solve
def solve(filename: str) -> tuple[int, int]:
    addresses: list[IPv7Address] = get_data(filename)
    return solve_part1(addresses), solve_part2(addresses)


def solve_part1(addresses: list[IPv7Address]) -> int:
    return sum(address.supports_TLS for address in addresses)


def solve_part2(addresses: list[IPv7Address]) -> int:
    return sum(address.supports_SSL for address in addresses)


def get_data(filename: str) -> list[IPv7Address]:
    with open(filename, 'r') as file:
        return [IPv7Address(line.strip()) for line in file]
# endregion
###############################################################################


###############################################################################
# region Main
if __name__ == "__main__":
    filepaths = [
        './2016/2016-07/example1.txt',
        './2016/2016-07/example2.txt',
        './2016/2016-07/input.txt',
    ]

    for filepath in filepaths:
        part_1, part_2 = solve(filepath)
        print(f"{filepath=}: Results: {part_1=}, {part_2=}")
# endregion
###############################################################################
