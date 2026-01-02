'''
Advent of Code 2015 - Day 22: Wizard Simulator 20XX
Puzzle: https://adventofcode.com/2015/day/22
'''
import heapq
from GameState import GameState, SPELLS, player_hp, player_mana


def solve(filename: str) -> tuple[int | None, int | None]:
    boss_hp, boss_damage = get_data(filename)
    result1 = solve_part1(player_hp, player_mana, boss_hp, boss_damage)
    result2 = solve_part2(player_hp, player_mana, boss_hp, boss_damage)
    return result1, result2


def solve_part1(player_hp, player_mana, boss_hp, boss_damage) -> int | None:
    return find_minimum_mana(player_hp, player_mana, boss_hp, boss_damage, hard_mode=False)


def solve_part2(player_hp, player_mana, boss_hp, boss_damage) -> int | None:
    return find_minimum_mana(player_hp, player_mana, boss_hp, boss_damage, hard_mode=True)


def find_minimum_mana(player_hp, player_mana, boss_hp, boss_damage, hard_mode=False) -> int | None:
    """Use Dijkstra's algorithm to find minimum mana to win."""
    initial_state = GameState(player_hp, player_mana, boss_hp, boss_damage)
    counter = 0
    pq = [(0, counter, initial_state)]
    visited = set()
    while pq:
        mana_spent, _, state = heapq.heappop(pq)
        # Hard mode: player loses 1 HP at start of their turn
        if hard_mode:
            state = GameState(
                state.player_hp - 1, state.player_mana, state.boss_hp, state.boss_damage,
                state.shield_timer, state.poison_timer, state.recharge_timer, state.mana_spent
            )
            if state.player_hp <= 0:
                continue  # Player died
        # Check visited AFTER hard mode penalty
        state_key = (state.player_hp, state.player_mana, state.boss_hp,
                     state.shield_timer, state.poison_timer, state.recharge_timer)
        if state_key in visited:
            continue
        visited.add(state_key)
        # Player turn: apply effects
        state = state.apply_effects()
        if state.boss_hp <= 0:
            return mana_spent
        # Try each spell
        for spell_name in SPELLS:
            if state.can_cast(spell_name):
                new_state = state.cast_spell(spell_name)
                if new_state.boss_hp <= 0:
                    return new_state.mana_spent
                # Boss turn: apply effects
                armor = new_state.get_armor()  # Armor based on timer BEFORE decrement
                boss_turn_state = new_state.apply_effects()
                if boss_turn_state.boss_hp <= 0:
                    return boss_turn_state.mana_spent  # Boss died from effects
                # Boss attacks
                after_attack = boss_turn_state.boss_attack(armor)
                if after_attack.player_hp > 0:
                    counter += 1
                    heapq.heappush(pq, (after_attack.mana_spent, counter, after_attack))
    return None


def get_data(filename: str) -> tuple[int, int]:
    """Parse boss stats from input file."""
    with open(filename) as f:
        lines = f.read().strip().split('\n')
    boss_hp = int(lines[0].split(': ')[1])
    boss_damage = int(lines[1].split(': ')[1])
    return boss_hp, boss_damage


if __name__ == "__main__":
    result1, result2 = solve('./2015/2015-22/input.txt')
    print(f"Part 1: {result1}, Part 2: {result2}")
