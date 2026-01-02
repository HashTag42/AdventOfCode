from Ingredient import Ingredient


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
        for ingredient, amount in self.ingredients.items():
            string += f"{ingredient} = {amount}"
        return string
