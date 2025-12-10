'''
Advent of Code 2025 - Day 09: Movie Theater
Puzzle: https://adventofcode.com/2025/day/9
'''


class Point():
    def __init__(self, xy: str) -> None:
        self.x, self.y = map(int, xy.split(','))


class Rectangle():
    def __init__(self, a: Point, b: Point) -> None:
        self.a: Point = a
        self.b: Point = b
        self.area: int = (abs(self.a.x - self.b.x) + 1)  * (abs(self.a.y - self.b.y) + 1)


def solve_2025_09(file: str) -> tuple[int, int]:
    data = get_data(file)
    return solve_part1(data), solve_part2(data)


def solve_part1(data) -> int:
    points: list[Point] = list()
    for line in data:
        points.append(Point(line))
    num_points = len(points)
    max_area = 0
    for a in range(num_points):
        for b in range(a+1, num_points):
            area = Rectangle(points[a], points[b]).area
            if area > max_area:
                max_area = area
    return max_area


def solve_part2(data) -> int:
    result = 0
    return result


def get_data(file) -> list[str]:
    data: list[str] = list()
    with open(file, 'r') as f:
        for line in f.readlines():
            data.append(line.strip())
    return data


if __name__ == "__main__":
    import pytest
    import sys
    sys.exit(pytest.main(['-v', './2025/09/day_2025_09_test.py']))
