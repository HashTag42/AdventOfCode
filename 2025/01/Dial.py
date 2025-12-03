import re

# Dial constants
MIN = 0
START = 50
MAX = 99
LENGTH = MAX - MIN + 1


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
        Rotate the dial according to the rotation instruction
        Returns the updated position and number of 'clicks' (zero hits)
        """

        direction, distance = self._parse_rotation(rotation)

        quotient, remainder = divmod(distance, LENGTH)
        clicks = quotient

        # Rotate the dial
        self.position += direction * remainder

        #  Correct the position if gone past MAX or below MIN
        if self.position < MIN:
            self.position += LENGTH
            clicks += 1
        elif self.position > MAX:
            self.position -= LENGTH
            clicks += 1

        return self.position, clicks
    # endregion
    ################################################################################

    ################################################################################
    # region PRIVATE INTERFACE
    def _parse_rotation(self, rotation: str) -> tuple[int, int]:
        """Parse the rotation instruction and return direction and distance"""
        match = re.match(r'([A-Z])(\d+)', rotation)
        if match:
            direction_str, distance = match.groups()
        else:
            raise ValueError("Unrecognized rotation instruction")

        match(direction_str):
            case "R":
                direction_int = 1
            case "L":
                direction_int = -1
            case _:
                raise ValueError("Unrecognized direction")

        return direction_int, int(distance)
    # endregion
    ################################################################################
