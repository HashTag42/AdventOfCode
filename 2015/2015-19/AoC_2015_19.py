'''
Advent of Code 2015 - Day 19: Medicine for Rudolph
Puzzle: https://adventofcode.com/2015/day/19
'''


def solve_2015_19(filename: str) -> tuple[int, int]:
    data = get_data(filename)
    return solve_part1(data), solve_part2(data)


def solve_part1(data) -> int:
    lines = data.strip().split('\n')
    # Parse replacements and molecule
    replacements = []
    molecule = ""
    for line in lines:
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
    result = 0
    return result


def get_data(filename: str) -> str:
    with open(filename, 'r') as file:
        data = file.read()
    return data


if __name__ == "__main__":
    import pytest
    import sys
    sys.exit(pytest.main(['-v', './2015/2015-19/AoC_2015_19_test.py']))
