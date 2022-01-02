# Day 12: Passage Pathing
# https://adventofcode.com/2021/day/12
# Code from https://old.reddit.com/r/adventofcode/comments/rehj2r/2021_day_12_solutions/ho7x83o/

# inFile = 'inputTest1.txt'
# inFile = 'inputTest2.txt'
# inFile = 'inputTest3.txt'
inFile = 'input.txt'

from collections import defaultdict
neighbours = defaultdict(list)

for line in open(inFile):
    a, b = line.strip().split('-')
    neighbours[a] += [b]
    neighbours[b] += [a]

def count(part, seen=[], cave='start'):
    if cave == 'end': return 1
    if cave in seen:
        if cave == 'start': return 0
        if cave.islower():
            if part == 1: return 0
            else: part = 1

    s = 0
    for n in neighbours[cave]:
        s += count(part, seen+[cave], n)
    return s

print("using: " + inFile)
print(count(part=1))
print(count(part=2))