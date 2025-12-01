from Dial import Dial
import pytest


def test_Dial__init__():
    dial = Dial()
    assert isinstance(dial, Dial) is True


rotate_test_cases = [
    # rotation, expected
    ("L10", 40),
    ("L50", 0),
    ("L51", 99),
    ("L52", 98),
    ("R10", 60),
    ("R49", 99),
    ("R50", 0),
    ("R51", 1),
]


@pytest.mark.parametrize("rotation, expected", rotate_test_cases)
def test_Dial_rotate(rotation, expected):
    dial = Dial()
    assert dial.rotate(rotation) == expected


rotate_raises_test_cases = [
    # rotation
    ("1"),
    ("A"),
    ("A5"),
    ("5B"),
    ("LR5"),
]


@pytest.mark.parametrize("rotation", rotate_raises_test_cases)
def test_Dial_rotate_raises(rotation):
    dial = Dial()
    with pytest.raises(ValueError):
        dial.rotate(rotation)
