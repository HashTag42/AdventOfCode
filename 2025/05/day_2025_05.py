'''
Advent of Code 2025 - Day 5:Cafeteria
Puzzle: https://adventofcode.com/2025/day/5
'''


def solve_2025_05(file: str) -> tuple[int, int]:
    with open(file, 'r') as f:
        ranges: list[str] = []
        ingredients: list[str] = []
        section = False
        for line in f.readlines():
            line = line.strip()
            if not section:
                if line == "":
                    section = True
                else:
                    ranges.append(line)
            else:
                ingredients.append(line)
        part1, part2 = solve_part1(ranges, ingredients), solve_part2()
        return part1, part2


def solve_part1(ranges_str: list[str], ingredients: list[str]) -> int:
    count = 0
    ranges_num = []
    for r_str in ranges_str:
        start, end = map(int, r_str.split('-'))
        ranges_num.append((start, end))
    for i in ingredients:
        for r in ranges_num:
            if r[0] <= int(i) <= r[1]:
                count += 1
                break
    return count


def solve_part2() -> int:
    return 0


if __name__ == "__main__":
    import pytest
    import sys
    sys.exit(pytest.main(['-v', './2025/05/day_2025_05_test.py']))
