from day_2025_06 import solve_part1, solve_part2, get_data
import pytest


test_cases = [
    # file, expected
    ('./2025/06/example.txt', [4277556, 3263827]),
    ('./2025/06/input.txt', [5667835681547, 9434900032651]),
]


@pytest.fixture
def test_data(request):
    """Fixture that loads data based on parametrized file"""
    file = request.param[0]
    expected = request.param[1]
    data = get_data(file)
    return data, expected


@pytest.mark.parametrize("test_data", test_cases, indirect=True)
def test_solve_part1(test_data):
    data, expected = test_data
    assert solve_part1(data[0]) == expected[0]


@pytest.mark.parametrize("test_data", test_cases, indirect=True)
def test_solve_part2(test_data):
    data, expected = test_data
    assert solve_part2(data[1]) == expected[1]
