'''
Advent of Code 2015 - Day 16: Aunt Sue
Puzzle: https://adventofcode.com/2015/day/16
'''


class Sue:
    def __init__(self, line: str = "") -> None:
        self.id: int = -1
        self.akitas: int = -1
        self.cars: int = -1
        self.cats: int = -1
        self.children: int = -1
        self.goldfish: int = -1
        self.perfumes: int = -1
        self.pomeranians: int = -1
        self.samoyeds: int = -1
        self.trees: int = -1
        self.vizslas: int = -1
        self.update_categories(line)

    def compare1(self, other: 'Sue') -> int:
        score = 0
        attrs = ['akitas', 'cars', 'cats', 'children', 'goldfish',
                 'perfumes', 'pomeranians', 'samoyeds', 'trees', 'vizslas']
        for attr in attrs:
            self_val = getattr(self, attr)
            other_val = getattr(other, attr)
            if self_val != -1 and other_val != -1 and self_val == other_val:
                score += 1
        return score

    def compare2(self, other: 'Sue') -> int:
        score = 0
        if self.akitas != -1 and other.akitas != -1 and self.akitas == other.akitas:
            score += 1
        if self.cars != -1 and other.cars != -1 and self.cars == other.cars:
            score += 1
        if self.cats != -1 and other.cats != -1 and self.cats > other.cats:
            score += 1
        if self.children != -1 and other.children != -1 and self.children == other.children:
            score += 1
        if self.goldfish != -1 and other.goldfish != -1 and self.goldfish < other.goldfish:
            score += 1
        if self.perfumes != -1 and other.perfumes != -1 and self.perfumes == other.perfumes:
            score += 1
        if self.pomeranians != -1 and other.pomeranians != -1 and self.pomeranians < other.pomeranians:
            score += 1
        if self.samoyeds != -1 and other.samoyeds != -1 and self.samoyeds == other.samoyeds:
            score += 1
        if self.trees != -1 and other.trees != -1 and self.trees > other.trees:
            score += 1
        if self.vizslas != -1 and other.vizslas != -1 and self.vizslas == other.vizslas:
            score += 1
        return score

    def update_categories(self, line: str) -> None:
        # parse line
        # example: "Sue 1: goldfish: 6, trees: 9, akitas: 0"
        if len(line) > 0:
            parts = line.split()
            self.id: int = int(parts[1].rstrip(':'))
            self.update_category(parts[2].rstrip(':'), int(parts[3].rstrip(',')))
            self.update_category(parts[4].rstrip(':'), int(parts[5].rstrip(',')))
            self.update_category(parts[6].rstrip(':'), int(parts[7]))

    def update_category(self, category: str, number: int) -> None:
        match category:
            case "akitas":
                self.akitas = number
            case "cars":
                self.cars = number
            case "cats":
                self.cats = number
            case "children":
                self.children = number
            case "goldfish":
                self.goldfish = number
            case "perfumes":
                self.perfumes = number
            case "pomeranians":
                self.pomeranians = number
            case "samoyeds":
                self.samoyeds = number
            case "trees":
                self.trees = number
            case "vizslas":
                self.vizslas = number
            case _:
                raise ValueError(f"Unknown category: {category}")


def solve_2015_16(filename: str) -> tuple[int, int]:
    sues: list[Sue] = get_data(filename)
    return solve_part1(sues), solve_part2(sues)


the_sue = Sue()
the_sue.update_category("children", 3)
the_sue.update_category("cats", 7)
the_sue.update_category("samoyeds", 2)
the_sue.update_category("pomeranians", 3)
the_sue.update_category("akitas", 0)
the_sue.update_category("vizslas", 0)
the_sue.update_category("goldfish", 5)
the_sue.update_category("trees", 3)
the_sue.update_category("cars", 2)
the_sue.update_category("perfumes", 1)


def solve_part1(sues: list[Sue]) -> int:
    for s in sues:
        if s.compare1(the_sue) == 3:
            return s.id
    return -1


def solve_part2(sues) -> int:
    for s in sues:
        if s.compare2(the_sue) == 3:
            return s.id
    return -1


def get_data(filename: str) -> list[Sue]:
    with open(filename, 'r') as file:
        return [Sue(line) for line in file]


if __name__ == "__main__":
    import pytest
    import sys
    sys.exit(pytest.main(['-v', './2015/2015-16/AoC_2015_16_test.py']))
