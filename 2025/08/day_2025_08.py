'''
Advent of Code 2025 - Day 8: Playground
Puzzle: https://adventofcode.com/2025/day/8
'''
from AoC_Graph import (
    Point,
    # Line,
    # Circuit,
    Graph,
)


def solve_2025_08(filename: str, num_connections: int) -> tuple[int, int]:
    points: set[Point] = get_data(filename)
    return solve_part1(points, num_connections), solve_part2(points, num_connections)


def solve_part1(points: set[Point], num_connections: int) -> int:
    graph = Graph(points, num_connections=num_connections)
    lengths = []
    for c in graph.circuits:
        lengths.append(len(c))
    lengths.sort(reverse=True)
    print(f"Circuit sizes: {lengths}")  # ← Add this
    print(f"Top 3: {lengths[0]}, {lengths[1]}, {lengths[2]}")  # ← Add this
    total = 1
    for i in range(3):
        total *= lengths[i]
    return total


def solve_part2(points: set[Point], num_connections: int) -> int:
    graph = Graph(points, num_connections=num_connections)
    return graph.part2


def get_data(filename) -> set[Point]:
    # Read points from the file
    points: set[Point] = set()
    with open(filename, 'r') as f:
        for line in f.readlines():
            x, y, z = map(int, line.split(','))
            points.add(Point(x, y, z))
    return points


if __name__ == "__main__":
    import pytest
    import sys
    sys.exit(pytest.main(['-v', './2025/08/day_2025_08_test.py']))
