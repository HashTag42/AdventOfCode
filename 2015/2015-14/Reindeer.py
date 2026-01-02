from enum import auto, Enum


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
