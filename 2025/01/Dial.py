import re

MIN = 0
MAX = 99


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
            factor = 1
        elif direction == "L":
            factor = -1
        else:
            raise ValueError("Unrecognized direction")

        self.position += factor * distance
        if self.position < MIN:
            self.position += MAX - MIN + 1
        elif self.position > MAX:
            self.position -= MAX - MIN + 1

        return self.position
