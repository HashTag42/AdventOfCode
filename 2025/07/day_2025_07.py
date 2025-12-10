'''
Advent of Code 2025 - Day 7:
Puzzle: https://adventofcode.com/2025/day/7
'''


def solve_2025_07(file: str) -> tuple[int, int]:
    data = get_data(file)
    return solve_part1(data), solve_part2(data)


def solve_part1(diagram) -> int:
    diagram[1][diagram[0].index('S')] = '|'
    splits = 0
    for r in range(2, len(diagram)):
        beams = [i for i, x in enumerate(diagram[r-1]) if x == '|']
        for b in beams:
            if diagram[r][b] == '.':
                diagram[r][b] = '|'
            elif diagram[r][b] == '^':
                splitted = False
                if diagram[r+1][b-1] != '^':
                    diagram[r][b-1] = '|'
                    splitted = True
                if diagram[r+1][b+1] != '^':
                    diagram[r][b+1] = '|'
                    splitted = True
                if splitted:
                    splits += 1
    return splits


def solve_part2(diagram) -> int:
    start_col = diagram[0].index('S')
    timelines = {start_col: 1}  # One timeline starts at S

    for r in range(1, len(diagram)):
        new_timelines = {}

        for col, count in timelines.items():
            cell = diagram[r][col]

            if cell == '.':
                # Beam continues straight - same timelines
                new_timelines[col] = new_timelines.get(col, 0) + count
            elif cell == '^':
                # Splitter: each timeline splits into left AND right
                new_timelines[col - 1] = new_timelines.get(col - 1, 0) + count
                new_timelines[col + 1] = new_timelines.get(col + 1, 0) + count

        timelines = new_timelines

    return sum(timelines.values())


def get_data(file) -> list[list[str]]:
    data = []
    with open(file, 'r') as f:
        for line in f.readlines():
            data.append(line.strip())
        data = [list(row) for row in data]
        return data


def print_diagram(diagram) -> None:
    string = ""
    diagram = [''.join(row) for row in diagram]
    for row in diagram:
        string += row + '\n'
    print(string)


if __name__ == "__main__":
    import pytest
    import sys
    sys.exit(pytest.main(['-v', './2025/07/day_2025_07_test.py']))
