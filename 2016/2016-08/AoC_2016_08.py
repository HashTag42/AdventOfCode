'''
Advent of Code 2016 - Day 8: Two-Factor Authentication
Puzzle: https://adventofcode.com/2016/day/8
'''
from Screen import Screen, State
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    )


def solve_part1(operations: list[str], cols: int, rows: int) -> int:
    screen = Screen(cols, rows)
    logging.debug(screen)
    for op in operations:
        logging.debug(f"{op=}")
        screen.execute(op)
        logging.debug(screen)
    logging.info(screen)
    return screen.count(State.ON)


def get_data(filename: str) -> list[str]:
    return Path(filename).read_text().splitlines()


if __name__ == "__main__":
    filename, cols, rows = './2016/2016-08/example.txt', 7, 3
    result1 = solve_part1(get_data(filename), cols, rows)
    print(f"{filename=}: {result1=}")

    filename, cols, rows = './2016/2016-08/input.txt', 50, 6
    result1 = solve_part1(get_data(filename), cols, rows)
    print(f"{filename=}: {result1=}")
