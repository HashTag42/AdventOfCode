'''
Advent of Code 2025 - Day 6: Trash Compactor
Puzzle: https://adventofcode.com/2025/day/6
'''


def solve_2025_06(file: str) -> tuple[int, int]:
    data1, data2 = get_data(file)
    return solve_part1(data1), solve_part2(data2)


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


def solve_part2(lines) -> int:
    """
    Solves cephalopod math puzzles where:
    - Numbers are written vertically (top to bottom) in columns
    - Problems are read right to left
    - Columns of spaces separate problems
    - The bottom row contains the operator
    """
    # Pad all lines to the same width
    max_width = max(len(line) for line in lines)
    lines = [line.ljust(max_width) for line in lines]
    # Separate operator row from number rows
    number_rows = lines[:-1]
    operator_row = lines[-1]
    results = []
    numbers = []
    operator = None
    # Process columns from right to left
    for col_idx in range(max_width - 1, -1, -1):
        # Read column vertically (top to bottom)
        column = ''.join(row[col_idx] for row in number_rows)
        op = operator_row[col_idx]
        # Check if this is a separator column (all spaces)
        if column.strip() == '':
            # End of problem - calculate result
            if numbers:
                if operator == '+':
                    result = sum(numbers)
                else:  # operator == '*'
                    result = 1
                    for num in numbers:
                        result *= num
                results.append(result)
                numbers = []
                operator = None
        else:
            # Part of current problem
            numbers.append(int(column.strip()))
            if op.strip():
                operator = op.strip()
    # Don't forget the last problem
    if numbers:
        if operator == '+':
            result = sum(numbers)
        else:  # operator == '*'
            result = 1
            for num in numbers:
                result *= num
        results.append(result)
    return sum(results)


def get_data(file: str) -> tuple[list[list[int]], list[str]]:
    with open(file, 'r') as f:
        data1 = []
        for line in f.readlines():
            numbers = line.split()
            data1.append(numbers)
    with open(file, 'r') as f:
        data2 = f.read().strip().split('\n')
    return data1, data2


if __name__ == "__main__":
    import pytest
    import sys
    sys.exit(pytest.main(['-v', './2025/06/day_2025_06_test.py']))
