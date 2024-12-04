# Puzzle: https://adventofcode.com/2024/day/1

import os
import re

DEBUG = False

################################################################################
def main():
    filename = "input.txt"
    # filename = "inputTest.txt"
    printDebug(filename, locals())

    with open(f"{os.path.dirname(__file__)}\{filename}", 'r') as file:
        list1, list2 = [], []
        dict1, dict2 = {}, {}
        for line in file:
            # Parse each line into two numbers
            numbers = re.findall(r'\d+', line)  #The regular expression '\d+' matches one or more digits.
            list1.append(numbers[0])
            list2.append(numbers[1])
            increaseDictCount(dict1, numbers[0])
            increaseDictCount(dict2, numbers[1])

    list1.sort()
    list2.sort()
    printDebug(list1, locals())
    printDebug(list2, locals())

    printDebug(dict1, locals())
    printDebug(dict2, locals())

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
def printDebug(var, namespace):
    if DEBUG:
        var_name = [name for name, value in namespace.items() if value is var][0]
        print(f"[DEBUG] {var_name} = {var}")
################################################################################

if __name__ == "__main__":
    main()