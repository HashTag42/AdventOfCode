from Dial import Dial, START
import pytest


def test_Dial__init__():
    dial = Dial()
    assert isinstance(dial, Dial) is True
    assert dial.position == START


rotate_test_cases = [
    # rotation, expected_position, expected_clicks
    ("L10", 40, 0),
    ("L50", 0, 1),
    ("L51", 99, 1),
    ("L52", 98, 1),
    ("L100", 50, 1),
    ("L210", 40, 2),
    ("R10", 60, 0),
    ("R49", 99, 0),
    ("R50", 0, 1),
    ("R51", 1, 1),
    ("R100", 50, 1),
    ("R210", 60, 2),
    ("R250", 0, 3),
    ("R1000", 50, 10),
]


@pytest.mark.parametrize("rotation, expected_position, expected_clicks", rotate_test_cases)
def test_Dial_rotate(rotation: str, expected_position: int, expected_clicks: int):
    dial = Dial()
    position, clicks = dial.rotate(rotation)
    assert position == expected_position
    assert clicks == expected_clicks


rotate_raises_test_cases = [
    # rotation
    ("A"),      # Missing distance
    ("1"),      # Missing direction
    ("5B"),     # Missing direction
    ("A5"),     # Incorrect direction
    ("LR5"),    # Incorrect direction
    ("L5R"),    # Incorrect distance
]


@pytest.mark.parametrize("rotation", rotate_raises_test_cases)
def test_Dial_rotate_raises(rotation: str):
    dial = Dial()
    with pytest.raises(ValueError):
        dial.rotate(rotation)
