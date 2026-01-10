'''
Advent of Code 2016 - Day 10: Balance Bots
Puzzle: https://adventofcode.com/2016/day/10
'''
from pathlib import Path


def solve(filename: str, search_ids: list[int]) -> tuple[int, int]:
    lines = get_data(filename)
    return solve_part1(lines, search_ids), solve_part2(lines, search_ids)


def solve_part1(lines: list[str], search_ids: list[int]) -> int:
    target = tuple(sorted(search_ids))
    bots: dict[int, list[int]] = {}
    bins: dict[int, list[int]] = {}

    # Process the initial/'value' instructions
    value_instructions: list[str] = [line for line in lines if line.split()[0] == 'value']
    for instruction in value_instructions:
        # example: 'value 5 goes to bot 2'
        tokens: list[str] = instruction.split()
        chip_id, bot_id = int(tokens[1]), int(tokens[5])
        bots.setdefault(bot_id, []).append(chip_id)

    # Process the action/'bot' instructions
    rules: dict[int, tuple[str, int, str, int]] = {}
    bot_instructions: list[str] = [line for line in lines if line.split()[0] == 'bot']
    for instruction in bot_instructions:
        # example: 'bot 1 gives low to output 1 and high to bot 0'
        tokens: list[str] = instruction.split()
        bot_id, low_type, low_id, high_type, high_id = (
            int(tokens[1]), tokens[5], int(tokens[6]), tokens[10], int(tokens[11])
        )
        rules[bot_id] = (low_type, low_id, high_type, high_id)

    while True:
        # Find a bot with exactly 2 chips
        acting_bot_id = find_acting_bot(bots)
        if acting_bot_id is None:
            break

        if acting_bot_id is None:
            # No more bots can act
            break

        chips = sorted(bots[acting_bot_id])
        low, high = chips

        # Check if this bot is comparing the target pair
        if (low, high) == target:
            return acting_bot_id

        if acting_bot_id not in rules:
            raise KeyError(f'No rule for bot {acting_bot_id}')
        low_type, low_id, high_type, high_id = rules[acting_bot_id]

        # Give low chip
        if low_type == 'bot':
            bots.setdefault(low_id, []).append(low)
        else:  # 'output'
            bins.setdefault(low_id, []).append(low)

        # Give high chip
        if high_type == 'bot':
            bots.setdefault(high_id, []).append(high)
        else:  # 'output'
            bins.setdefault(high_id, []).append(high)

        # Clear this bot's chips
        bots[acting_bot_id] = []

    raise ValueError('No bot compared the target chip IDs.')


def find_acting_bot(bots: dict[int, list[int]]) -> int | None:
    for b_id, chips in bots.items():
        if len(chips) == 2:
            return b_id
    return None


def solve_part2(lines: list[str], search_ids: list[int]) -> int:
    bots: dict[int, list[int]] = {}
    bins: dict[int, list[int]] = {}

    # Process value instructions
    value_instructions = [line for line in lines if line.split()[0] == 'value']
    for instruction in value_instructions:
        tokens = instruction.split()
        chip_id, bot_id = int(tokens[1]), int(tokens[5])
        bots.setdefault(bot_id, []).append(chip_id)

    # Process bot rules
    rules: dict[int, tuple[str, int, str, int]] = {}
    bot_instructions = [line for line in lines if line.split()[0] == 'bot']
    for instruction in bot_instructions:
        tokens = instruction.split()
        bot_id, low_type, low_id, high_type, high_id = (
            int(tokens[1]), tokens[5], int(tokens[6]), tokens[10], int(tokens[11])
        )
        rules[bot_id] = (low_type, low_id, high_type, high_id)

    # Run full simulation (no early exit)
    while True:
        acting_bot_id = find_acting_bot(bots)
        if acting_bot_id is None:
            break

        chips = sorted(bots[acting_bot_id])
        low, high = chips

        if acting_bot_id not in rules:
            raise KeyError(f"No rule for bot {acting_bot_id}")
        low_type, low_id, high_type, high_id = rules[acting_bot_id]

        # Give low chip
        if low_type == 'bot':
            bots.setdefault(low_id, []).append(low)
        else:
            bins.setdefault(low_id, []).append(low)

        # Give high chip
        if high_type == 'bot':
            bots.setdefault(high_id, []).append(high)
        else:
            bins.setdefault(high_id, []).append(high)

        bots[acting_bot_id] = []

    # After simulation, compute product of outputs 0, 1, 2
    return bins[0][0] * bins[1][0] * bins[2][0]


def get_data(filename: str) -> list[str]:
    return Path(filename).read_text().splitlines()


if __name__ == '__main__':
    input_file, search_ids = './2016/2016-10/example.txt', [2, 5]
    result1, result2 = solve(input_file, search_ids)
    print(f'{input_file=}: Results: {result1=}, {result2=}')

    input_file, search_ids = './2016/2016-10/input.txt', [17, 61]
    result1, result2 = solve(input_file, search_ids)
    print(f'{input_file=}: Results: {result1=}, {result2=}')
