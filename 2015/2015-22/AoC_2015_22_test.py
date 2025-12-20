from AoC_2015_22 import solve_part1, solve_part2, get_data
import pytest

test_cases = [
    # filename, player_hp, player_mana, expected
    ('./2015/2015-22/input.txt', 50, 500, [900, 1216]),
]


@pytest.mark.parametrize("filename, player_hp, player_mana, expected", test_cases)
def test_solve_part1(filename, player_hp, player_mana, expected):
    boss_hp, boss_damage = get_data(filename)
    assert solve_part1(player_hp, player_mana, boss_hp, boss_damage) == expected[0]


@pytest.mark.parametrize("filename, player_hp, player_mana, expected", test_cases)
def test_solve_part2(filename, player_hp, player_mana, expected):
    boss_hp, boss_damage = get_data(filename)
    assert solve_part2(player_hp, player_mana, boss_hp, boss_damage) == expected[1]
