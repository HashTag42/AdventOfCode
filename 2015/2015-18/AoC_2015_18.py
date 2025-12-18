'''
Advent of Code 2015 - Day 18: Like a GIF For Your Yard
Puzzle: https://adventofcode.com/2015/day/18
'''

ON = '#'
OFF = '.'
NEIGHBORS = [(-1, -1), (-1, 0), (-1, +1), (0, -1), (0, +1), (+1, -1), (+1, 0), (+1, +1)]


def solve_part1(matrix: list[list[str]], steps: int) -> int:
    for _ in range(steps):
        matrix = update_matrix(matrix)
    return count_lights(matrix, ON)


def update_matrix(matrix: list[list[str]]) -> list[list[str]]:
    matrix_copy = [row[:] for row in matrix]
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            on_count = count_neighbors(matrix, row, col, ON)
            if matrix[row][col] == ON and on_count not in (2, 3):
                matrix_copy[row][col] = OFF
            elif matrix[row][col] == OFF and on_count == 3:
                matrix_copy[row][col] = ON
    return matrix_copy


def count_neighbors(matrix: list[list[str]], row: int, col: int, find_char: str = ON) -> int:
    count = 0
    rows = len(matrix)
    cols = len(matrix[0])
    for dr, dc in NEIGHBORS:
        try_row, try_col = row + dr, col + dc
        if 0 <= try_row <= rows and 0 <= try_col <= cols:
            try:
                count += 1 if matrix[try_row][try_col] == find_char else 0
            except IndexError:
                pass
    return count


def count_lights(matrix: list[list[str]], find_char: str = ON) -> int:
    return sum(cell == find_char for row in matrix for cell in row)


def display_matrix(matrix: list[list[str]]) -> str:
    output = ""
    for row in matrix:
        output += ' '.join(map(str, row)) + '\n'
    return output


def solve_part2(matrix: list[list[str]]) -> int:
    result = 0
    return result


def get_data(filename: str) -> list[list[str]]:
    with open(filename, 'r') as file:
        matrix: list[list[str]] = [[c for c in line.strip()] for line in file]
    return matrix


if __name__ == "__main__":
    import pytest
    import sys
    sys.exit(pytest.main(['-v', './2015/2015-18/AoC_2015_18_test.py']))
