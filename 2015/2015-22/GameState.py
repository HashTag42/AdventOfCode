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
