import re

# Dial constants
MIN = 0
START = 50
MAX = 99


class Dial():
    ################################################################################
    # region CONSTRUCTOR
    def __init__(self, start: int = START, min: int = MIN, max: int = MAX) -> None:
        assert min < start < max, "START must be between MIN and MAX"
        self.position: int = start
        self._start: int = start
        self._min: int = min
        self._max: int = max
        self._length: int = max - min + 1
        assert self._length > 0, "LENGTH must be greater than zero"
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
            if self.position > self._max:
                self.position = self._min
            elif self.position < self._min:
                self.position = self._max

            # Count if we hit or crossed zero
            if old_pos != self._min and self.position == self._min:
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


if __name__ == "__main__":
    import pytest
    import sys
    sys.exit(pytest.main(['-v', './2025/01/Dial_test.py']))
