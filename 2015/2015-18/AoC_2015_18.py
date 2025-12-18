'''
Advent of Code 2015 - Day 18: Like a GIF For Your Yard
Puzzle: https://adventofcode.com/2015/day/18
'''

ON = '#'
OFF = '.'
NEIGHBORS = [(-1, -1), (-1, 0), (-1, +1), (0, -1), (0, +1), (+1, -1), (+1, 0), (+1, +1)]


def solve_part1(matrix: list[list[str]], steps: int) -> int:
    for _ in range(steps):
        matrix = update_matrix1(matrix)
    return count_lights(matrix, ON)


def solve_part2(matrix: list[list[str]], steps: int) -> int:
    matrix = set_corners_on(matrix)
    for _ in range(steps):
        matrix = update_matrix2(matrix)
    return count_lights(matrix, ON)


def update_matrix1(matrix: list[list[str]]) -> list[list[str]]:
    matrix_copy = [row[:] for row in matrix]
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            on_count = count_neighbors(matrix, row, col, ON)
            if matrix[row][col] == ON and on_count not in (2, 3):
                matrix_copy[row][col] = OFF
            elif matrix[row][col] == OFF and on_count == 3:
                matrix_copy[row][col] = ON
    return matrix_copy


def set_corners_on(matrix: list[list[str]]) -> list[list[str]]:
    rows, cols = len(matrix), len(matrix[0])
    matrix[0][0] = ON
    matrix[0][cols - 1] = ON
    matrix[rows - 1][0] = ON
    matrix[rows - 1][cols - 1] = ON
    return matrix


def update_matrix2(matrix: list[list[str]]) -> list[list[str]]:
    matrix_copy = [row[:] for row in matrix]
    rows, cols = len(matrix), len(matrix[0])
    corners = {(0, 0), (0, cols - 1), (rows - 1, 0), (rows - 1, cols - 1)}
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if (row, col) not in corners:
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
        if 0 <= try_row < rows and 0 <= try_col < cols:
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


def get_data(filename: str) -> list[list[str]]:
    with open(filename, 'r') as file:
        matrix: list[list[str]] = [[c for c in line.strip()] for line in file]
    return matrix


if __name__ == "__main__":
    import pytest
    import sys
    sys.exit(pytest.main(['-v', './2015/2015-18/AoC_2015_18_test.py']))
