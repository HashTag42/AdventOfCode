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
        self.time_in_state: int = 0
        self.distance: int = 0
        self.points: int = 0
        self.state: State = State.FLYING

    def tick(self) -> None:
        match self.state:
            case State.FLYING:
                self.distance += self.speed
                self.time_in_state += 1
                if self.time_in_state >= self.fly_time:
                    self.state, self.time_in_state = State.RESTING, 0
            case State.RESTING:
                self.time_in_state += 1
                if self.time_in_state >= self.rest_time:
                    self.state, self.time_in_state = State.FLYING, 0

    def travel(self, time: int) -> None:
        self.state = State.FLYING
        for _ in range(time):
            self.tick()

    def reset(self) -> None:
        self.distance, self.time_in_state = 0, 0

    def __repr__(self) -> str:
        return self.name


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
