'''
Advent of Code 2016 - Day 06: Signals and Noise
Puzzle: https://adventofcode.com/2016/day/6
'''
from collections import Counter


def solve(filename: str) -> tuple[str, int]:
    matrix: list[str] = get_data(filename)
    return solve_part1(matrix), solve_part2(matrix)


def solve_part1(matrix: list[str]) -> str:
    corrected_message: str = ""
    length = len(matrix[0])
    counters: list[Counter] = [Counter() for _ in range(length)]
    for row in matrix:
        for col in range(length):
            counters[col].update(row[col])
    for col in range(length):
        corrected_message += counters[col].most_common(1)[0][0]
    return corrected_message


def solve_part2(matrix: list[str]) -> int:
    result = 0
    return result


def get_data(filename: str) -> list[str]:
    with open(filename, 'r') as file:
        return [line.strip() for line in file]


if __name__ == "__main__":
    result1, result2 = solve('./2016/2016-06/example.txt')
    print(f"example.txt: Results: Part 1 = {result1}, Part 2 = {result2}")

    result1, result2 = solve('./2016/2016-06/input.txt')
    print(f"input.txt: Results: Part 1 = {result1}, Part 2 = {result2}")
