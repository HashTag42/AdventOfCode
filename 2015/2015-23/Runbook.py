from Instruction import Instruction


class Runbook:
    def __init__(self, instructions: list[Instruction] | None = None) -> None:
        self.instructions: list[Instruction] = instructions if instructions is not None else []
        self.registers: dict[str, int] = {'a': 0, 'b': 0}

    def run(self) -> None:
        index: int = 0
        length = len(self.instructions)
        while index < length:
            instruction: Instruction = self.instructions[index]
            match instruction.opcode:
                case 'hlf':
                    self.registers[instruction.parts[1]] //= 2
                    index += 1
                case 'tpl':
                    self.registers[instruction.parts[1]] *= 3
                    index += 1
                case 'inc':
                    self.registers[instruction.parts[1]] += 1
                    index += 1
                case 'jmp':
                    index += int(instruction.parts[1])
                case 'jie':
                    if self.registers[instruction.parts[1]] % 2 == 0:
                        index += int(instruction.parts[2])
                    else:
                        index += 1
                case 'jio':
                    if self.registers[instruction.parts[1]] == 1:
                        index += int(instruction.parts[2])
                    else:
                        index += 1
                case _:
                    pass

    def __repr__(self) -> str:
        return f"Runbook: {len(self.instructions)} instructions, {self.registers=}"
