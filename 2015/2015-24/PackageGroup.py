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
