# Puzzle: https://adventofcode.com/2024/day/3

# --- Day 3: Mull It Over ---
# --- Part One ---
# "Our computers are having issues, so I have no idea if we have any Chief Historians in stock! You're welcome to check
# the warehouse, though," says the mildly flustered shopkeeper at the North Pole Toboggan Rental Shop. The Historians
# head out to take a look.
# The shopkeeper turns to you. "Any chance you can see why our computers are having issues again?"
# The computer appears to be trying to run a program, but its memory (your puzzle input) is corrupted. All of the
# instructions have been jumbled up!
# It seems like the goal of the program is just to multiply some numbers. It does that with instructions like mul(X,Y),
# where X and Y are each 1-3 digit numbers. For instance, mul(44,46) multiplies 44 by 46 to get a result of 2024.
# Similarly, mul(123,4) would multiply 123 by 4.
# However, because the program's memory has been corrupted, there are also many invalid characters that should be
# ignored, even if they look like part of a mul instruction. Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 )
# do nothing.
# For example, consider the following section of corrupted memory:
# xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
# Only the four highlighted sections are real mul instructions. Adding up the result of each instruction produces
# 161 (2*4 + 5*5 + 11*8 + 8*5).
# Scan the corrupted memory for uncorrupted mul instructions. What do you get if you add up all of the results of the
# multiplications?
# Puzzle Input: https://adventofcode.com/2024/day/3/input
# Your puzzle answer was 180233229.
# The first half of this puzzle is complete! It provides one gold star: *
# --- Part Two ---
# As you scan through the corrupted memory, you notice that some of the conditional statements are also still intact.
# If you handle some of the uncorrupted conditional statements in the program, you might be able to get an even more
# accurate result.
# There are two new instructions you'll need to handle:
# The do() instruction enables future mul instructions.
# The don't() instruction disables future mul instructions.
# Only the most recent do() or don't() instruction applies. At the beginning of the program, mul instructions are
# enabled.
# For example:
# xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
# This corrupted memory is similar to the example from before, but this time the mul(5,5) and mul(11,8) instructions are
# disabled because there is a don't() instruction before them. The other mul instructions function normally,
# including the one at the end that gets re-enabled by a do() instruction.
# This time, the sum of the results is 48 (2*4 + 8*5).
# Handle the new instructions; what do you get if you add up all of the results of just the enabled multiplications?
# Puzzle Input: https://adventofcode.com/2024/day/3/input


import logging
import os
import re

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


################################################################################
def main():
    calculate_part1("inputTest.txt")    # 161
    calculate_part1("input.txt")        # 180233229
    calculate_part2("inputTest2.txt")   # 48
    calculate_part2("input.txt")        # 95411583
################################################################################


################################################################################
def calculate_part1(filename):
    filepath = f"{os.path.dirname(__file__)}\\{filename}"
    logging.debug(f"Processing part 1 of file: [{filepath}]...")

    with open(filepath, 'r') as file:
        text = file.read()
        total = addup_muls(text)

    print(f"File: [{filename}]. Part 1 result = {total}")
################################################################################


################################################################################
def calculate_part2(filename):
    filepath = f"{os.path.dirname(__file__)}\\{filename}"
    logging.debug(f"Processing part 2 of file: [{filepath}]...")

    with open(filepath, 'r') as file:
        text = file.read()
        total_muls = 0
        index = 0
        enabled = True
        while (index < len(text)):
            if enabled:
                start_dont = text.find("don't()", index)
                if start_dont == -1:
                    start_dont = len(text)
                total_muls += addup_muls(text[index:start_dont])
                index = start_dont + 7
                enabled = False
            else:
                start_do = text.find("do()", index)
                if start_do == -1:
                    break
                else:
                    index = start_do + 4
                    enabled = True

    print(f"File: [{filename}]. Part 2 result = {total_muls}")
################################################################################


################################################################################
def addup_muls(text):
    logging.debug(f"addup_muls text: [{text}]")
    total = 0
    match = re.findall(r'mul\(\d+,\d+\)', text)
    if match:
        logging.debug(match)
        for m in match:
            logging.debug(f"Substring: [{m}]")
            numbers = re.findall(r'\d+', m)
            total += int(numbers[0]) * int(numbers[1])
    return total
################################################################################


################################################################################
if __name__ == "__main__":
    main()
################################################################################
