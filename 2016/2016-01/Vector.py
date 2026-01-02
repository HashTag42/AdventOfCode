from Position import Position
from Direction import Direction


class Vector:
    def __init__(self, position: Position = Position(0, 0), direction: Direction = Direction(0, 1)) -> None:
        self.position: Position = position
        self.direction: Direction = direction

    def travel(self, move: str) -> list[Position]:
        turn: str = move[0]
        distance: int = int(move[1:])
        self.direction.turn(turn)
        steps: list[Position] = []
        for _ in range(distance):
            self.position = Position(
                self.position.x + self.direction.x_dir,
                self.position.y + self.direction.y_dir
            )
            steps.append(self.position)
        return steps

    def __repr__(self) -> str:
        return f"{self.position} - {self.direction}"
