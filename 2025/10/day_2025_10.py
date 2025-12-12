'''
Advent of Code 2025 - Day 10: Factory
Puzzle: https://adventofcode.com/2025/day/10

Key insight: Since pressing a button twice cancels out, each button is pressed 0 or 1 times.
This becomes a system of linear equations over GF(2), but we want minimum number of 1s.
We need to find all solutions and pick the one with minimum Hamming weight.
'''

import re
from itertools import product


class Machine():
    def __init__(self, line: str) -> None:
        # Parse lights pattern [.##.]
        lights_match = re.search(r'\[([.#]+)\]', line)
        if lights_match is not None:
            self.target = lights_match.group(1)
        self.num_lights = len(self.target)

        # Parse buttons (x) or (x,y,z)
        buttons_matches = re.findall(r'\(([0-9,]+)\)', line)
        self.buttons = []
        for match in buttons_matches:
            indices = [int(x) for x in match.split(',')]
            self.buttons.append(indices)

        # Parse joltage {x,y,z}
        joltage_match = re.search(r'\{([0-9,]+)\}', line)
        if joltage_match is not None:
            self.joltage = [int(x) for x in joltage_match.group(1).split(',')]

    def __repr__(self) -> str:
        return f"[{self.target}] buttons={self.buttons}"

    def get_target_vector(self):
        """Convert target pattern to binary vector"""
        return [1 if c == '#' else 0 for c in self.target]

    def get_button_vectors(self):
        """Get button effects as binary vectors"""
        vectors = []
        for button in self.buttons:
            vec = [0] * self.num_lights
            for idx in button:
                vec[idx] = 1
            vectors.append(vec)
        return vectors


def solve_minimum_presses(machine: Machine) -> int:
    """
    Find minimum button presses to reach target state.
    Uses Gaussian elimination over GF(2) then enumerates free variables.
    """
    target = machine.get_target_vector()
    button_vecs = machine.get_button_vectors()
    num_buttons = len(button_vecs)
    num_lights = machine.num_lights

    # Build augmented matrix [A | b] where A has buttons as columns
    matrix = []
    for i in range(num_lights):
        row = [button_vecs[j][i] for j in range(num_buttons)]
        row.append(target[i])
        matrix.append(row)

    # Gaussian elimination over GF(2)
    pivot_cols = []
    row = 0
    for col in range(num_buttons):
        # Find pivot
        pivot_row = None
        for r in range(row, num_lights):
            if matrix[r][col] == 1:
                pivot_row = r
                break

        if pivot_row is None:
            continue

        # Swap rows
        matrix[row], matrix[pivot_row] = matrix[pivot_row], matrix[row]
        pivot_cols.append(col)

        # Eliminate
        for r in range(num_lights):
            if r != row and matrix[r][col] == 1:
                for c in range(num_buttons + 1):
                    matrix[r][c] ^= matrix[row][c]

        row += 1

    # Check for inconsistency
    for r in range(row, num_lights):
        if matrix[r][num_buttons] == 1:
            return int(float('inf'))  # No solution

    # Free variables are columns not in pivot_cols
    free_vars = [c for c in range(num_buttons) if c not in pivot_cols]
    num_free = len(free_vars)

    # Enumerate all assignments to free variables to find minimum weight solution
    min_weight = float('inf')

    for free_assignment in product([0, 1], repeat=num_free):
        # Build solution
        solution = [0] * num_buttons

        # Set free variables
        for i, fv in enumerate(free_vars):
            solution[fv] = free_assignment[i]

        # Back-substitute for pivot variables
        for i in range(len(pivot_cols) - 1, -1, -1):
            pc = pivot_cols[i]
            val = matrix[i][num_buttons]
            for c in range(pc + 1, num_buttons):
                val ^= matrix[i][c] * solution[c]
            solution[pc] = val

        weight = sum(solution)
        min_weight = min(min_weight, weight)

    return int(min_weight)


def solve_2025_10(filename: str) -> tuple[int, int]:
    machines = get_data(filename)
    return solve_part1(machines), solve_part2(machines)


def solve_part1(machines) -> int:
    total: int = 0
    for machine in machines:
        presses: int = solve_minimum_presses(machine)
        total += presses
    return total


def solve_part2(machines) -> int:
    result = 0
    return result


def get_data(filename) -> list[Machine]:
    machines: list[Machine] = []
    with open(filename, 'r') as file:
        for line in file.readlines():
            line = line.strip()
            if line:
                machines.append(Machine(line))
        return machines


if __name__ == "__main__":
    import pytest
    import sys
    sys.exit(pytest.main(['-v', './2025/10/day_2025_10_test.py']))
