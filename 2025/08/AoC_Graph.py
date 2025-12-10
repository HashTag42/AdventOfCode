from typing import Optional
import math


class Point():
    def __init__(self, x: int, y: int, z: int) -> None:
        self.x: int = x
        self.y: int = y
        self.z: int = z

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.z))

    def __repr__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"


class Line():
    def __init__(self, p: Point, q: Point) -> None:
        self.p: Point = p
        self.q: Point = q
        self.distance = math.sqrt((p.x - q.x)**2 + (p.y - q.y)**2 + (p.z - q.z)**2)

    def __lt__(self, other: 'Line') -> bool:
        return self.distance < other.distance

    def __repr__(self) -> str:
        return f"{self.p} <-> {self.q}, distance = {self.distance}"


class Circuit():
    def __init__(self, points: set[Point]) -> None:
        self.points: set[Point] = points

    def __contains__(self, point: Point) -> bool:
        return point in self.points

    def __len__(self) -> int:
        return len(self.points)

    def __lt__(self, other: 'Circuit') -> bool:
        return len(self) < len(other)

    def __repr__(self) -> str:
        return str(self.points)


class Graph():
    def __init__(self, points: set[Point], num_connections: int = 10) -> None:
        self.points_set: set[Point] = points
        self.points_list: list[Point] = list(self.points_set)

        self.point_to_circuit: dict[Point, Circuit] = {}

        # Build a list of lines between all point pairs
        self.lines: list[Line] = []
        total_points = len(self.points_set)
        for p in range(total_points):
            for q in range(p + 1, total_points):
                self.lines.append(Line(self.points_list[p], self.points_list[q]))
        self.lines.sort()

        # Build a list of circuits
        self.circuits: list[Circuit] = []
        connections_attempted = 0
        for line in self.lines:
            if connections_attempted >= num_connections:
                break
            connections_attempted += 1
            p_circuit = self.point_to_circuit.get(line.p)
            q_circuit = self.point_to_circuit.get(line.q)
            if p_circuit is None and q_circuit is None:
                new_circuit = Circuit({line.p, line.q})
                self.circuits.append(new_circuit)
                self.point_to_circuit[line.p] = new_circuit
                self.point_to_circuit[line.q] = new_circuit
            elif p_circuit is not None and q_circuit is None:
                p_circuit.points.add(line.q)
                self.point_to_circuit[line.q] = p_circuit
            elif p_circuit is None and q_circuit is not None:
                q_circuit.points.add(line.p)
                self.point_to_circuit[line.p] = q_circuit
            elif p_circuit is not q_circuit:
                # Merge: update all points in q_circuit to point to p_circuit
                if p_circuit is not None and q_circuit is not None:
                    for point in q_circuit.points:
                        self.point_to_circuit[point] = p_circuit
                    p_circuit.points.update(q_circuit.points)
                    self.circuits.remove(q_circuit)
            else:
                # Both points already in same circuit - skip, don't count as connection
                pass

            if len(self.circuits) == 1 and len(self.circuits[0]) == len(self.points_set):
                self.part2 = line.p.x * line.q.x
                return

        # Add singleton circuits for unconnected points
        for point in self.points_set:
            if point not in self.point_to_circuit:
                singleton = Circuit({point})
                self.circuits.append(singleton)
                self.point_to_circuit[point] = singleton

        self.circuits.sort()

    def find_circuit(self, point: Point) -> Optional[Circuit]:
        for circuit in self.circuits:
            if point in circuit:
                return circuit
        return None

    def __repr__(self) -> str:
        return (f"Graph({len(self.points_set)} points, "
                f"{len(self.lines)} lines, "
                f"{len(self.circuits)} components)")
