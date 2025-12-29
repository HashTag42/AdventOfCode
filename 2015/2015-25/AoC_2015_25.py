'''
Advent of Code 2015 - Day 25: Let It Snow
Puzzle: https://adventofcode.com/2015/day/25
'''
from typing import Final
import re

START: Final[int] = 20151125
MUL_FACTOR: Final[int] = 252533
DIV_FACTOR: Final[int] = 33554393


def get_code(num: int) -> int:
    current: int = START
    for _ in range(1, num):
        current *= MUL_FACTOR
        quotient, current = divmod(current, DIV_FACTOR)
    return current


def get_num(row: int, col: int) -> int:
    return int((row + col - 1) * (row + col - 2) / 2 + col)


def solve(filename: str) -> tuple[int, int]:
    row, col = get_data(filename)
    return solve_part1(row, col), solve_part2(row, col)


def solve_part1(row: int, col: int) -> int:
    return get_code(get_num(row, col))


def solve_part2(row: int, col: int) -> int:
    result = 0
    return result


def get_data(filename: str) -> tuple[int, int]:
    with open(filename, 'r') as file:
        match = re.search(r'row (\d+), column (\d+)', file.read())
        if match:
            return (int(match.group(1)), int(match.group(2)))
        else:
            return (0, 0)


if __name__ == "__main__":
    part1, part2 = solve('./2015/2015-25/input.txt')
    print(f"example.txt: Results: {part1=}, {part2=}")
