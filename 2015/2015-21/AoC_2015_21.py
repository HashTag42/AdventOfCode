'''
Advent of Code 2015 - Day 21: RPG Simulator 20XX
Puzzle: https://adventofcode.com/2015/day/21
'''
from itertools import combinations

# Define items as (name, cost, damage, armor)
WEAPONS = [
    ("Dagger", 8, 4, 0),
    ("Shortsword", 10, 5, 0),
    ("Warhammer", 25, 6, 0),
    ("Longsword", 40, 7, 0),
    ("Greataxe", 74, 8, 0),
]

ARMOR = [
    ("None", 0, 0, 0),  # Option to buy no armor
    ("Leather", 13, 0, 1),
    ("Chainmail", 31, 0, 2),
    ("Splintmail", 53, 0, 3),
    ("Bandedmail", 75, 0, 4),
    ("Platemail", 102, 0, 5),
]

RINGS = [
    ("Damage +1", 25, 1, 0),
    ("Damage +2", 50, 2, 0),
    ("Damage +3", 100, 3, 0),
    ("Defense +1", 20, 0, 1),
    ("Defense +2", 40, 0, 2),
    ("Defense +3", 80, 0, 3),
]


def solve_part1(boss_hp, boss_damage, boss_armor):
    """Find minimum gold to win the fight."""
    player_hp = 100
    min_cost = float('inf')
    ring_combos = generate_ring_combinations()
    # Try all combinations
    for weapon in WEAPONS:
        for armor in ARMOR:
            for rings in ring_combos:
                # Calculate totals
                cost = weapon[1] + armor[1] + sum(r[1] for r in rings)
                damage = weapon[2] + armor[2] + sum(r[2] for r in rings)
                defense = weapon[3] + armor[3] + sum(r[3] for r in rings)
                # Check if we win
                if simulate_fight(player_hp, damage, defense, boss_hp, boss_damage, boss_armor):
                    min_cost = min(min_cost, cost)
    return min_cost


def simulate_fight(player_hp, player_damage, player_armor, boss_hp, boss_damage, boss_armor):
    """Returns True if player wins, False otherwise."""
    # Calculate damage per turn (minimum 1)
    player_deals = max(1, player_damage - boss_armor)
    boss_deals = max(1, boss_damage - player_armor)
    # Calculate turns to kill each other
    # Ceiling division: how many hits to reduce HP to 0?
    turns_to_kill_boss = (boss_hp + player_deals - 1) // player_deals
    turns_to_kill_player = (player_hp + boss_deals - 1) // boss_deals
    # Player wins if they kill boss in same or fewer turns
    # (player attacks first)
    return turns_to_kill_boss <= turns_to_kill_player


def generate_ring_combinations():
    """Generate all valid ring combinations (0, 1, or 2 rings)."""
    ring_combos = [()]  # No rings
    ring_combos += [(r,) for r in RINGS]  # One ring
    ring_combos += list(combinations(RINGS, 2))  # Two rings
    return ring_combos


def solve_part2(data) -> int:
    result = 0
    return result


def get_data(filename: str) -> tuple[int, int, int]:
    with open(filename, 'r') as file:
        data = file.read()
        lines = data.strip().split('\n')
        stats = {}
        for line in lines:
            key, value = line.split(': ')
            stats[key] = int(value)
        return stats['Hit Points'], stats['Damage'], stats['Armor']


if __name__ == "__main__":
    import pytest
    import sys
    sys.exit(pytest.main(['-v', './2015/2015-21/AoC_2015_21_test.py']))
