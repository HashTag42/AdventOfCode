from get_password import get_password
import pytest

test_cases = [
    # input, expected_part1, expected_part2
    ('./2025/01/example.txt', 3, 6),
    ('./2025/01/input1.txt', 2, 4),
    ('./2025/01/input.txt', 1059, 6305),
]


@pytest.mark.parametrize("input, expected_part1, expected_part2", test_cases)
def test_get_password(input: str, expected_part1: str, expected_part2: str):
    click_count, total_clicks = get_password(input)
    assert click_count == expected_part1
    assert total_clicks == expected_part2
