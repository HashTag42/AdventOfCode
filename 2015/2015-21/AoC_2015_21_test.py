from AoC_2015_21 import solve_part1, solve_part2, get_data
import pytest

test_cases = [
    # filename, expected
    ('./2015/2015-21/input.txt', [91, 0]),
]


@pytest.mark.parametrize("filename, expected", test_cases)
def test_solve_part1(filename, expected):
    boss_hp, boss_damage, boss_armor = get_data(filename)
    assert solve_part1(boss_hp, boss_damage, boss_armor) == expected[0]


@pytest.mark.parametrize("filename, expected", test_cases)
def test_solve_part2(filename, expected):
    assert solve_part2(get_data(filename)) == expected[1]
