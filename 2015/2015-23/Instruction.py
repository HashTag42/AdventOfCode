class Instruction:
    def __init__(self, line: str) -> None:
        self.line: str = line.strip()
        self.parts: tuple = tuple(line.replace(",", " ").split())
        self.opcode: str = self.parts[0]

    def __repr__(self) -> str:
        return self.line
