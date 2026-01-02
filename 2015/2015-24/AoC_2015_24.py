'''
Advent of Code 2015 - Day 24: It Hangs in the Balance
Puzzle: https://adventofcode.com/2015/day/24
'''
from PackageCombinator import PackageCombinator


################################################################################
# region Solve
def solve(filename: str) -> tuple[int, int]:
    packages = get_data(filename)
    return solve_part1(packages), solve_part2(packages)


def solve_part1(packages: list[int]) -> int:
    return PackageCombinator(packages, groups=3).get_first_group_qe()


def solve_part2(packages: list[int]) -> int:
    return PackageCombinator(packages, groups=4).get_first_group_qe()


def get_data(filename: str) -> list[int]:
    packages: list[int] = []
    with open(filename, 'r') as file:
        for line in file.readlines():
            packages.append(int(line))
    return packages
# endregion
################################################################################


################################################################################
# region Main
if __name__ == "__main__":
    result1, result2 = solve('./2015/2015-24/example.txt')
    print(f"example.txt results: Part 1 = {result1}, Part 2 = {result2}")

    result1, result2 = solve('./2015/2015-24/input.txt')
    print(f"input.txt results: Part 1 = {result1}, Part 2 = {result2}")
# endregion
################################################################################
