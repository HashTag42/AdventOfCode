'''
Advent of Code YEAR - Day DAY:
Puzzle: https://adventofcode.com/YEAR/day/DAY
'''
from pathlib import Path


def solve(filename: str) -> tuple[int, int]:
    lines = get_data(filename)
    return solve_part1(lines), solve_part2(lines)


def solve_part1(lines: list[str]) -> int:
    result = 0
    return result


def solve_part2(lines: list[str]) -> int:
    result = 0
    return result


def get_data(filename: str) -> list[str]:
    return Path(filename).read_text().splitlines()


if __name__ == "__main__":
    input_files = [
        './YEAR/FOLDER/example.txt',
        './YEAR/FOLDER/input.txt',
    ]
    for input_file in input_files:
        result1, result2 = solve(input_file)
        print(f"{input_file=}: Results: {result1=}, {result2=}")
