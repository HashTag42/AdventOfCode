'''
Advent of Code 2016 - Day 7: Internet Protocol Version 7
Puzzle: https://adventofcode.com/2016/day/7
'''


###############################################################################
# region Segment
class Segment():
    def __init__(self, segment: str) -> None:
        self.segment: str = segment
        self.is_hypernet: bool = self._is_hypernet()
        self.has_ABBA: bool = self._has_ABBA()
        self.ABAs: list[str] = self._get_ABAs()
        self.has_ABA: bool = len(self.ABAs) > 0

    def _is_hypernet(self) -> bool:
        if self.segment[0] == '[':
            # remove square brackets
            self.segment = self.segment[1:-1]
            return True
        return False

    def _get_ABAs(self) -> list[str]:
        ABAs: list[str] = []
        length: int = len(self.segment)
        if len(self.segment) >= 3:
            for i in range(length - 3 + 1):
                string: str = self.segment[i: i + 3]
                if self._is_string_ABA(string):
                    ABAs.append(string)
        return ABAs

    def _has_ABBA(self) -> bool:
        length: int = len(self.segment)
        if len(self.segment) < 4:
            return False
        for i in range(length - 4 + 1):
            string: str = self.segment[i: i + 4]
            if self._is_string_ABBA(string):
                return True
        return False

    def _is_string_ABA(self, string: str) -> bool:
        return string[0] == string[2] and string[0] != string[1]

    def _is_string_ABBA(self, string: str) -> bool:
        return string[0] != string[1] and string[0] == string[3] and string[1] == string[2]

    def __repr__(self) -> str:
        return f'{self.segment}, {self.is_hypernet=}, {self.has_ABBA=}'
# endregion
###############################################################################


###############################################################################
# region Address
class Address():
    def __init__(self, address: str) -> None:
        self.address: str = address
        self.segments: list[Segment] = self._get_segments()
        self.supports_SSL: bool = self._supports_SSL()
        self.supports_TLS: bool = self._supports_TLS()

    def _get_segments(self) -> list[Segment]:
        segments: list[Segment] = []
        current: str = ''
        for c in self.address:
            if c == '[':
                segments.append(Segment(current))
                current = c
            elif c == ']':
                segments.append(Segment(current + c))
                current = ''
            else:
                current += c
        if len(current) > 0:
            segments.append(Segment(current))
        return segments

    def _supports_SSL(self) -> bool:
        ABA, BAB = '', ''
        for segment in self.segments:
            if not segment.is_hypernet and segment.has_ABA:
                for ABA in segment.ABAs:
                    for segment in self.segments:
                        if segment.is_hypernet and segment.has_ABA:
                            for BAB in segment.ABAs:
                                if ABA[0] == BAB[1] and ABA[1] == BAB[0]:
                                    return True
        return False

    def _supports_TLS(self) -> bool:
        valid_ABBA: bool = False
        for segment in self.segments:
            if segment.is_hypernet and segment.has_ABBA:
                return False
            if not segment.is_hypernet and segment.has_ABBA:
                valid_ABBA = True
        return valid_ABBA

    def __repr__(self) -> str:
        return f'{self.address}, ({self.supports_TLS=}, {self.supports_SSL=})'
# endregion
###############################################################################


###############################################################################
# region Solve
def solve(filename: str) -> tuple[int, int]:
    addresses: list[Address] = get_data(filename)
    return solve_part1(addresses), solve_part2(addresses)


def solve_part1(addresses: list[Address]) -> int:
    return sum(1 for address in addresses if address.supports_TLS)


def solve_part2(addresses: list[Address]) -> int:
    return sum(1 for address in addresses if address.supports_SSL)


def get_data(filename: str) -> list[Address]:
    addresses: list[Address] = []
    with open(filename, 'r') as file:
        for line in file.readlines():
            if line[0] != '#':
                addresses.append(Address(line.strip()))
        return addresses
# endregion
###############################################################################


###############################################################################
# region Main
if __name__ == "__main__":

    input_files: list[str] = [
        './2016/2016-07/example1.txt',
        './2016/2016-07/example2.txt',
        './2016/2016-07/input.txt',
    ]

    for file in input_files:
        part_1, part_2 = solve(file)
        print(f"{file=}: Results: {part_1=}, {part_2=}")
# endregion
###############################################################################
