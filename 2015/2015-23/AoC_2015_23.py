'''
Advent of Code 2015 - Day 23: Opening the Turing Lock
Puzzle: https://adventofcode.com/2015/day/23
'''
from Instruction import Instruction
from Runbook import Runbook


def solve(filename: str, register: str, part: int) -> int:
    runbook = Runbook(get_data(filename))
    if part == 2:
        runbook.registers['a'] = 1
    runbook.run()
    return runbook.registers[register]


def get_data(filename: str) -> list[Instruction]:
    """Read a list of instructions from the input file"""
    instructions: list[Instruction] = []
    with open(filename, 'r') as file:
        for line in file.readlines():
            instructions.append(Instruction(line))
    return instructions


if __name__ == "__main__":
    result1 = solve('./2015/2015-23/example.txt', 'a', 1)
    result2 = solve('./2015/2015-23/example.txt', 'a', 2)
    print(f"example.txt, register 'a': Part 1 = {result1}, Part 2 = {result2}")

    result1 = solve('./2015/2015-23/input.txt', 'b', 1)
    result2 = solve('./2015/2015-23/input.txt', 'b', 2)
    print(f"input.txt, register 'b': Part 1: {result1}, Part 2: {result2}")
