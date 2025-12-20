'''
Advent of Code 2015 - Day 22: Wizard Simulator 20XX
Puzzle: https://adventofcode.com/2015/day/22
'''

import heapq
from dataclasses import dataclass

SPELLS = {
    'magic_missile': {'cost': 53, 'damage': 4, 'heal': 0, 'effect': None},
    'drain': {'cost': 73, 'damage': 2, 'heal': 2, 'effect': None},
    'shield': {'cost': 113, 'damage': 0, 'heal': 0, 'effect': ('shield', 6)},
    'poison': {'cost': 173, 'damage': 0, 'heal': 0, 'effect': ('poison', 6)},
    'recharge': {'cost': 229, 'damage': 0, 'heal': 0, 'effect': ('recharge', 5)},
}


@dataclass(frozen=True)
class GameState:
    player_hp: int
    player_mana: int
    boss_hp: int
    boss_damage: int
    shield_timer: int = 0
    poison_timer: int = 0
    recharge_timer: int = 0
    mana_spent: int = 0

    def get_armor(self):
        return 7 if self.shield_timer > 0 else 0

    def apply_effects(self):
        """Apply all active effects and return new state."""
        new_boss_hp = self.boss_hp - (3 if self.poison_timer > 0 else 0)
        new_mana = self.player_mana + (101 if self.recharge_timer > 0 else 0)

        return GameState(
            self.player_hp, new_mana, new_boss_hp, self.boss_damage,
            max(0, self.shield_timer - 1),
            max(0, self.poison_timer - 1),
            max(0, self.recharge_timer - 1),
            self.mana_spent
        )

    def can_cast(self, spell_name):
        """Check if a spell can be cast."""
        spell = SPELLS[spell_name]
        if self.player_mana < spell['cost']:
            return False
        if spell_name == 'shield' and self.shield_timer > 0:
            return False
        if spell_name == 'poison' and self.poison_timer > 0:
            return False
        if spell_name == 'recharge' and self.recharge_timer > 0:
            return False
        return True

    def cast_spell(self, spell_name):
        """Cast a spell and return the new state."""
        spell = SPELLS[spell_name]

        new_shield = 6 if spell_name == 'shield' else self.shield_timer
        new_poison = 6 if spell_name == 'poison' else self.poison_timer
        new_recharge = 5 if spell_name == 'recharge' else self.recharge_timer

        return GameState(
            self.player_hp + spell['heal'],
            self.player_mana - spell['cost'],
            self.boss_hp - spell['damage'],
            self.boss_damage,
            new_shield, new_poison, new_recharge,
            self.mana_spent + spell['cost']
        )

    def boss_attack(self):
        """Boss attacks player, return new state."""
        damage = max(1, self.boss_damage - self.get_armor())
        return GameState(
            self.player_hp - damage, self.player_mana, self.boss_hp, self.boss_damage,
            self.shield_timer, self.poison_timer, self.recharge_timer, self.mana_spent
        )


def solve_part1(player_hp, player_mana, boss_hp, boss_damage) -> int | None:
    """Use Dijkstra's algorithm to find minimum mana to win."""
    initial_state = GameState(player_hp, player_mana, boss_hp, boss_damage)

    counter = 0
    pq = [(0, counter, initial_state)]
    visited = set()

    while pq:
        mana_spent, _, state = heapq.heappop(pq)

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
                boss_turn_state = new_state.apply_effects()

                if boss_turn_state.boss_hp <= 0:
                    counter += 1
                    heapq.heappush(pq, (boss_turn_state.mana_spent, counter, boss_turn_state))
                    continue

                # Boss attacks
                after_attack = boss_turn_state.boss_attack()

                if after_attack.player_hp > 0:
                    counter += 1
                    heapq.heappush(pq, (after_attack.mana_spent, counter, after_attack))

    return None


def solve_part2(data) -> int:
    result = 0
    return result


def get_data(filename: str) -> tuple[int, int]:
    """Parse boss stats from input file."""
    with open(filename) as f:
        lines = f.read().strip().split('\n')
    boss_hp = int(lines[0].split(': ')[1])
    boss_damage = int(lines[1].split(': ')[1])
    return boss_hp, boss_damage


if __name__ == "__main__":
    import pytest
    import sys
    sys.exit(pytest.main(['-v', './2015/2015-22/AoC_2015_22_test.py']))
