# Puzzle: https://adventofcode.com/2024/day/3

import logging
import os
import re

logging.basicConfig(level=logging.ERROR, format='%(levelname)s: %(message)s')

################################################################################
def main():
    process_file("inputTest.txt")
    process_file("input.txt")
################################################################################

################################################################################
def process_file(filename):
    logging.info(f"Processing file: {filename}...")

    total = 0
    with open(f"{os.path.dirname(__file__)}\\{filename}", 'r') as file:
        text = file.read()
        logging.debug(f"Content: {text}")

        match = re.findall(r'mul\(\d+,\d+\)', text)
        if match:
            logging.debug(match)
            for m in match:
                logging.debug(m)
                numbers = re.findall(r'\d+', m)
                total += int(numbers[0]) * int(numbers[1])

    print(f"File: {filename}. Part 1 result = {total}")
################################################################################

################################################################################
if __name__ == "__main__":
    main()
################################################################################