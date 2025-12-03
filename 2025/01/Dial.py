import re

# Dial constants
MIN = 0
START = 50
MAX = 99
LENGTH = MAX - MIN + 1
assert MIN < START < MAX, "START must be between MIN and MAX"
assert LENGTH > 0, "LENGTH must be positive"


class Dial():
    ################################################################################
    # region CONSTRUCTOR
    def __init__(self, start: int = START) -> None:
        self.position: int = start
    # endregion
    ################################################################################

    ################################################################################
    # region PUBLIC INTERFACE
    def rotate(self, rotation: str) -> tuple[int, int]:
        """
        Rotate the dial according to the rotation instruction.
        Returns (final_position, zero_crossings).
        """
        direction, distance = self._parse_rotation(rotation)

        clicks = 0

        for _ in range(distance):
            old_pos = self.position
            self.position += direction

            # Handle wrapping
            if self.position > MAX:
                self.position = MIN
            elif self.position < MIN:
                self.position = MAX

            # Count if we hit or crossed zero
            if old_pos != MIN and self.position == MIN:
                clicks += 1

        return self.position, clicks
    # endregion
    ################################################################################

    ################################################################################
    # region PRIVATE INTERFACE
    def _parse_rotation(self, rotation: str) -> tuple[int, int]:
        """Parse the rotation instruction and return direction and distance"""
        parts = re.findall(r'[A-Z]+|\d+', rotation)
        if len(parts) != 2:
            raise ValueError(f"Invalid rotation format: {rotation}")

        direction_str, distance_str = parts

        match direction_str:
            case "R":
                direction = 1
            case "L":
                direction = -1
            case _:
                raise ValueError(f"Invalid direction: {direction_str}")

        return direction, int(distance_str)
    # endregion
    ################################################################################
