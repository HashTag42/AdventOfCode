'''
Advent of Code 2025 - Day 6:
Puzzle: https://adventofcode.com/2025/day/6
'''


def solve_2025_06(file: str) -> tuple[int, int]:
    data = get_data(file)
    return solve_part1(data), solve_part2(data)


def solve_part1(data) -> int:
    count, rows, cols = 0, len(data), len(data[0])
    for c in range(cols):
        operand = data[rows - 1][c]
        if operand == '+':
            result = 0
            for r in range(rows - 1):
                result += int(data[r][c])
        else:   # operand == '*'
            result = 1
            for r in range(rows - 1):
                result *= int(data[r][c])
        count += result
    return count


def solve_part2(data) -> int:
    count, rows, cols = 0, len(data), len(data[0])
    for c in range(cols):
        operand = data[rows - 1][c]
        if operand == '+':
            result = 0
            pass
        else:   # operand == '*'
            result = 1
            pass
        count += result
    return count


def get_data(file: str) -> list[list[int]]:
    data = []
    with open(file, 'r') as f:
        for line in f.readlines():
            numbers = line.split()
            data.append(numbers)
    return data


if __name__ == "__main__":
    import pytest
    import sys
    sys.exit(pytest.main(['-v', './2025/06/day_2025_06_test.py']))
