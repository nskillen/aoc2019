from helpers import read_input
from typing import List

def how_much(fuel: int) -> int:
    if (fuel < 6):
        return 0
    f = (fuel // 3) - 2
    a = how_much(f)
    return f + a

def part1(input: List[str]):
    total = 0
    for fuel in input:
        total += (int(fuel) // 3) - 2
    print("The total fuel is %d" % total)

def part2(input: List[str]):
    total = 0
    for fuel in input:
        total += how_much(int(fuel))
    print("The real total is %d" % total)

if __name__ == '__main__':
    input = read_input()
    part1(input)
    part2(input)
