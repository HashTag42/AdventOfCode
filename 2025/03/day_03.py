'''
Advent of Code 2025 - Day 3: Lobby
Puzzle: https://adventofcode.com/2025/day/3
'''


def get_file_total_ouput(file: str) -> int:
    with open(file, 'r') as f:
        banks = f.readlines()
    part1 = 0
    for bank in banks:
        part1 += get_bank_max_joltage(bank)
    return part1


def get_bank_max_joltage(bank: str) -> int:
    max_joltage = 0
    length = len(bank) - 1
    for i in range(length):
        for j in range(i + 1, length + 1):
            joltage = int(bank[i] + bank[j])
            if joltage > max_joltage:
                max_joltage = joltage
    return max_joltage


if __name__ == "__main__":

    get_bank_max_joltage_test_cases = [
        # bank, expected_max_joltage
        ("987654321111111", 98),
        ("811111111111119", 89),
        ("234234234234278", 78),
        ("818181911112111", 92),
    ]

    for test in get_bank_max_joltage_test_cases:
        actual = get_bank_max_joltage(test[0])
        expected = test[1]
        assert actual == expected, f"{actual} != {expected}"

    get_file_total_output_test_cases = [
        # file, expected_part1
        ('./2025/03/example.txt', 357),
        # ('./2025/03/input.txt', 0),
    ]

    for test in get_file_total_output_test_cases:
        actual = get_file_total_ouput(test[0])
        expected_part1 = test[1]
        assert actual == expected_part1, f"{actual} != {expected_part1}"
