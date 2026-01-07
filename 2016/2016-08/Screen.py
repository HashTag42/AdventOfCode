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
        command = tokens[0]

        match command:
            case "rect":
                cols, rows = self._parse_rect(tokens)
                self._rect(cols, rows)

            case "rotate":
                axis, index, amount = self._parse_rotate(tokens)
                if axis == "row":
                    self._rotate_row(index, amount)
                elif axis == "column":
                    self._rotate_col(index, amount)
                else:
                    raise ValueError(f"Invalid rotate axis: {axis}")

            case _:
                raise ValueError(f"Unknown operation: {operation}")

    def _parse_rect(self, tokens: list[str]) -> tuple[int, int]:
        if len(tokens) != 2:
            raise ValueError(f"Invalid rect syntax: {' '.join(tokens)}")

        try:
            cols, rows = map(int, tokens[1].split("x"))
        except ValueError as exc:
            raise ValueError(f"Invalid rect dimensions: {tokens[1]}") from exc

        return cols, rows

    def _parse_rotate(self, tokens: list[str]) -> tuple[str, int, int]:
        if len(tokens) != 5 or tokens[3] != "by":
            raise ValueError(f"Invalid rotate syntax: {' '.join(tokens)}")

        axis = tokens[1]

        try:
            index = int(tokens[2].split("=")[1])
            amount = int(tokens[4])
        except (IndexError, ValueError) as exc:
            raise ValueError(f"Invalid rotate arguments: {' '.join(tokens)}") from exc

        return axis, index, amount

    def _parse_rotate_row(self, tokens: list[str]) -> tuple[int, int]:
        _, _, y_part, _, amount = tokens
        return int(y_part.split("=")[1]), int(amount)

    def _parse_rotate_column(self, tokens: list[str]) -> tuple[int, int]:
        _, _, x_part, _, amount = tokens
        return int(x_part.split("=")[1]), int(amount)

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

    def __str__(self) -> str:
        return "\n".join("".join(c.value for c in row) for row in self.screen)

    __repr__ = __str__
