'''
Advent of Code 2016 - Day 02: Bathroom Security
Puzzle: https://adventofcode.com/2016/day/02
'''


class Keypad:
    def __init__(self) -> None:
        self.position: tuple[int, int] = (1, 1)
        self.buttons: list[list[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    def move(self, direction: str) -> tuple[int, int]:
        match direction:
            case "U":
                if self.position[0] > 0:
                    self.position = (self.position[0] - 1, self.position[1])
            case "D":
                if self.position[0] < 2:
                    self.position = (self.position[0] + 1, self.position[1])
            case "L":
                if self.position[1] > 0:
                    self.position = (self.position[0], self.position[1] - 1)
            case "R":
                if self.position[1] < 2:
                    self.position = (self.position[0], self.position[1] + 1)
            case _:
                raise ValueError(f"Invalid direction: {direction=}")
        return self.position

    def press(self) -> int:
        return self.buttons[self.position[0]][self.position[1]]

    def __repr__(self) -> str:
        return f"{self.position}"


def solve(filename: str) -> tuple[int, int]:
    data = get_data(filename)
    return solve_part1(data), solve_part2(data)


def solve_part1(data) -> int:
    keypad: Keypad = Keypad()
    code: str = ""
    for line in data:
        for step in line.strip():
            keypad.move(step)
        code += str(keypad.press())
    return int(code)


def solve_part2(data) -> int:
    result = 0
    return result


def get_data(filename: str) -> list[str]:
    with open(filename, 'r') as file:
        data = file.readlines()
    return data


if __name__ == "__main__":
    result1, result2 = solve('./2016/2016-02/example.txt')
    print(f"example.txt: Results: Part 1 = {result1}, Part 2 = {result2}")
    result1, result2 = solve('./2016/2016-02/input.txt')
    print(f"input.txt: Results: Part 1 = {result1}, Part 2 = {result2}")
