'''
Advent of Code 2016 - Day 03:
Puzzle: https://adventofcode.com/2016/day/03
'''
from itertools import permutations


class Shape:
    def __init__(self, sides: tuple[int, int, int]) -> None:
        self.sides: tuple[int, int, int] = sides
        self.isTriangle: bool = self.__is_triangle()

    def __is_triangle(self) -> bool:
        perms = permutations(self.sides)
        for perm in perms:
            if perm[0] + perm[1] <= perm[2]:
                return False
        return True


def solve(filename: str) -> tuple[int, int]:
    data = get_data(filename)
    return solve_part1(data), solve_part2(data)


def solve_part1(shapes: list[Shape]) -> int:
    total = 0
    for shape in shapes:
        if shape.isTriangle:
            total += 1
    return total


def solve_part2(data) -> int:
    result = 0
    return result


def get_data(filename: str) -> list[Shape]:
    shapes: list[Shape] = []
    with open(filename, 'r') as file:
        for line in file.readlines():
            values: list[str] = [val for val in line.split()]
            shape: Shape = Shape((int(values[0]), int(values[1]), int(values[2])))
            shapes.append(shape)
    return shapes


if __name__ == "__main__":
    result1, result2 = solve('./2016/2016-03/input.txt')
    print(f"input.txt: Results: Part 1 = {result1}, Part 2 = {result2}")
