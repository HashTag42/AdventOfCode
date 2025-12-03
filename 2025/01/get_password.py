'''
Advent of Code 2025 - Day 1: Secret Entrance
Puzzle: https://adventofcode.com/2025/day/1
'''
from Dial import Dial


def get_password(filename: str):
    dial = Dial()
    part1 = part2 = 0
    # Rotate the dial according to the rotations defined in the input file
    with open(filename, 'r') as input:
        for rotation in input.readlines():
            position, clicks = dial.rotate(rotation)
            part1 += 1 if position == 0 else 0
            part2 += clicks
    return part1, part2
