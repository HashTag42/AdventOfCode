# Puzzle: https://adventofcode.com/2024/day/1

import re

# UNCOMMENT ONE OF THE FOLLOWING LINES
DEBUG = True
# DEBUG = False

# UNCOMMENT ONE OF THE FOLLOWING LINES
# filename = "input.txt"
filename = "inputTest.txt"

################################################################################
def main():
    printDebug(filename)

    list1, list2 = [], []
    dict1, dict2 = {}, {}

    for line in open(filename, 'r'):
        # Parse each line into two numbers
        # The regular expression '\d+' matches one or more digits.
        numbers = re.findall(r'\d+', line)
        list1.append(numbers[0])
        list2.append(numbers[1])
        increaseDictCount(dict1, numbers[0])
        increaseDictCount(dict2, numbers[1])

    list1.sort()
    list2.sort()
    printDebug(list1)
    printDebug(list2)
    printDebug(dict1)
    printDebug(dict2)

    dif = 0
    similarity_score = 0
    for i, a in enumerate(list1):
        dif += abs(int(a) - int(list2[i]))
        try:
            factor = int(dict2[list1[i]])
        except:
            factor = 0
        finally:
            similarity_score += int(list1[i]) * factor

    print(f"Part 1 result: {dif}")
    print(f"Part 2 result: {similarity_score}")

################################################################################

################################################################################
def increaseDictCount(dict, key):
    p = 0
    try:
        p = dict[key]
    except KeyError as e:
        dict[key] = 0
    finally:
        dict[key] = p+1
################################################################################

################################################################################
def printDebug(text):
    if DEBUG:
        print(f"[DEBUG] {text}")
################################################################################

if __name__ == "__main__":
    main()