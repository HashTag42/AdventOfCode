'''
Advent of Code 2016 - Day 9: Explosives in Cyberspace
Puzzle: https://adventofcode.com/2016/day/9
'''
from pathlib import Path


def decompress_v1(s: str) -> str:
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


def decompressed_length(s: str, start: int = 0, end: int | None = None) -> int:
    if end is None:
        end = len(s)
    i = start
    total = 0
    while i < end:
        if s[i] != '(':
            total += 1
            i += 1
            continue
        # Parse marker
        j = s.index(')', i)
        a, b = map(int, s[i+1:j].split('x'))
        # Recursively compute length of the segment
        segment_len = decompressed_length(s, j+1, j+1+a)
        total += segment_len * b
        i = j + 1 + a
    return total


def solve(filename: str) -> tuple[int, int]:
    lines = get_data(filename)
    return solve_part1(lines), solve_part2(lines)


def solve_part1(lines: list[str]) -> int:
    total = 0
    for line in lines:
        total += len(decompress_v1(line))
    return total


def solve_part2(lines: list[str]) -> int:
    total = 0
    for line in lines:
        total += decompressed_length(line)
    return total


def get_data(filename: str) -> list[str]:
    return Path(filename).read_text().splitlines()


if __name__ == "__main__":
    input_files = [
        './2016/2016-09/example1.txt',
        './2016/2016-09/example2.txt',
        './2016/2016-09/input.txt',
    ]
    for input_file in input_files:
        result1, result2 = solve(input_file)
        print(f"{input_file=}: {result1=}, {result2=}")
