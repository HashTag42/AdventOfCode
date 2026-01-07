from enum import Enum


class State(Enum):
    OFF = '.'
    ON = '#'

    def __str__(self):
        return self.value


class Screen:
    def __init__(self, cols: int, rows: int) -> None:
        self.cols = cols
        self.rows = rows
        self.screen: list[list[str]] = [[State.OFF.value for _ in range(cols)] for _ in range(rows)]

    def clear(self) -> None:
        for row in range(self.rows):
            for col in range(self.cols):
                self.screen[row][col] = State.OFF.value

    def execute(self, operation: str) -> None:
        tokens = operation.split()
        match tokens[0]:
            case 'rect':
                cols, rows = tokens[1].split('x')
                for row in range(int(rows)):
                    for col in range(int(cols)):
                        self.screen[row][col] = State.ON.value

            case 'rotate':
                axis = tokens[1]          # "row" or "column"
                index = int(tokens[2].split('=')[1])
                amount = int(tokens[4])   # number after "by"

                if axis == 'row':
                    # Rotate row to the right
                    amount %= self.cols
                    self.screen[index] = (
                        self.screen[index][-amount:] + self.screen[index][:-amount]
                    )

                elif axis == 'column':
                    # Rotate column downward
                    amount %= self.rows
                    col_vals = [self.screen[r][index] for r in range(self.rows)]
                    col_vals = col_vals[-amount:] + col_vals[:-amount]
                    for r in range(self.rows):
                        self.screen[r][index] = col_vals[r]

    def count(self, state: str) -> int:
        return sum(
            cell == state
            for row in self.screen
            for cell in row
        )

    def __repr__(self) -> str:
        return '\n'.join(
            ''.join(cell for cell in row)
            for row in self.screen
        )
