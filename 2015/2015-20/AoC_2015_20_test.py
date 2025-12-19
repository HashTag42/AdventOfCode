from AoC_2015_20 import solve_part1, solve_part2
import pytest

test_cases = [
    # input, expected
    (36000000, [831600, 884520]),
]


@pytest.mark.parametrize("input, expected", test_cases)
def test_solve_part1(input, expected):
    assert solve_part1(input) == expected[0]


@pytest.mark.parametrize("input, expected", test_cases)
def test_solve_part2(input, expected):
    assert solve_part2(input) == expected[1]
