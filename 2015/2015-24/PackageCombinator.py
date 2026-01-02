from itertools import combinations
from PackageGroup import PackageGroup


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
