import re


class Dial():
    def __init__(self) -> None:
        self.position: int = 50

    def rotate(self, rotation: str) -> int:
        match = re.match(r'([A-Z])(\d+)', rotation)
        if match:
            direction, distance = match.groups()
        else:
            raise ValueError("Unrecognized rotation")

        distance = int(distance)
        if direction == "R":
            return self._rotate_right(distance)
        elif direction == "L":
            return self._rotate_left(distance)
        else:
            raise ValueError("Unrecognized direction")

    def _rotate_right(self, distance: int) -> int:
        self.position += distance
        if self.position > 99:
            self.position -= 100
        return self.position

    def _rotate_left(self, distance: int) -> int:
        self.position -= distance
        if self.position < 0:
            self.position += 100
        return self.position
