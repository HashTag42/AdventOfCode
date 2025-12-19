'''
Advent of Code 2015 - Day 19: Medicine for Rudolph
Puzzle: https://adventofcode.com/2015/day/19
'''
import random


def solve_2015_19(filename: str) -> tuple[int, int]:
    data = get_data(filename)
    return solve_part1(data), solve_part2(data)


def solve_part1(data) -> int:
    # Parse replacements and molecule
    replacements = []
    molecule = ""
    for line in data:
        if '=>' in line:
            source, dest = line.split(' => ')
            replacements.append((source, dest))
        elif line.strip():  # Non-empty line that's not a rule = the molecule
            molecule = line.strip()
    # Generate all possible molecules after one replacement
    distinct = set()
    for source, dest in replacements:
        # Find all occurrences of source in molecule
        start = 0
        while True:
            pos = molecule.find(source, start)
            if pos == -1:
                break
            # Create new molecule by replacing THIS occurrence only
            new_molecule = molecule[:pos] + dest + molecule[pos + len(source):]
            distinct.add(new_molecule)
            start = pos + 1  # Move past this position to find next occurrence
    return len(distinct)


def solve_part2(data) -> int:
    # Parse replacements and molecule
    replacements = []
    molecule = ""
    for line in data:
        if '=>' in line:
            source, dest = line.split(' => ')
            replacements.append((source, dest))
        elif line.strip():
            molecule = line.strip()
    target = molecule
    # Work backwards with randomized greedy approach
    while True:
        random.shuffle(replacements)
        current = target
        count = 0
        while current != 'e':
            replaced = False
            for source, dest in replacements:
                if dest in current:
                    # Replace ONE occurrence (going backwards: dest -> source)
                    current = current.replace(dest, source, 1)
                    count += 1
                    replaced = True
                    break
            if not replaced:
                # Stuck - restart with different rule order
                break
        if current == 'e':
            return count


def get_data(filename: str) -> list[str]:
    with open(filename, 'r') as file:
        data = file.read().strip().split('\n')
    return data


if __name__ == "__main__":
    import pytest
    import sys
    sys.exit(pytest.main(['-v', './2015/2015-19/AoC_2015_19_test.py']))
