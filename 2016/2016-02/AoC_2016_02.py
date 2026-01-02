'''
Advent of Code 2016 - Day 02: Bathroom Security
Puzzle: https://adventofcode.com/2016/day/02
'''
from ClassicKeypad import ClassicKeypad
from ModernKeypad import ModernKeypad


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
