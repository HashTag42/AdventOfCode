'''
Advent of Code 2016 - Day 10: Balance Bots
Puzzle: https://adventofcode.com/2016/day/10
'''
from pathlib import Path


def solve(filename: str, search_ids: list[int]) -> tuple[int, int]:
    lines = get_data(filename)
    return solve_part1(lines, search_ids), solve_part2(lines, search_ids)


def solve_part1(lines: list[str], search_ids: list[int]) -> int:
    target: tuple[int, int] = tuple(sorted(search_ids))  # type: ignore
    bot_id, _, _ = run_simulation(lines, target=target)
    if bot_id is None:
        raise ValueError("No bot compared the target chip IDs.")
    return bot_id


def solve_part2(lines: list[str], search_ids: list[int]) -> int:
    _, _, bins = run_simulation(lines, target=None)
    return bins[0][0] * bins[1][0] * bins[2][0]


def find_acting_bot(bots: dict[int, list[int]]) -> int | None:
    for b_id, chips in bots.items():
        if len(chips) == 2:
            return b_id
    return None


def run_simulation(lines: list[str], target: tuple[int, int] | None = None):
    bots: dict[int, list[int]] = {}
    bins: dict[int, list[int]] = {}

    # Parse value instructions
    value_instructions = [line for line in lines if line.startswith("value")]
    for instruction in value_instructions:
        tokens = instruction.split()
        chip_id, bot_id = int(tokens[1]), int(tokens[5])
        bots.setdefault(bot_id, []).append(chip_id)

    # Parse bot rules
    rules: dict[int, tuple[str, int, str, int]] = {}
    bot_instructions = [line for line in lines if line.startswith("bot")]
    for instruction in bot_instructions:
        tokens = instruction.split()
        bot_id = int(tokens[1])
        low_type, low_id = tokens[5], int(tokens[6])
        high_type, high_id = tokens[10], int(tokens[11])
        rules[bot_id] = (low_type, low_id, high_type, high_id)

    # Simulation loop
    while True:
        acting_bot_id = find_acting_bot(bots)
        if acting_bot_id is None:
            break

        chips = sorted(bots[acting_bot_id])
        low, high = chips

        # Part 1 early exit
        if target is not None and (low, high) == target:
            return acting_bot_id, bots, bins

        if acting_bot_id not in rules:
            raise KeyError(f"No rule for bot {acting_bot_id}")

        low_type, low_id, high_type, high_id = rules[acting_bot_id]

        # Give low chip
        if low_type == "bot":
            bots.setdefault(low_id, []).append(low)
        else:
            bins.setdefault(low_id, []).append(low)

        # Give high chip
        if high_type == "bot":
            bots.setdefault(high_id, []).append(high)
        else:
            bins.setdefault(high_id, []).append(high)

        bots[acting_bot_id] = []

    # Finished full simulation
    return None, bots, bins


def get_data(filename: str) -> list[str]:
    return Path(filename).read_text().splitlines()


if __name__ == '__main__':
    input_file, search_ids = './2016/2016-10/example.txt', [2, 5]
    result1, result2 = solve(input_file, search_ids)
    print(f'{input_file=}: Results: {result1=}, {result2=}')

    input_file, search_ids = './2016/2016-10/input.txt', [17, 61]
    result1, result2 = solve(input_file, search_ids)
    print(f'{input_file=}: Results: {result1=}, {result2=}')
