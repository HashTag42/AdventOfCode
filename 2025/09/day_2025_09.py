'''
Advent of Code 2025 - Day 09: Movie Theater
Puzzle: https://adventofcode.com/2025/day/9
'''


class Point():
    def __init__(self, x: int, y: int) -> None:
        self.x, self.y = x, y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class Rectangle():
    def __init__(self, a: Point, b: Point) -> None:
        self.a: Point = a
        self.b: Point = b
        self.area: int = (abs(self.a.x - self.b.x) + 1) * (abs(self.a.y - self.b.y) + 1)


def solve_2025_09(filename: str) -> tuple[int, int]:
    points = get_data(filename)
    return solve_part1(points), solve_part2(points)


def solve_part1(points: list[Point]) -> int:
    num_points = len(points)
    max_area = 0
    for a in range(num_points):
        for b in range(a+1, num_points):
            area = Rectangle(points[a], points[b]).area
            if area > max_area:
                max_area = area
    return max_area


def solve_part2(points: list[Point]) -> int:
    num_points = len(points)

    # Build edges of the polygon
    edges = []
    for i in range(num_points):
        p1 = points[i]
        p2 = points[(i + 1) % num_points]
        edges.append(((p1.x, p1.y), (p2.x, p2.y)))

    # Separate into horizontal and vertical edges
    h_edges = []  # (y, x_min, x_max)
    v_edges = []  # (x, y_min, y_max)

    for (x1, y1), (x2, y2) in edges:
        if y1 == y2:  # horizontal
            h_edges.append((y1, min(x1, x2), max(x1, x2)))
        else:  # vertical
            v_edges.append((x1, min(y1, y2), max(y1, y2)))

    def point_in_polygon(px, py):
        """Check if point is inside or on the polygon boundary using ray casting"""
        # First check if on boundary
        for (y, x_min, x_max) in h_edges:
            if py == y and x_min <= px <= x_max:
                return True
        for (x, y_min, y_max) in v_edges:
            if px == x and y_min <= py <= y_max:
                return True

        # Ray casting - count crossings to the right
        crossings = 0
        for (x, y_min, y_max) in v_edges:
            if x > px and y_min < py <= y_max:
                crossings += 1

        return crossings % 2 == 1

    def rectangle_in_polygon(x_min, y_min, x_max, y_max):
        """
        Check if entire rectangle is within the polygon.
        For a rectilinear polygon, we need to check:
        1. All four corners are inside or on boundary
        2. No edge of the polygon crosses through the interior of the rectangle
        """
        # Check corners
        corners = [(x_min, y_min), (x_min, y_max), (x_max, y_min), (x_max, y_max)]
        for cx, cy in corners:
            if not point_in_polygon(cx, cy):
                return False

        # Check if any horizontal polygon edge cuts through rectangle interior
        # An edge cuts through if:
        #   - Its y is strictly between y_min and y_max
        #   - It crosses into the rectangle's x-range
        for (y, ex_min, ex_max) in h_edges:
            if y_min < y < y_max:
                if ex_min < x_max and ex_max > x_min:
                    if ex_min < x_min < ex_max:  # Edge crosses left boundary
                        return False
                    if ex_min < x_max < ex_max:  # Edge crosses right boundary
                        return False
                    if ex_min >= x_min and ex_max <= x_max:  # Edge entirely inside x-range
                        return False

        # Check if any vertical polygon edge cuts through rectangle interior
        for (x, ey_min, ey_max) in v_edges:
            if x_min < x < x_max:
                if ey_min < y_max and ey_max > y_min:
                    if ey_min < y_min < ey_max:  # Edge crosses bottom boundary
                        return False
                    if ey_min < y_max < ey_max:  # Edge crosses top boundary
                        return False
                    if ey_min >= y_min and ey_max <= y_max:  # Edge entirely inside y-range
                        return False

        return True

    # Find largest rectangle with red corners contained in polygon
    max_area = 0

    for i in range(num_points):
        for j in range(i + 1, num_points):
            p1, p2 = points[i], points[j]
            x_min, x_max = min(p1.x, p2.x), max(p1.x, p2.x)
            y_min, y_max = min(p1.y, p2.y), max(p1.y, p2.y)

            area = (x_max - x_min + 1) * (y_max - y_min + 1)

            # Skip if area can't beat current max
            if area <= max_area:
                continue

            if rectangle_in_polygon(x_min, y_min, x_max, y_max):
                max_area = area

    return max_area


def get_data(filename) -> list[Point]:
    points: list[Point] = list()
    with open(filename, 'r') as file:
        for line in file.readlines():
            line = line.strip()
            if line:
                x, y = map(int, line.split(','))
                points.append(Point(x, y))
        return points


if __name__ == "__main__":
    import pytest
    import sys
    sys.exit(pytest.main(['-v', './2025/09/day_2025_09_test.py']))
