'''
Advent of Code YEAR - Day DAY:
Puzzle: https://adventofcode.com/YEAR/day/DAY
'''


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
    with open(filename, 'r') as file:
        return [line.strip() for line in file]


if __name__ == "__main__":
    input_files = [
        './YEAR/FOLDER/example.txt',
        './YEAR/FOLDER/input.txt',
    ]
    for input_file in input_files:
        result1, result2 = solve(input_file)
        print(f"{input_file=}: Results: {result1=}, {result2=}")
