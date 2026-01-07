'''
Advent of Code 2016 - Day 8: Two-Factor Authentication
Puzzle: https://adventofcode.com/2016/day/8
'''
from Screen import Screen, State
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    )


def solve(filename: str, cols: int, rows: int) -> tuple[int, int]:
    operations = get_data(filename)
    return (
        solve_part1(operations, cols, rows),
        solve_part2(operations, cols, rows)
        )


def solve_part1(operations: list[str], cols: int, rows: int) -> int:
    screen = Screen(cols, rows)
    logging.debug(screen)
    for op in operations:
        logging.debug(f"{op=}")
        screen.execute(op)
        logging.debug(screen)
    return screen.count(State.ON.value)


def solve_part2(operations: list[str], cols: int, rows: int) -> int:
    result = 0
    return result


def get_data(filename: str) -> list[str]:
    with open(filename, 'r') as file:
        return [line.strip() for line in file]


if __name__ == "__main__":
    input_file, cols, rows = './2016/2016-08/example.txt', 7, 3
    result1, result2 = solve(input_file, cols, rows)
    print(f"{input_file=}: {result1=}, {result2=}")

    input_file, cols, rows = './2016/2016-08/input.txt', 50, 6
    result1, result2 = solve(input_file, cols, rows)
    print(f"{input_file=}: {result1=}, {result2=}")
