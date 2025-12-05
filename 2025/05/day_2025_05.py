'''
Advent of Code 2025 - Day 5:Cafeteria
Puzzle: https://adventofcode.com/2025/day/5
'''


def solve_2025_05(file: str) -> tuple[int, int]:
    ranges_num, ingredients = get_data(file)
    return solve_part1(ranges_num, ingredients), solve_part2(ranges_num)


def solve_part1(ranges_num: list[tuple[int, int]], ingredients: list[str]) -> int:
    count = 0
    for i in ingredients:
        for r in ranges_num:
            if r[0] <= int(i) <= r[1]:
                count += 1
                break
    return count


def solve_part2(ranges_num: list[tuple[int, int]]) -> int:
    sorted_ranges = sorted(ranges_num)
    merged = [sorted_ranges[0]]
    for current in sorted_ranges[1:]:
        last = merged[-1]
        if current[0] <= last[1] + 1:
            merged[-1] = (last[0], max(last[1], current[1]))
        else:
            merged.append(current)
    count = 0
    for m in merged:
        count += m[1] - m[0] + 1
    return count


def get_data(file: str) -> tuple[list[tuple[int, int]], list[str]]:
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
        ranges_num: list[tuple[int, int]] = []
        for r_str in ranges:
            start, end = map(int, r_str.split('-'))
            ranges_num.append((start, end))
        return ranges_num, ingredients


if __name__ == "__main__":
    import pytest
    import sys
    sys.exit(pytest.main(['-v', './2025/05/day_2025_05_test.py']))
