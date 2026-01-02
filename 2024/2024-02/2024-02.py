# Puzzle: https://adventofcode.com/2024/day/2

import re
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s  %(levelname)s: %(message)s')


################################################################################
def main():
    process_file("inputTest.txt")   # Part 1 == 2, Part 2 ==
    process_file("input.txt")       # Part 1 == 686, Part 2 ==
################################################################################


################################################################################
def process_file(filename):
    logging.info(f"Processing file: {filename}...")

    safe_reports_part1 = 0
    safe_reports_part2 = 0

    with open(f"{os.path.dirname(__file__)}\\{filename}", 'r') as file:
        safe_reports_part1 = 0
        safe_reports_part2 = 0
        for line in file:
            logging.debug(f"Processing line: {line}")
            numbers = re.findall(r'\d+', line)  # The regular expression '\d+' matches one or more digits.
            if is_report_safe_part1(numbers):
                safe_reports_part1 += 1
            if is_report_safe_part2(numbers):
                safe_reports_part2 += 1

    print(f"Part 1: Safe reports in {filename}: Part 1 == {safe_reports_part1}, Part 2 == {safe_reports_part2}")
################################################################################


################################################################################
def is_report_safe_part1(report):

    is_report_safe = True
    previous_diff = 0

    for i in range(1, len(report)):
        diff = int(report[i]) - int(report[i-1])
        if diff == 0 or abs(diff) > 3:
            is_report_safe = False
            break
        if diff > 0 and previous_diff < 0:
            is_report_safe = False
            break
        if diff < 0 and previous_diff > 0:
            is_report_safe = False
            break
        previous_diff = diff

    logging.debug(f"Report: {report}, is_report_safe: {is_report_safe}")
    return is_report_safe
################################################################################


################################################################################
def is_report_safe_part2(report):

    is_report_safe = False
    for i in range(0, len(report)):
        copy = report.copy()
        copy.pop(i)
        if is_report_safe_part1(copy):
            is_report_safe = True

    logging.debug(f"Report: {report}, is_report_safe: {is_report_safe}")
    return is_report_safe
################################################################################


################################################################################
if __name__ == "__main__":
    main()
################################################################################
