from helpers import read_input
from typing import List, Tuple
from collections import defaultdict
from itertools import permutations
from vm import vm as vmachine

directions = ['u','r','d','l']

robot = [0,0,0,'p']
panels = defaultdict(int)

def r_input():
    return panels[tuple(robot[0:2])]

def r_output(output):
    if robot[3] == 'p':
        panels[tuple(robot[0:2])] = output
        robot[3] = 't'
    elif robot[3] == 't':
        if output == 0: # ccw
            robot[2] = (robot[2] - 1) % 4
        elif output == 1: # cw
            robot[2] = (robot[2] + 1) % 4
        if directions[robot[2]] == 'u':
            robot[1] += 1
        elif directions[robot[2]] == 'd':
            robot[1] -= 1
        elif directions[robot[2]] == 'l':
            robot[0] -= 1
        elif directions[robot[2]] == 'r':
            robot[0] += 1
        robot[3] = 'p'

def part1(lines: List[str]):
    panels[(0,0)] = 1
    vm = vmachine.VM()
    vm.load(lines[0])
    vm.input_function = r_input
    vm.output_function = r_output
    vm.run()
    print(len(panels))
    xs = list(map(lambda p: p[0], list(panels.keys())))
    ys = list(map(lambda p: p[1], list(panels.keys())))
    for y in range(max(ys),min(ys)-1,-1):
        for x in range(min(xs),max(xs)+1):
            if panels[(x,y)] == 0:
                print(" ", end="")
            else:
                print("#", end="")
        print("")

def part2(lines: List[str]):
    pass

if __name__ == '__main__':
    lines = list(map(lambda s: s.strip(), read_input()))
    part1(lines)
    part2(lines)
