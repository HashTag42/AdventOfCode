'''
Advent of Code 2025 - Day 11: Reactor
Puzzle: https://adventofcode.com/2025/day/11

This is a path counting problem in a DAG (Directed Acyclic Graph).
We need to count all distinct paths from 'you' to 'out'.

Approach: DFS with memoization
- count_paths(node) returns number of paths from node to 'out'
- Base case: count_paths("out") = 1
- Recursive: count_paths(node) = sum of count_paths for all children
'''

from functools import cache


def solve_2025_11(filename: str) -> tuple[int, int]:
    data = get_data(filename)
    return solve_part1(data), solve_part2(data)


def solve_part1(data: dict[str, list[str]]) -> int:
    graph = data

    @cache
    def count_paths(node: str) -> int:
        # Base case: reached the destination
        if node == "out":
            return 1

        # If node has no outputs (dead end, not 'out'), no valid paths
        if node not in graph:
            return 0

        # Sum paths through all children
        total = 0
        for child in graph[node]:
            total += count_paths(child)

        return total

    return count_paths("you")


def solve_part2(data: dict[str, list[str]]) -> int:
    result = 0
    return result


def get_data(filename: str) -> dict[str, list[str]]:
    """Parse input into a graph (adjacency list)"""
    graph = {}
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            # Format: "node: child1 child2 child3"
            parts = line.split(': ')
            node = parts[0]
            children = parts[1].split()
            graph[node] = children
    return graph


if __name__ == "__main__":
    import pytest
    import sys
    sys.exit(pytest.main(['-v', './2025/11/day_2025_11_test.py']))
