from AoC_2015_23 import (
    solve,
)
import pytest

test_cases = [
    # filename, register, expected
    ('./2015/2015-23/example.txt', 'a', [2, 7]),
    ('./2015/2015-23/input.txt', 'b', [170, 247]),
]


@pytest.mark.parametrize("filename, register, expected", test_cases)
def test_solve_part1(filename, register, expected):
    assert solve(filename, register, 1) == expected[0]


@pytest.mark.parametrize("filename, register, expected", test_cases)
def test_solve_part2(filename, register, expected):
    assert solve(filename, register, 2) == expected[1]
