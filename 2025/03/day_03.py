'''
Advent of Code 2025 - Day 3: Lobby
Puzzle: https://adventofcode.com/2025/day/3
'''


def get_total_ouput(file: str) -> tuple[int, int]:
    with open(file, 'r') as f:
        banks = f.readlines()
    part1 = part2 = 0
    for bank in banks:
        bank = bank.strip()
        part1 += get_bank_max_joltage(bank, 2)
        part2 += get_bank_max_joltage(bank, 12)
    return part1, part2


def get_bank_max_joltage(bank: str, batteries: int) -> int:
    result = []
    start = 0
    for i in range(batteries):
        needed = batteries - i - 1
        search = len(bank) - needed
        digits = [(bank[pos], pos) for pos in range(start, search)]
        max_digit, max_pos = max(digits, key=lambda x: x[0])
        result.append(max_digit)
        start = max_pos + 1
    return int(''.join(result))


if __name__ == "__main__":
    import pytest
    import sys
    sys.exit(pytest.main(['-v', './2025/03/day_03_test.py']))
