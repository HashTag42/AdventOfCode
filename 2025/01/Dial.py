import re

# General parameters
MIN = 0
MAX = 99
START = 50
RANGE = MAX - MIN + 1


class Dial():
    def __init__(self, start: int = START) -> None:
        self.position: int = start

    def rotate(self, rotation: str) -> int:
        """Rotate the dial according to the rotation instruction and return the updated position."""
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
            self.position += RANGE
        elif self.position > MAX:
            self.position -= RANGE

        return self.position
