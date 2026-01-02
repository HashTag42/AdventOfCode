'''
Advent of Code 2015 - Day 14: Reindeer Olympics
Puzzle: https://adventofcode.com/2015/day/14
'''
from Reindeer import Reindeer


def solve_part1(reindeers: list[Reindeer], time: int) -> int:
    for r in reindeers:
        r.reset()
        r.travel(time)
    return max(r.distance for r in reindeers)


def solve_part2(reindeers: list[Reindeer], time: int) -> int:
    for r in reindeers:
        r.reset()
    for _ in range(time):
        ranking: dict[Reindeer, int] = {}
        for r in reindeers:
            r.tick()
            ranking[r] = r.distance
        top_value = max(ranking.values())
        top_reindeers = {k: v for k, v in ranking.items() if v == top_value}
        for top_r in top_reindeers:
            top_r.points += 1
    return max(r.points for r in reindeers)


def get_data(filename: str) -> list[Reindeer]:
    with open(filename, 'r') as file:
        reindeers: list[Reindeer] = []
        for line in file:
            # Example: "Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds."
            parts = line.split()
            reindeers.append(Reindeer(parts[0], int(parts[3]), int(parts[6]), int(parts[13])))
    return reindeers


if __name__ == "__main__":
    import pytest
    import sys
    sys.exit(pytest.main(['-v', './2015/2015-14/AoC_2015_14_test.py']))
