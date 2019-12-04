from helpers import read_input
from typing import List
from collections import defaultdict

def run_wire(wire, grid, wireno):
    closest_crossing = 9999999999999999
    x = 0
    y = 0
    steps = 0
    mttc = 9999999999999
    for step in wire.split(","):
        direction = step[0]
        distance = int(step[1:])
        while distance > 0:
            steps += 1
            if direction == 'U':
                y += 1
            elif direction == 'D':
                y -= 1
            elif direction == 'L':
                x -= 1
            elif direction == 'R':
                x += 1
            else:
                print("Invalid direction %s" % direction)
                exit(1)
            distance -= 1
            visitors = list(grid[y][x])
            if visitors[wireno] == 0:
                visitors[wireno] = steps
                grid[y][x] = tuple(visitors)
            md = abs(x) + abs(y)
            if md < closest_crossing and all(q > 0 for q in grid[y][x]):
                closest_crossing = md
            ttc = sum(grid[y][x])
            if ttc < mttc and all(q > 0 for q in grid[y][x]):
                print("crossing at %d,%d: %s" % (x, y, grid[y][x]))
                mttc = ttc
    return closest_crossing, mttc,

def part1(input: List[str]):
    wire1 = input[0]
    wire2 = input[1]
    grid = defaultdict(lambda: defaultdict(lambda: (0, 0)))
    closest1 = run_wire(wire1, grid, 0)
    closest2 = run_wire(wire2, grid, 1)
    print(min(closest1[0], closest2[0]), closest2[1])

def part2(input: List[str]):
    pass

if __name__ == '__main__':
    input = read_input()
    part1(input)
    part2(input)
