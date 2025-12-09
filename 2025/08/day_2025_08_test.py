from day_2025_08 import solve_part1, solve_part2, get_data
import pytest

test_cases = [
    # filename, num_connections, expected
    ('./2025/08/example.txt', 10, [40, 0]),
    ('./2025/08/input.txt', 1000, [57564, 0]),
]


@pytest.mark.parametrize("filename, num_connections, expected", test_cases)
def test_solve_2025_08_Part1(filename, num_connections, expected):
    actual = solve_part1(get_data(filename, num_connections))
    assert actual == expected[0]


@pytest.mark.parametrize("filename, num_connections, expected", test_cases)
def test_solve_2025_08_Part2(filename, num_connections, expected):
    actual = solve_part2(get_data(filename, num_connections))
    assert actual == expected[0]
