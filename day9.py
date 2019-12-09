from helpers import read_input
from typing import List
from collections import defaultdict
from itertools import permutations
from vm import vm as vmachine

def part1(lines: List[str]):
    program = lines[0]
    vm = vmachine.VM()
    vm.load(program)
    vm.run()

def part2(lines: List[str]):
    pass

if __name__ == '__main__':
    lines = list(map(lambda s: s.strip(), read_input()))
    part1(lines)
    part2(lines)
