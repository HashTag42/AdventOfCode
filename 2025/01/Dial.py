import re

# Dial constants
MIN = 0
START = 50
MAX = 99
LENGTH = MAX - MIN + 1


class Dial():
    def __init__(self, start: int = START) -> None:
        self.position: int = start

    def rotate(self, rotation: str) -> int:
        """Rotate the dial according to the rotation instruction and return the updated position."""

        # Identify
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

        # Rotate the dial
        self.position += factor * distance % LENGTH
        if self.position > MAX:
            self.position -= LENGTH

        return self.position
