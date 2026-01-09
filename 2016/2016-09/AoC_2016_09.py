'''
Advent of Code 2016 - Day 9: Explosives in Cyberspace
Puzzle: https://adventofcode.com/2016/day/9
'''
from pathlib import Path


def decompress(s: str) -> str:
    i = 0
    out = []
    while i < len(s):
        if s[i] != '(':
            out.append(s[i])
            i += 1
            continue
        # Parse marker
        j = s.index(')', i)
        a, b = map(int, s[i+1:j].split('x'))
        segment = s[j+1:j+1+a]
        out.append(segment * b)
        i = j + 1 + a
    return ''.join(out)


def solve(filename: str) -> tuple[int, int]:
    lines = get_data(filename)
    return solve_part1(lines), solve_part2(lines)


def solve_part1(lines: list[str]) -> int:
    total = 0
    for line in lines:
        total += len(decompress(line))
    return total


def solve_part2(lines: list[str]) -> int:
    result = 0
    return result


def get_data(filename: str) -> list[str]:
    return Path(filename).read_text().splitlines()


if __name__ == "__main__":
    input_files = [
        './2016/2016-09/example.txt',
        './2016/2016-09/input.txt',
    ]
    for input_file in input_files:
        result1, result2 = solve(input_file)
        print(f"{input_file=}: {result1=}, {result2=}")
