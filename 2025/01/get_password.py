'''
Advent of Code 2025 - Day 1: Secret Entrance
Puzzle: https://adventofcode.com/2025/day/1
'''
from Dial import Dial

input0 = './2025/01/input0.txt'
input = './2025/01/input.txt'


def get_password(filename: str):
    dial = Dial()
    zero_count = 0
    # Rotate the dial according to the rotations defined in the input file
    with open(filename, 'r') as input:
        for rotation in input.readlines():
            position = dial.rotate(rotation)
            # print("[DEBUG]", position)
            if position == 0:
                zero_count += 1
    return zero_count
