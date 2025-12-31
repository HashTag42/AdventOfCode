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
    tuples = get_data(filename)
    return solve_part1(tuples), solve_part2(tuples)


def solve_part1(tuples: list[tuple[int, int, int]]) -> int:
    triangles = 0
    for item in tuples:
        shape: Shape = Shape(item)
        triangles += 1 if shape.isTriangle else 0
    return triangles


def solve_part2(tuples: list[tuple[int, int, int]]) -> int:
    triangles, row, length = 0, 0, len(tuples)
    while True:
        for i in range(3):
            shape: Shape = Shape((tuples[row][i], tuples[row+1][i], tuples[row+2][i]))
            triangles += 1 if shape.isTriangle else 0
        row = row + 3
        if row >= length:
            break
    return triangles


def get_data(filename: str) -> list[tuple[int, int, int]]:
    tuples: list[tuple[int, int, int]] = []
    with open(filename, 'r') as file:
        for line in file.readlines():
            values: list[str] = [val for val in line.split()]
            item: tuple[int, int, int] = (int(values[0]), int(values[1]), int(values[2]))
            tuples.append(item)
    return tuples


if __name__ == "__main__":
    result1, result2 = solve('./2016/2016-03/input.txt')
    print(f"input.txt: Results: Part 1 = {result1}, Part 2 = {result2}")
