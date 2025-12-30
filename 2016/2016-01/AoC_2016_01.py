'''
Advent of Code 2016 - Day 1: No Time for a Taxicab
Puzzle: https://adventofcode.com/2016/day/1
'''


class Position:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x: int = x
        self.y: int = y


class Direction:
    def __init__(self, x_dir: int = 0, y_dir: int = 0) -> None:
        self.x_dir: int = x_dir
        self.y_dir: int = y_dir

    def turn(self, turn_direction: str) -> None:
        match turn_direction:
            case 'R':
                match (self.x_dir, self.y_dir):
                    case (0, 1):
                        self.x_dir, self.y_dir = 1, 0
                    case (1, 0):
                        self.x_dir, self.y_dir = 0, -1
                    case (0, -1):
                        self.x_dir, self.y_dir = -1, 0
                    case (-1, 0):
                        self.x_dir, self.y_dir = 0, 1
                    case _:
                        raise ValueError("Invalid direction")
            case 'L':
                match (self.x_dir, self.y_dir):
                    case (0, 1):
                        self.x_dir, self.y_dir = -1, 0
                    case (-1, 0):
                        self.x_dir, self.y_dir = 0, -1
                    case (0, -1):
                        self.x_dir, self.y_dir = 1, 0
                    case (1, 0):
                        self.x_dir, self.y_dir = 0, 1
                    case _:
                        raise ValueError("Invalid direction")
            case _:
                raise ValueError("Invalid turn direction.")


class Vector:
    def __init__(self, position: Position, direction: Direction, length: int = 0) -> None:
        self.position: Position = position
        self.direction: Direction = direction
        self.length: int = length

    def move(self, step: str) -> None:
        turn: str = step[0]
        distance: int = int(step[1:])
        self.direction.turn(turn)
        new_x: int = self.position.x + self.direction.x_dir * distance
        new_y: int = self.position.y + self.direction.y_dir * distance
        self.position = Position(new_x, new_y)

    def get_blocks(self) -> int:
        return abs(self.position.x) + abs(self.position.y)


def solve(filename: str) -> tuple[int, int]:
    data = get_data(filename)
    return solve_part1(data), solve_part2(data)


def solve_part1(data) -> int:
    vector: Vector = Vector(Position(0, 0), Direction(0, 1))
    for step in data:
        vector.move(step)
    return vector.get_blocks()


def solve_part2(data) -> int:
    result = 0
    return result


def get_data(filename: str) -> list[str]:
    with open(filename, 'r') as file:
        data = file.read().split(',')
        for i, v in enumerate(data):
            data[i] = v.strip()
        return data


if __name__ == "__main__":
    result1, result2 = solve('./2016/2016-01/example.txt')
    print(f"example.txt: Results: Part 1 = {result1}, Part 2 = {result2}")

    result1, result2 = solve('./2016/2016-01/input.txt')
    print(f"input.txt: Results: Part 1 = {result1}, Part 2 = {result2}")
