from day_2025_08 import solve_part1, solve_part2, get_data
import pytest

test_cases = [
    # filename, num_connections, expected
    ('./2025/08/example.txt', [10, 100000], [40, 25272]),
    ('./2025/08/input.txt', [1000, 100000], [57564, 133296744]),
]


@pytest.mark.parametrize("filename, num_connections, expected", test_cases)
def test_solve_2025_08_Part1(filename, num_connections, expected):
    actual = solve_part1(get_data(filename), num_connections[0])
    assert actual == expected[0]


@pytest.mark.parametrize("filename, num_connections, expected", test_cases)
def test_solve_2025_08_Part2(filename, num_connections, expected):
    actual = solve_part2(get_data(filename), num_connections[1])
    assert actual == expected[1]
