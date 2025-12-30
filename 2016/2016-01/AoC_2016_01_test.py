from AoC_2016_01 import solve
import pytest

test_cases = [
    # filename, expected
    ('./2016/2016-01/example.txt', [12, 0]),
    ('./2016/2016-01/input.txt', [271, 153]),
]


@pytest.mark.parametrize("filename, expected", test_cases)
def test_solve(filename, expected):
    assert solve(filename) == (expected[0], expected[1])
