'''
Advent of Code 2016 - Day 1: No Time for a Taxicab
Puzzle: https://adventofcode.com/2016/day/1
'''


class Position:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x: int = x
        self.y: int = y

    def get_blocks(self) -> int:
        return abs(self.x) + abs(self.y)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Position):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"


class Direction:
    def __init__(self, x_dir: int = 0, y_dir: int = 0) -> None:
        self.x_dir: int = x_dir
        self.y_dir: int = y_dir

    def turn(self, turn_direction: str) -> None:
        if turn_direction == 'R':
            self.x_dir, self.y_dir = self.y_dir, -self.x_dir
        elif turn_direction == 'L':
            self.x_dir, self.y_dir = -self.y_dir, self.x_dir
        else:
            raise ValueError("Invalid turn direction.")

    def __repr__(self) -> str:
        return f"[{self.x_dir}, {self.y_dir}]"


class Vector:
    def __init__(self, position: Position, direction: Direction, length: int = 0) -> None:
        self.position: Position = position
        self.direction: Direction = direction

    def travel(self, move: str) -> list[Position]:
        turn: str = move[0]
        distance: int = int(move[1:])
        self.direction.turn(turn)
        steps: list[Position] = []
        new_x: int = self.position.x + self.direction.x_dir * distance
        new_y: int = self.position.y + self.direction.y_dir * distance
        self.position = Position(new_x, new_y)
        return steps

    def __repr__(self) -> str:
        return f"{self.position} - {self.direction}"


def solve(filename: str) -> tuple[int, int]:
    steps: list[str] = get_data(filename)
    position = Position(0, 0)
    direction = Direction(0, 1)
    visited: set[Position] = {position}
    double_blocks: int | None = None

    for step in steps:
        direction.turn(step[0])
        distance = int(step[1:])

        for _ in range(distance):
            position = Position(
                position.x + direction.x_dir,
                position.y + direction.y_dir
            )
            if double_blocks is None and position in visited:
                double_blocks = abs(position.x) + abs(position.y)
            visited.add(position)

    part1 = abs(position.x) + abs(position.y)
    return part1, double_blocks or 0


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
