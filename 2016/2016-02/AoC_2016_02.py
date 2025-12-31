'''
Advent of Code 2016 - Day 02: Bathroom Security
Puzzle: https://adventofcode.com/2016/day/02
'''


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


def solve(filename: str) -> tuple[str, str]:
    data = get_data(filename)
    return solve_part1(data), solve_part2(data)


def solve_part1(lines: list[str]) -> str:
    keypad: ClassicKeypad = ClassicKeypad()
    code: str = ''
    for line in lines:
        for direction in line:
            keypad.move(direction)
        code += str(keypad.press())
    return code


def solve_part2(lines: list[str]) -> str:
    keypad: ModernKeypad = ModernKeypad()
    code: str = ''
    for line in lines:
        for step in line:
            keypad.move(step)
        code += str(keypad.press())
    return code


def get_data(filename: str) -> list[str]:
    with open(filename, 'r') as file:
        return [line.strip() for line in file]


if __name__ == '__main__':
    result1, result2 = solve('./2016/2016-02/example.txt')
    print(f'example.txt: Results: Part 1 = {result1}, Part 2 = {result2}')
    result1, result2 = solve('./2016/2016-02/input.txt')
    print(f'input.txt: Results: Part 1 = {result1}, Part 2 = {result2}')
