from helpers import read_input
from typing import List
from collections import defaultdict
from itertools import permutations
from vm import vm as vmachine

def part1(lines: List[str]):
    base_list = [0,1,2,3,4]
    phase_inputs = permutations(base_list)

    best_thrust = 0
    for phase_settings in phase_inputs:
        vms = [vmachine.VM(), vmachine.VM(), vmachine.VM(), vmachine.VM(), vmachine.VM()]
        for vm in vms:
            vm.load(lines[0])
            vm.queue_inputs = True
            vm.queue_outputs = True
        for i in range(0,5):
            vms[i].queue_input(phase_settings[i])
        vms[0].queue_input(0)
        for i in range(0,5):
            vms[i].run()
            out = vms[i].get_output()
            if out is None:
                print("ERROR: VM{} did not produce output".format(i))
                exit(1)
            elif i < 4:
                vms[i+1].queue_input(out)
            else:
                if out > best_thrust:
                    best_thrust = out
    print(best_thrust)

def part2(lines: List[str]):
    base_list = [5,6,7,8,9]
    phase_inputs = permutations(base_list)

    best_thrust = 0
    for phase_settings in phase_inputs:
        vms = [vmachine.VM(), vmachine.VM(), vmachine.VM(), vmachine.VM(), vmachine.VM()]
        for vm in vms:
            vm.load(lines[0])
            vm.queue_inputs = True
            vm.queue_outputs = True
        for i in range(0,5):
            vms[i].queue_input(phase_settings[i])
        next_starting_input = 0
        while not all(map(lambda v: v.halted, vms)):
            vms[0].queue_input(next_starting_input)
            for i in range(0,5):
                vms[i].run()
                out = vms[i].get_output()
                if out is None:
                    print("ERROR: VM{} did not produce output".format(i))
                    exit(1)
                elif i < 4:
                    vms[i+1].queue_input(out)
                else:
                    next_starting_input = out
        if next_starting_input > best_thrust:
            best_thrust = next_starting_input
    print(best_thrust)

if __name__ == '__main__':
    lines = list(map(lambda s: s.strip(), read_input()))
    part1(lines)
    part2(lines)
