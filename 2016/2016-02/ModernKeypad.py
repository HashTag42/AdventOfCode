class ModernKeypad:
    def __init__(self) -> None:
        self.position: tuple[int, int] = (2, 0)     # Start at '5'
        self.buttons: list[list[str]] = [
            [' ', ' ', '1', ' ', ' '],
            [' ', '2', '3', '4', ' '],
            ['5', '6', '7', '8', '9'],
            [' ', 'A', 'B', 'C', ' '],
            [' ', ' ', 'D', ' ', ' '],
        ]

    def move(self, direction: str) -> tuple[int, int]:
        row_edge = len(self.buttons) - 1
        col_edge = len(self.buttons[0]) - 1
        match direction:
            case 'U':
                row_target, col_target = self.position[0] - 1, self.position[1]
                if self.position[0] > 0 and self.buttons[row_target][col_target] != ' ':
                    self.position = (row_target, col_target)
            case 'D':
                row_target, col_target = self.position[0] + 1, self.position[1]
                if self.position[0] < row_edge and self.buttons[row_target][col_target] != ' ':
                    self.position = (row_target, col_target)
            case 'L':
                row_target, col_target = self.position[0], self.position[1] - 1
                if self.position[1] > 0 and self.buttons[row_target][col_target] != ' ':
                    self.position = (row_target, col_target)
            case 'R':
                row_target, col_target = self.position[0], self.position[1] + 1
                if self.position[1] < col_edge and self.buttons[row_target][col_target] != ' ':
                    self.position = (row_target, col_target)
            case _:
                raise ValueError(f'Invalid direction: {direction=}')
        return self.position

    def press(self) -> str:
        return self.buttons[self.position[0]][self.position[1]]

    def __repr__(self) -> str:
        return f'{self.position}'
