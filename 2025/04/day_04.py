'''
Advent of Code 2025 - Day 4: Printing Department
Puzzle: https://adventofcode.com/2025/day/4
'''

ROLL = '@'
LIMIT = 4


def day_04(file: str, limit: int = LIMIT) -> tuple[int, int]:
    with open(file, 'r') as f:
        diagram = [[c for c in line.strip()] for line in f]
    return part1(diagram)[0], part2(diagram)


def part1(in_diagram: list[list[str]], limit: int = LIMIT) -> tuple[int, list[list[str]]]:
    count = 0
    out_diagram = [row[:] for row in in_diagram]
    for row in range(len(in_diagram)):
        for col in range(len(in_diagram[0])):
            if in_diagram[row][col] == ROLL and get_adjacent_rolls(in_diagram, row, col) < limit:
                count += 1
                out_diagram[row][col] = 'x'
    return count, out_diagram


def part2(in_diagram: list[list[str]]) -> int:
    count = 0
    while True:
        count1, out_diagram = part1(in_diagram)
        if count1 == 0:
            break
        count += count1
        in_diagram = [row[:] for row in out_diagram]
    return count


def get_adjacent_rolls(diagram: list[list[str]], row: int, col: int, char: str = ROLL) -> int:
    count: int = 0
    rows = len(diagram)
    cols = len(diagram[0])
    neighbors = [(-1, -1), (-1, 0), (-1, +1), (0, -1), (0, +1), (+1, -1), (+1, 0), (+1, +1)]
    for n in neighbors:
        try_row, try_col = row + n[0], col + n[1]
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
