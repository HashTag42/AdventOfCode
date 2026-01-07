from enum import Enum


class State(Enum):
    OFF = '.'
    ON = '#'


class Screen:
    def __init__(self, cols: int, rows: int) -> None:
        self.cols = cols
        self.rows = rows
        self.screen: list[list[State]] = [[State.OFF for _ in range(cols)] for _ in range(rows)]

    def count(self, state: State) -> int:
        return sum(cell == state for row in self.screen for cell in row)

    def execute(self, operation: str) -> None:
        tokens = operation.split()
        match tokens[0]:
            case 'rect':
                cols, rows = map(int, tokens[1].split('x'))
                self._rect(cols, rows)
            case 'rotate':
                axis = tokens[1]          # "row" or "column"
                index = int(tokens[2].split('=')[1])
                amount = int(tokens[4])   # number after "by"
                if axis == 'row':
                    self._rotate_row(index, amount)
                elif axis == 'column':
                    self._rotate_col(index, amount)

    def _rect(self, cols: int, rows: int) -> None:
        for row in range(rows):
            for col in range(cols):
                self.screen[row][col] = State.ON

    def _rotate_col(self, index: int, amount: int) -> None:
        # Rotate column downward
        amount %= self.rows
        col_vals = [self.screen[r][index] for r in range(self.rows)]
        col_vals = col_vals[-amount:] + col_vals[:-amount]
        for r in range(self.rows):
            self.screen[r][index] = col_vals[r]

    def _rotate_row(self, index: int, amount: int) -> None:
        # Rotate row to the right
        amount %= self.cols
        self.screen[index] = (
            self.screen[index][-amount:] + self.screen[index][:-amount]
        )

    def __repr__(self) -> str:
        return "\n".join("".join(c.value for c in row) for row in self.screen)
