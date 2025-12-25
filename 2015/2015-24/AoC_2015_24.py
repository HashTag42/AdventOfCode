'''
Advent of Code 2015 - Day 24: It Hangs in the Balance
Puzzle: https://adventofcode.com/2015/day/24
'''
from itertools import combinations


################################################################################
# region PackageGroup
class PackageGroup:
    def __init__(self, packages: list[int]) -> None:
        self.__packages: dict[int, int] = {}
        for package in packages:
            self.__packages[package] = 0
        self.__qe: int = self.__calculate_qe()
        self.__weight: int = sum(self.__packages)

    def get_group_weight(self) -> int:
        return self.__weight

    def get_packages(self) -> dict[int, int]:
        return self.__packages

    def get_qe(self) -> int:
        return self.__qe

    def get_weight(self) -> int:
        return self.__weight

    def __calculate_qe(self) -> int:
        qe = 1
        for package in self.__packages:
            qe *= package
        return qe

    def __len__(self) -> int:
        return len(self.__packages)

    def __repr__(self) -> str:
        return (
            f"<PackageGroup: Packages={len(self.__packages)}, "
            f"QE={self.get_qe()}, "
            f"Group weight={self.get_group_weight()}>"
        )
# endregion
################################################################################


################################################################################
# region Sleigh
class Sleigh:
    def __init__(self, groups: tuple[PackageGroup, PackageGroup, PackageGroup]) -> None:
        self.__groups: tuple[PackageGroup, PackageGroup, PackageGroup] = groups
# endregion
################################################################################


################################################################################
# region PackageCombinator
class PackageCombinator:
    def __init__(self, packages: list[int], groups: int) -> None:
        self.__all_packages_group: PackageGroup = PackageGroup(packages)
        self.__groups: int = groups

    def get_first_group_qe(self) -> int:
        # Calculate the target weight
        target_weight = self.__all_packages_group.get_group_weight() // self.__groups
        # print(f"[DEBUG] {target_weight=}")

        # Create all possible combinations and filter only those that produce package groups of equal weight
        valid_combinations = []
        for r in range(1, len(self.__all_packages_group.get_packages())):
            valid_combinations = [
                c for c in combinations(self.__all_packages_group.get_packages(), r)
                if sum(p for p in c) == target_weight
            ]
            # for each of those combinations, identify the package group(s) with fewest packages
            if len(valid_combinations) > 0:
                break
        # print(f"[DEBUG] {len(valid_combinations)=}")
        # print(f"[DEBUG] {valid_combinations=}")

        # if there are several combination with the same number of fewest packages:
        # find the combination with the smallest qe from their group with fewest packages
        qes: list[int] = []
        for combo in valid_combinations:
            qes.append(PackageGroup(list(combo)).get_qe())

        return min(qes)
# endregion
################################################################################


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
