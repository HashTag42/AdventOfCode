'''
Advent of Code 2016 - Day 7: Internet Protocol Version 7
Puzzle: https://adventofcode.com/2016/day/7
'''
import re


###############################################################################
# region Segment
class Segment:
    def __init__(self, segment: str) -> None:
        if segment.startswith('['):
            self.segment = segment[1:-1]
            self.is_hypernet = True
        else:
            self.segment = segment
            self.is_hypernet = False
        self.has_ABBA: bool = self._has_ABBA()
        self.ABAs: list[str] = self._get_ABAs()

    def _get_ABAs(self) -> list[str]:
        length = len(self.segment)
        if length < 3:
            return []
        return [
            self.segment[i:i + 3]
            for i in range(length - 2)
            if self._is_ABA(self.segment[i:i + 3])
        ]

    def _has_ABBA(self) -> bool:
        length = len(self.segment)
        if length < 4:
            return False
        return any(
            self._is_ABBA(self.segment[i:i + 4])
            for i in range(length - 3)
        )

    def _is_ABA(self, s: str) -> bool:
        return s[0] == s[2] and s[0] != s[1]

    def _is_ABBA(self, s: str) -> bool:
        return s[0] != s[1] and s == s[::-1]

    def __repr__(self) -> str:
        return f'{self.segment}, {self.is_hypernet=}, {self.has_ABBA=}'
# endregion
###############################################################################


###############################################################################
# region Address
class Address:
    def __init__(self, address: str) -> None:
        self.address: str = address
        self.segments: list[Segment] = self._get_segments()
        self.supports_SSL: bool = self._supports_SSL()
        self.supports_TLS: bool = self._supports_TLS()

    def _get_segments(self) -> list[Segment]:
        # Split but keep the delimiters (bracketed parts)
        parts = re.split(r'(\[[a-z]+\])', self.address)
        return [Segment(part) for part in parts if part]

    def _supports_SSL(self) -> bool:
        supernet_ABAs = [
            aba for seg in self.segments if not seg.is_hypernet for aba in seg.ABAs
        ]
        hypernet_ABAs = {
            aba for seg in self.segments if seg.is_hypernet for aba in seg.ABAs
        }
        return any(aba[1] + aba[0] + aba[1] in hypernet_ABAs for aba in supernet_ABAs)

    def _supports_TLS(self) -> bool:
        has_abba_in_supernet = any(
            seg.has_ABBA for seg in self.segments if not seg.is_hypernet
        )
        has_abba_in_hypernet = any(
            seg.has_ABBA for seg in self.segments if seg.is_hypernet
        )
        return has_abba_in_supernet and not has_abba_in_hypernet

    def __repr__(self) -> str:
        return f'{self.address}, {self.supports_TLS=}, {self.supports_SSL=}'
# endregion
###############################################################################


###############################################################################
# region Solve
def solve(filename: str) -> tuple[int, int]:
    addresses: list[Address] = get_data(filename)
    return solve_part1(addresses), solve_part2(addresses)


def solve_part1(addresses: list[Address]) -> int:
    return sum(address.supports_TLS for address in addresses)


def solve_part2(addresses: list[Address]) -> int:
    return sum(address.supports_SSL for address in addresses)


def get_data(filename: str) -> list[Address]:
    with open(filename, 'r') as file:
        return [Address(line.strip()) for line in file]
# endregion
###############################################################################


###############################################################################
# region Main
if __name__ == "__main__":
    filepaths: list[str] = [
        './2016/2016-07/example1.txt',
        './2016/2016-07/example2.txt',
        './2016/2016-07/input.txt',
    ]

    for filepath in filepaths:
        part_1, part_2 = solve(filepath)
        print(f"{filepath=}: Results: {part_1=}, {part_2=}")
# endregion
###############################################################################
