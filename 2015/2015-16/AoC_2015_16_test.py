from AoC_2015_16 import solve_part1, solve_part2, get_data, Sue
import pytest

solve_test_cases = [
    # filename, expected
    ('./2015/2015-16/input.txt', [103, 405]),
]


@pytest.mark.parametrize("filename, expected", solve_test_cases)
def test_solve_part1(filename, expected):
    assert solve_part1(get_data(filename)) == expected[0]


@pytest.mark.parametrize("filename, expected", solve_test_cases)
def test_solve_part2(filename, expected):
    assert solve_part2(get_data(filename)) == expected[1]


compare_test_cases = [
    # sue1, sue2, expected
    ("Sue 1: cars: 1, cats: 2, children: 3", "Sue 2: cars: 0, cats: 0, children: 0", 0),
    ("Sue 1: cars: 1, cats: 2, children: 3", "Sue 2: cars: 1, cats: 0, children: 0", 1),
    ("Sue 1: cars: 1, cats: 2, children: 3", "Sue 2: cars: 1, cats: 2, children: 0", 2),
    ("Sue 1: cars: 1, cats: 2, children: 3", "Sue 2: cars: 1, cats: 2, children: 3", 3),
    ("Sue 1: cars: 1, cats: 2, children: 3", "Sue 2: cars: 1, cats: 2, akitas: 3", 2),
]


@pytest.mark.parametrize("sue1, sue2, expected", compare_test_cases)
def test_Sue_compare1(sue1, sue2, expected):
    s1 = Sue(sue1)
    s2 = Sue(sue2)
    assert s1.compare1(s2) == expected
