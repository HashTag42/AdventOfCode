'''
Advent of Code 2016 - Day 04: Security Through Obscurity
Puzzle: https://adventofcode.com/2016/day/04
'''
from Room import Room
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s: %(message)s",
    )

NORTH_POLE_ROOM_NAME = 'northpole object storage'


def solve(filename: str) -> tuple[int, int]:
    rooms = get_data(filename)
    return solve_part1(rooms), solve_part2(rooms)


def solve_part1(rooms: list[Room]) -> int:
    return sum(room.sector_id for room in rooms if room.is_real)


def solve_part2(rooms: list[Room]) -> int:
    for room in rooms:
        if room.decrypted_name == NORTH_POLE_ROOM_NAME:
            return room.sector_id
    return -1


def get_data(filename: str) -> list[Room]:
    with open(filename, 'r') as file:
        return [Room(line.strip()) for line in file]


if __name__ == "__main__":
    result1, result2 = solve('./2016/2016-04/example.txt')
    print(f"example.txt: Results: Part 1 = {result1}, Part 2 = {result2}")

    result1, result2 = solve('./2016/2016-04/input.txt')
    print(f"input.txt: Results: Part 1 = {result1}, Part 2 = {result2}")
