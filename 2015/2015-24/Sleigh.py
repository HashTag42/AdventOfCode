from PackageGroup import PackageGroup


################################################################################
# region Sleigh
class Sleigh:
    def __init__(self, groups: tuple[PackageGroup, PackageGroup, PackageGroup]) -> None:
        self.__groups: tuple[PackageGroup, PackageGroup, PackageGroup] = groups
# endregion
################################################################################
