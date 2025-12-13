'''
Advent of Code 2015 - Day 13: Knights of the Dinner Table
Puzzle: https://adventofcode.com/2015/day/13
'''
from pathlib import Path
from itertools import permutations
# Graph's implementation is at https://github.com/HashTag42/Python/blob/master/Python101/Graph.py
from Graph import Graph, GraphNode


def solve_2015_13(filename: Path) -> tuple[int, int]:
    graph = get_data(filename)
    return solve_part1(graph), solve_part2(graph)


def solve_part1(graph: Graph) -> int:
    happiness, max_happiness = 0, 0
    perms = list(permutations(graph.nodes))
    total_people = len(graph.nodes)
    for p in perms:
        for i in range(total_people - 1):
            happiness += graph.get_weight(p[i], p[i+1]) + graph.get_weight(p[i+1], p[i])
        happiness += graph.get_weight(p[total_people - 1], p[0]) + graph.get_weight(p[0], p[total_people - 1])
        max_happiness = happiness if happiness > max_happiness else max_happiness
        happiness = 0
    return max_happiness


def solve_part2(graph: Graph) -> int:
    result = 0
    return result


def get_data(filename: Path) -> Graph:
    """
    Loads the input file into a directed Graph object, using an adjacency matrix.
    Nodes are people and weights are the happiness gained (or lost if negative) from sitting next to someone else.
    """
    with open(filename, 'r') as file:
        graph = Graph(directed=True)
        for line in file.readlines():
            # Example: "Alice would gain 54 happiness units by sitting next to Bob."
            parts = line.split()
            from_node: GraphNode = GraphNode(parts[0])  # 'Alice'
            to_node: GraphNode = GraphNode(parts[10].rstrip('.'))  # 'Bob'
            sign: int = 1 if parts[2] == 'gain' else -1  # 'gain'(or 'lose')
            weight: int = sign * int(parts[3])  # '54'
            graph.add_edge(from_node, to_node, weight)
        return graph


if __name__ == "__main__":
    import pytest
    import sys
    sys.exit(pytest.main(['-v', str(Path('./2015/2015-13/AoC_2015_13_test.py'))]))
