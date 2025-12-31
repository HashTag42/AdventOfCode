'''
Advent of Code YEAR - Day DAY:
Puzzle: https://adventofcode.com/YEAR/day/DAY
'''


def solve(filename: str) -> tuple[int, int]:
    data = get_data(filename)
    return solve_part1(data), solve_part2(data)


def solve_part1(data) -> int:
    result = 0
    return result


def solve_part2(data) -> int:
    result = 0
    return result


def get_data(filename: str) -> list[str]:
    with open(filename, 'r') as file:
        return [line.strip() for line in file]


if __name__ == "__main__":
    result1, result2 = solve('./YEAR/FOLDER/example.txt')
    print(f"example.txt: Results: Part 1 = {result1}, Part 2 = {result2}")

    result1, result2 = solve('./YEAR/FOLDER/input.txt')
    print(f"input.txt: Results: Part 1 = {result1}, Part 2 = {result2}")
