class Direction:
    def __init__(self, x_dir: int = 0, y_dir: int = 0) -> None:
        self.x_dir: int = x_dir
        self.y_dir: int = y_dir

    def turn(self, turn_direction: str) -> None:
        match turn_direction:
            case 'R':
                self.x_dir, self.y_dir = self.y_dir, -self.x_dir
            case 'L':
                self.x_dir, self.y_dir = -self.y_dir, self.x_dir
            case _:
                raise ValueError("Invalid turn direction.")

    def __repr__(self) -> str:
        return f"[{self.x_dir}, {self.y_dir}]"
