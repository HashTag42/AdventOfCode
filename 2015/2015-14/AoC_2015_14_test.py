from AoC_2015_14 import solve_part1, solve_part2, get_data
import pytest

test_cases = [
    # filename, time, expected
    ('./2015/2015-14/example.txt', 1000, [1120, 689]),
    ('./2015/2015-14/input.txt', 2503, [2696, 1084]),
]


@pytest.mark.parametrize("filename, time, expected", test_cases)
def test_solve_part1(filename, time, expected):
    assert solve_part1(get_data(filename), time) == expected[0]


@pytest.mark.parametrize("filename, time, expected", test_cases)
def test_solve_part2(filename, time, expected):
    assert solve_part2(get_data(filename), time) == expected[1]
