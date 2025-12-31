'''
Advent of Code 2016 - Day 03:
Puzzle: https://adventofcode.com/2016/day/03
'''


def is_triangle(sides: tuple[int, ...]) -> bool:
    a, b, c = sorted(sides)
    return a + b > c


def solve(filename: str) -> tuple[int, int]:
    data = get_data(filename)
    return solve_part1(data), solve_part2(data)


def solve_part1(data: list[tuple[int, ...]]) -> int:
    return sum(is_triangle(sides) for sides in data)


def solve_part2(data: list[tuple[int, ...]]) -> int:
    total = 0
    for i in range(0, len(data), 3):
        for col in zip(data[i], data[i+1], data[i+2]):
            total += 1 if is_triangle(col) else 0
    return total


def get_data(filename: str) -> list[tuple[int, ...]]:
    with open(filename, 'r') as file:
        return [tuple(map(int, line.split())) for line in file]


if __name__ == "__main__":
    result1, result2 = solve('./2016/2016-03/input.txt')
    print(f"input.txt: Results: Part 1 = {result1}, Part 2 = {result2}")
