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

    get_bank_max_joltage_test_cases = [
        # bank, expected_part1, expected_part2
        ("987654321111111", 98, 987654321111),
        ("811111111111119", 89, 811111111119),
        ("234234234234278", 78, 434234234278),
        ("818181911112111", 92, 888911112111),
    ]

    get_total_output_test_cases = [
        # file, expected_part1, expected_part2
        ('./2025/03/example.txt', 357, 3121910778619),
        ('./2025/03/input.txt', 17346, 172981362045136),
    ]

    for test in get_bank_max_joltage_test_cases:
        assert get_bank_max_joltage(test[0], 2) == test[1]
        assert get_bank_max_joltage(test[0], 12) == test[2]

    for test in get_total_output_test_cases:
        part1, part2 = get_total_ouput(test[0])
        assert part1 == test[1]
        assert part2 == test[2]
