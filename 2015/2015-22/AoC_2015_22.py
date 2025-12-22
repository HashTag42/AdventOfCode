'''
Advent of Code 2015 - Day 22: Wizard Simulator 20XX
Puzzle: https://adventofcode.com/2015/day/22
'''
import heapq
from dataclasses import dataclass

SPELLS = {
    'magic_missile': {'cost': 53, 'damage': 4, 'heal': 0},
    'drain': {'cost': 73, 'damage': 2, 'heal': 2},
    'shield': {'cost': 113, 'damage': 0, 'heal': 0},
    'poison': {'cost': 173, 'damage': 0, 'heal': 0},
    'recharge': {'cost': 229, 'damage': 0, 'heal': 0},
}

player_hp = 50
player_mana = 500


@dataclass(frozen=True, slots=True)
class GameState:
    player_hp: int
    player_mana: int
    boss_hp: int
    boss_damage: int
    shield_timer: int = 0
    poison_timer: int = 0
    recharge_timer: int = 0
    mana_spent: int = 0

    def get_armor(self) -> int:
        return 7 if self.shield_timer > 0 else 0

    def apply_effects(self) -> 'GameState':
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

    def can_cast(self, spell_name) -> bool:
        """Check if a spell can be cast.
        Note: Called after apply_effects(), so timer=0 means effect
        just ended and can be recast this turn.
        """
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

    def cast_spell(self, spell_name) -> 'GameState':
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

    def boss_attack(self, armor) -> 'GameState':
        """Boss attacks player, return new state."""
        damage = max(1, self.boss_damage - armor)
        return GameState(
            self.player_hp - damage, self.player_mana, self.boss_hp, self.boss_damage,
            self.shield_timer, self.poison_timer, self.recharge_timer, self.mana_spent
        )


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
