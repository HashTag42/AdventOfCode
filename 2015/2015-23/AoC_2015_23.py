'''
Advent of Code 2015 - Day 23: Opening the Turing Lock
Puzzle: https://adventofcode.com/2015/day/23
'''


class Instruction:
    def __init__(self, line: str) -> None:
        self.line: str = line.strip()
        self.tuple: tuple = tuple(line.replace(",", " ").split())
        self.instruction: str = self.tuple[0]

    def __repr__(self) -> str:
        return self.line


class Runbook:
    def __init__(self, instructions: list[Instruction] = []) -> None:
        self.instructions: list[Instruction] = instructions
        self.registers: dict[str, int] = {'a': 0, 'b': 0}

    def run(self) -> None:
        index: int = 0
        while True:
            if index >= len(self.instructions):
                break
            instruction: Instruction = self.instructions[index]
            match instruction.instruction:
                case 'hlf':
                    self.registers[instruction.tuple[1]] //= 2
                    index += 1
                case 'tpl':
                    self.registers[instruction.tuple[1]] *= 3
                    index += 1
                case 'inc':
                    self.registers[instruction.tuple[1]] += 1
                    index += 1
                case 'jmp':
                    index += int(instruction.tuple[1])
                case 'jie':
                    if self.registers[instruction.tuple[1]] % 2 == 0:
                        index += int(instruction.tuple[2])
                    else:
                        index += 1
                case 'jio':
                    if self.registers[instruction.tuple[1]] == 1:
                        index += int(instruction.tuple[2])
                    else:
                        index += 1
                case _:
                    pass

    def __repr__(self) -> str:
        return f"Runbook: {len(self.instructions)} instructions, {self.registers=}"


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
