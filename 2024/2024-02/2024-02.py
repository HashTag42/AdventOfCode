# Puzzle: https://adventofcode.com/2024/day/2

import re
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Modules'))
from printDebug import printDebug # type: ignore

################################################################################
def main():
    filename = "input.txt"
    # filename = "testInput.txt"
    printDebug(filename, locals())

    total_safe_reports = 0

    with open(f"{os.path.dirname(__file__)}\\{filename}", 'r') as file:
        total_safe_reports = 0
        for line in file:
            printDebug(line, locals())
            numbers = re.findall(r'\d+', line)  #The regular expression '\d+' matches one or more digits.
            if is_report_safe(numbers):
                total_safe_reports += 1

    print(f"Total safe reports in {filename} = {total_safe_reports}")
################################################################################

################################################################################
def is_report_safe(report):
    is_report_safe = True
    l = len(report)
    previous_diff = 0

    for i in range(1, l):
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

    printDebug(is_report_safe, locals())
    return is_report_safe
################################################################################

################################################################################
if __name__ == "__main__":
    main()
################################################################################
