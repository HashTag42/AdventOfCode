from AoC_2016_10 import solve_part1, solve_part2, get_data
import pytest

test_cases = [
    # filename, chip_ids, expected
    ('./2016/2016-10/example.txt', [2, 5], [2, 0]),
    ('./2016/2016-10/input.txt', [17, 61], [147, 0]),
]


@pytest.mark.parametrize("filename, chip_ids, expected", test_cases)
def test_solve_part1(filename, chip_ids, expected):
    assert solve_part1(get_data(filename), chip_ids) == expected[0]


@pytest.mark.parametrize("filename, chip_ids, expected", test_cases)
def test_solve_part2(filename, chip_ids, expected):
    assert solve_part2(get_data(filename), chip_ids) == expected[1]
