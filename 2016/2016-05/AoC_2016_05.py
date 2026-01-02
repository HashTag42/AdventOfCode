'''
Advent of Code 2016 - Day 05: How About a Nice Game of Chess?
Puzzle: https://adventofcode.com/2016/day/05
'''
import hashlib
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s: %(message)s",
    )


def solve(door_id: str) -> tuple[str, str]:
    return solve_part1(door_id), solve_part2(door_id)


def solve_part1(door_id) -> str:
    password: str = ""
    counter: int = 0
    while True:
        string: str = door_id + str(counter)
        md5_hash: str = hashlib.md5(string.encode()).hexdigest()
        if md5_hash.startswith('00000'):
            password += md5_hash[5]
            logging.debug(f"{string=}, {md5_hash=}, {password=}")
        if len(password) == 8:
            break
        counter += 1
    return password


def solve_part2(input) -> str:
    result = ""
    return result


if __name__ == "__main__":
    result1, result2 = solve('abc')
    logging.info(f"example.txt: Results: Part 1 = {result1}, Part 2 = {result2}")

    result1, result2 = solve('ojvtpuvg')
    logging.info(f"input.txt: Results: Part 1 = {result1}, Part 2 = {result2}")
