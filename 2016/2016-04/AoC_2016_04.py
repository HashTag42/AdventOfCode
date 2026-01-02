'''
Advent of Code 2016 - Day 04: Security Through Obscurity
Puzzle: https://adventofcode.com/2016/day/04
'''
import re
from collections import Counter
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s: %(message)s",
    )


class Room:
    def __init__(self, room: str) -> None:
        self.full_name: str = room
        self.encrypted_name, self.sector_id, self.checksum = self._parse_full_name()
        self.is_real: bool = self._is_real()

    def _parse_full_name(self) -> tuple[str, int, str]:
        match = re.match(r'(.+)-(\d+)\[(\w+)\]', self.full_name)
        if match:
            encrypted_name, sector_id, checksum = match.groups()
        else:
            raise ValueError(f"Invalid room: {self.full_name}")
        return encrypted_name, int(sector_id), checksum

    def _is_real(self) -> bool:
        counter = Counter(c for c in self.encrypted_name if c.isalpha())
        sorted_chars = sorted(counter.items(), key=lambda item: (-item[1], item[0]))
        top_5 = ''.join(char for char, count in sorted_chars[:5])
        return top_5 == self.checksum


def solve(filename: str) -> tuple[int, int]:
    rooms = get_data(filename)
    return solve_part1(rooms), solve_part2(rooms)


def solve_part1(rooms: list[Room]) -> int:
    return sum(room.sector_id for room in rooms if room.is_real)


def solve_part2(rooms: list[Room]) -> int:
    result = 0
    return result


def get_data(filename: str) -> list[Room]:
    with open(filename, 'r') as file:
        return [Room(line.strip()) for line in file]


if __name__ == "__main__":
    result1, result2 = solve('./2016/2016-04/example.txt')
    print(f"example.txt: Results: Part 1 = {result1}, Part 2 = {result2}")

    result1, result2 = solve('./2016/2016-04/input.txt')
    print(f"input.txt: Results: Part 1 = {result1}, Part 2 = {result2}")
