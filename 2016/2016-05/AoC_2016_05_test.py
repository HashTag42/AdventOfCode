from AoC_2016_05 import solve_part1, solve_part2
import pytest

test_cases = [
    # door_id, expected
    ('abc', ['18f47a30', 0]),
    ('ojvtpuvg', ['4543c154', 0]),
]


@pytest.mark.parametrize('door_id, expected', test_cases)
def test_solve_part1(door_id, expected):
    assert solve_part1(door_id) == expected[0]


@pytest.mark.parametrize('door_id, expected', test_cases)
def test_solve_part2(door_id, expected):
    assert solve_part2(door_id) == expected[1]
