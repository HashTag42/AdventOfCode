'''
Advent of Code 2025 - Day 11: Reactor
Puzzle: https://adventofcode.com/2025/day/11

Part 1: Count all paths from 'you' to 'out'
Part 2: Count paths from 'svr' to 'out' that visit BOTH 'dac' and 'fft'

Approach: DFS with memoization
- For Part 2, state includes which required nodes have been visited
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
    graph = data

    @cache
    def count_paths(node: str, seen_dac: bool, seen_fft: bool) -> int:
        # Update flags if we're at dac or fft
        if node == "dac":
            seen_dac = True
        if node == "fft":
            seen_fft = True

        # Base case: reached the destination
        if node == "out":
            # Only count if we've visited BOTH required nodes
            return 1 if (seen_dac and seen_fft) else 0

        # If node has no outputs (dead end, not 'out'), no valid paths
        if node not in graph:
            return 0

        # Sum paths through all children
        total = 0
        for child in graph[node]:
            total += count_paths(child, seen_dac, seen_fft)

        return total

    return count_paths("svr", False, False)


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
    sys.exit(pytest.main(['-v', './2025/11/AoC_2025_11_test.py']))
