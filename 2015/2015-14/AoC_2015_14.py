'''
Advent of Code 2015 - Day 14: Reindeer Olympics
Puzzle: https://adventofcode.com/2015/day/14
'''
from enum import Enum, auto


class State(Enum):
    FLYING = auto()
    RESTING = auto()


class Reindeer:
    def __init__(self, name: str, speed: int, fly_time: int, rest_time: int) -> None:
        self.name: str = name
        self.speed: int = speed
        self.fly_time: int = fly_time
        self.rest_time: int = rest_time

    def travel(self, time: int) -> int:
        self.state = State.FLYING
        distance = 0
        time_flying = 0
        time_resting = 0
        for _ in range(1, time + 1):
            if self.state == State.FLYING and time_flying >= self.fly_time:
                self.state = State.RESTING
                time_flying = time_resting = 0
            elif self.state == State.RESTING and time_resting >= self.rest_time:
                self.state = State.FLYING
                time_resting = time_flying = 0

            if self.state == State.FLYING:
                distance += self.speed
                time_flying += 1
            elif self.state == State.RESTING:
                time_resting += 1
        return distance

    def __repr__(self) -> str:
        return self.name


def solve_part1(reindeers: list[Reindeer], time: int) -> int:
    max = 0
    for r in reindeers:
        distance = r.travel(time)
        max = distance if distance > max else max
    return max


def solve_part2(reindeers: list[Reindeer]) -> int:
    result = 0
    return result


def get_data(filename: str) -> list[Reindeer]:
    with open(filename, 'r') as file:
        reindeers: list[Reindeer] = []
        for line in file.readlines():
            # Example: "Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds."
            parts = line.split()
            new_reindeer = Reindeer(parts[0], int(parts[3]), int(parts[6]), int(parts[13]))
            reindeers.append(new_reindeer)
    return reindeers


if __name__ == "__main__":
    import pytest
    import sys
    sys.exit(pytest.main(['-v', './2015/2015-14/AoC_2015_14_test.py']))
