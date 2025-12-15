'''
Advent of Code 2015 - Day 15: Science for Hungry People
Puzzle: https://adventofcode.com/2015/day/15
'''
from typing import Iterator


class Ingredient:
    def __init__(self, line: str) -> None:
        # Parse the line
        # Example: "Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8"
        parts = line.split()
        self.name: str = parts[0].rstrip(':')
        self.capacity: int = int(parts[2].rstrip(','))
        self.durability: int = int(parts[4].rstrip(','))
        self.flavor: int = int(parts[6].rstrip(','))
        self.texture: int = int(parts[8].rstrip(','))
        self.calories: int = int(parts[10])

    def __iter__(self) -> Iterator[int]:
        yield self.capacity
        yield self.durability
        yield self.flavor
        yield self.texture
        yield self.calories

    def __repr__(self) -> str:
        return (
            f"{self.name}: capacity {self.capacity}, "
            f"durability {self.durability}, flavor {self.flavor}, "
            f"texture {self.texture}, calories {self.calories}"
        )


class Cookie:
    def __init__(self, ingredients: dict[Ingredient, int]) -> None:
        self.ingredients: dict[Ingredient, int] = ingredients

    def score(self) -> tuple[int, int]:
        capacity, durability, flavor, texture, calories = 0, 0, 0, 0, 0
        for ingredient, amount in self.ingredients.items():
            capacity += ingredient.capacity * amount
            durability += ingredient.durability * amount
            flavor += ingredient.flavor * amount
            texture += ingredient.texture * amount
            calories += ingredient.calories * amount
        # Part 1 score does not include calories
        score1 = max(capacity, 0) * max(durability, 0) * max(flavor, 0) * max(texture, 0)
        score2 = 0
        if calories == 500:
            score2 = score1
        return score1, score2

    def __repr__(self) -> str:
        string = ""
        for ingredient, amount in self.ingredients:
            string += f"{ingredient} = {amount}"
        return string


def solve_2015_15(filename: str) -> tuple[int, int]:
    ingredients: list[Ingredient] = get_data(filename)
    return solve_part(ingredients, 1), solve_part(ingredients, 2)


def solve_part(ingredients: list[Ingredient], part: int) -> int:
    max_score, TOTAL = 0, 100
    if len(ingredients) == 2:
        for i1 in (range(TOTAL + 1)):
            i2 = TOTAL - i1
            cookie = Cookie({ingredients[0]: i1, ingredients[1]: i2})
            cookie_score1, cookie_score2 = cookie.score()
            if part == 1:
                max_score = max(max_score, cookie_score1)
            else:   # part == 2
                max_score = max(max_score, cookie_score2)
    else:   # len(ingredients) == 4
        for a in range(TOTAL + 1):
            for b in range(TOTAL - a):
                for c in range(TOTAL - a - b):
                    d = TOTAL - a - b - c
                    cookie = Cookie({ingredients[0]: a, ingredients[1]: b, ingredients[2]: c, ingredients[3]: d})
                    cookie_score1, cookie_score2 = cookie.score()
                    if part == 1:
                        max_score = max(max_score, cookie_score1)
                    else:   # part == 2
                        max_score = max(max_score, cookie_score2)
    return max_score


def get_data(filename: str) -> list[Ingredient]:
    ingredients: list[Ingredient] = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            ingredients.append(Ingredient(line))
        return ingredients


if __name__ == "__main__":
    import pytest
    import sys
    sys.exit(pytest.main(['-v', './2015/2015-15/AoC_2015_15_test.py']))
