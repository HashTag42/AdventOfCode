'''
Advent of Code 2016 - Day 1: No Time for a Taxicab
Puzzle: https://adventofcode.com/2016/day/1
'''
from Position import Position
from Vector import Vector


def solve(filename: str) -> tuple[int, int]:
    moves: list[str] = get_data(filename)
    vector: Vector = Vector()
    visited: set[Position] = {vector.position}
    double_blocks: int | None = None
    for move in moves:
        steps = vector.travel(move)
        for step in steps:
            if double_blocks is None and step in visited:
                double_blocks = step.get_blocks()
            visited.add(step)
    return vector.position.get_blocks(), double_blocks or 0


def get_data(filename: str) -> list[str]:
    with open(filename, 'r') as file:
        data = file.read().split(',')
        for i, v in enumerate(data):
            data[i] = v.strip()
        return data


if __name__ == "__main__":
    result1, result2 = solve('./2016/2016-01/example.txt')
    print(f"example.txt: Results: Part 1 = {result1}, Part 2 = {result2}")
    result1, result2 = solve('./2016/2016-01/input.txt')
    print(f"input.txt: Results: Part 1 = {result1}, Part 2 = {result2}")
