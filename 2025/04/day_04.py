'''
Advent of Code 2025 - Day 4: Printing Department
Puzzle: https://adventofcode.com/2025/day/4
'''

ROLL = '@'
LIMIT = 4


def day_04(file: str, limit: int = LIMIT) -> int:
    with open(file, 'r') as f:
        diagram = [[c for c in line.strip()] for line in f]
        part1 = 0
        for row in range(len(diagram)):
            for col in range(len(diagram[0])):
                if diagram[row][col] == ROLL and get_adjacent_rolls(diagram, row, col) < limit:
                    part1 += 1
        # for row in diagram:
        #     print(row)
    return part1


def get_adjacent_rolls(diagram: list[list[str]], row: int, col: int, char: str = ROLL) -> int:
    count: int = 0
    rows = len(diagram)
    cols = len(diagram[0])

    try_row, try_col = row-1, col-1
    if 0 <= try_row <= rows and 0 <= try_col <= cols:
        try:
            count += 1 if diagram[try_row][try_col] == char else 0
        except IndexError:
            pass

    try_row, try_col = row-1, col
    if 0 <= try_row <= rows and 0 <= try_col <= cols:
        try:
            count += 1 if diagram[try_row][try_col] == char else 0
        except IndexError:
            pass

    try_row, try_col = row-1, col+1
    if 0 <= try_row <= rows and 0 <= try_col <= cols:
        try:
            count += 1 if diagram[try_row][try_col] == char else 0
        except IndexError:
            pass

    try_row, try_col = row, col-1
    if 0 <= try_row <= rows and 0 <= try_col <= cols:
        try:
            count += 1 if diagram[try_row][try_col] == char else 0
        except IndexError:
            pass

    try_row, try_col = row, col+1
    if 0 <= try_row <= rows and 0 <= try_col <= cols:
        try:
            count += 1 if diagram[try_row][try_col] == char else 0
        except IndexError:
            pass

    try_row, try_col = row+1, col-1
    if 0 <= try_row <= rows and 0 <= try_col <= cols:
        try:
            count += 1 if diagram[try_row][try_col] == char else 0
        except IndexError:
            pass

    try_row, try_col = row+1, col
    if 0 <= try_row <= rows and 0 <= try_col <= cols:
        try:
            count += 1 if diagram[try_row][try_col] == char else 0
        except IndexError:
            pass

    try_row, try_col = row+1, col+1
    if 0 <= try_row <= rows and 0 <= try_col <= cols:
        try:
            count += 1 if diagram[try_row][try_col] == char else 0
        except IndexError:
            pass

    return count


if __name__ == "__main__":
    import pytest
    import sys
    sys.exit(pytest.main(['-v', './2025/04/day_04_test.py']))
