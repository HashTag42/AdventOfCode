from AoC_2015_12 import solve_part1, solve_part2, get_data
import pytest

test_cases = [
    # filename, expected
    ('./2015/2015-12/input.txt', [191164, 87842]),
]


@pytest.mark.parametrize("filename, expected", test_cases)
def test_solve_part1(filename, expected):
    data, json_data = get_data(filename)
    assert solve_part1(data) == expected[0]


@pytest.mark.parametrize("filename, expected", test_cases)
def test_solve_part2(filename, expected):
    data, json_data = get_data(filename)
    assert solve_part2(json_data) == expected[1]
