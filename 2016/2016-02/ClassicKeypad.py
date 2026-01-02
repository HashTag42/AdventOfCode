class ClassicKeypad:
    def __init__(self) -> None:
        self.position: tuple[int, int] = (1, 1)     # Start at '5'
        self.buttons: list[list[int]] = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]

    def move(self, direction: str) -> tuple[int, int]:
        row_edge = len(self.buttons) - 1
        col_edge = len(self.buttons[0]) - 1
        match direction:
            case 'U':
                if self.position[0] > 0:
                    self.position = (self.position[0] - 1, self.position[1])
            case 'D':
                if self.position[0] < row_edge:
                    self.position = (self.position[0] + 1, self.position[1])
            case 'L':
                if self.position[1] > 0:
                    self.position = (self.position[0], self.position[1] - 1)
            case 'R':
                if self.position[1] < col_edge:
                    self.position = (self.position[0], self.position[1] + 1)
            case _:
                raise ValueError(f'Invalid direction: {direction=}')
        return self.position

    def press(self) -> int:
        return self.buttons[self.position[0]][self.position[1]]

    def __repr__(self) -> str:
        return f'{self.position}'
