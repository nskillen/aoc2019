from helpers import read_input
from typing import List
from vm import vm as vmachine

def part1(inp: List[str]):
    vm = vmachine.VM()
    vm.load(inp[0])
    #vm.setDebug(True)
    #vm.setPrintAsm(True)
    vm.run()

def part2(inp: List[str]):
    pass

if __name__ == '__main__':
    inp = read_input()
    part1(inp)
    part2(inp)
