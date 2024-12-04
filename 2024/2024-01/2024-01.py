# Puzzle: https://adventofcode.com/2024/day/1

import os
import re

# Open the file

filename = "input.txt"
# filename = "inputTest.txt"

f = open(f"{os.path.dirname(__file__)}\{filename}", 'r')

# Create two lists
columna, columnb = [], []

# Read each line of the file

for line in f:
    print(line)

    # Parse each line into two numbers
    numbers = re.findall(r'\d+', line)

    # Store each number into their respective list
    columna.append(numbers[0])
    columnb.append(numbers[1])

f.close()

# Sort each list incrementally
columna.sort()
columnb.sort()

# Compare elements between the lists and add up their absolute difference
dif = 0
for i, a in enumerate(columna):
    d = int(a) - int(columnb[i])
    dif += abs(d)

# Print out the total difference
print(dif)