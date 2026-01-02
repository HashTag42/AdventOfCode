'''
Advent of Code 2015 - Day 15: Science for Hungry People
Puzzle: https://adventofcode.com/2015/day/15
'''
from Ingredient import Ingredient
from Cookie import Cookie


def solve_2015_15(filename: str) -> tuple[int, int]:
    ingredients: list[Ingredient] = get_data(filename)
    return solve_part(ingredients, 1), solve_part(ingredients, 2)


def solve_part(ingredients: list[Ingredient], part: int) -> int:
    max_score, TOTAL = 0, 100
    if len(ingredients) == 2:
        for i1 in range(TOTAL + 1):
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
                for c in range(TOTAL - a - b + 1):
                    d = TOTAL - a - b - c
                    cookie = Cookie({ingredients[0]: a, ingredients[1]: b, ingredients[2]: c, ingredients[3]: d})
                    cookie_score1, cookie_score2 = cookie.score()
                    if part == 1:
                        max_score = max(max_score, cookie_score1)
                    else:   # part == 2
                        max_score = max(max_score, cookie_score2)
    return max_score


def get_data(filename: str) -> list[Ingredient]:
    with open(filename, 'r') as file:
        return [Ingredient(line) for line in file]


if __name__ == "__main__":
    import pytest
    import sys
    sys.exit(pytest.main(['-v', './2015/2015-15/AoC_2015_15_test.py']))
