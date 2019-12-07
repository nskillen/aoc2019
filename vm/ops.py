from typing import Tuple

def add(vm, a1: Tuple[int, int], a2: Tuple[int, int], a3: Tuple[int, int]):
    v1 = vm.get(*a1)
    v2 = vm.get(*a2)
    if vm.debug:
        print("[{}] = {} + {}".format(a3, v1, v2))
    vm.memory.write(a3, v1 + v2)

def mul(vm, a1: Tuple[int, int], a2: Tuple[int, int], a3: Tuple[int, int]):
    v1 = vm.get(*a1)
    v2 = vm.get(*a2)
    if vm.debug:
        print("[{}] = {} * {}".format(a3, v1, v2))
    vm.memory.write(a3, v1 * v2)

def inp(vm, a1: Tuple[int, int]):
    if not vm.queue_inputs:
        val = int(input("> "))
    else:
        if len(vm.queued_inputs) == 0:
            vm.waiting_for_input = True
            return
        val = vm.queued_inputs[0]
        vm.queued_inputs = vm.queued_inputs[1:]

    if vm.debug:
        print("[{}] = {}".format(a1, val))
    vm.memory.write(a1, val)

def out(vm, a1: Tuple[int, int]):
    v1 = vm.get(a1)
    if vm.queue_outputs:
        vm.queued_outputs.append(v1)
    else:
        print(v1)

def jnz(vm, a1: Tuple[int, int], a2: Tuple[int, int]):
    v1 = vm.get(a1)
    if v1 != 0:
        vm.jump(a2)

def jz(vm, a1: Tuple[int, int], a2: Tuple[int, int]):
    v1 = vm.get(a1)
    if v1 == 0:
        vm.jump(a2)

def lt(vm, a1: Tuple[int, int], a2: Tuple[int, int], a3: Tuple[int, int]):
    v1 = vm.get(*a1)
    v2 = vm.get(*a2)
    if vm.debug:
        print("{} < {} ?".format(v1,v2))
    vm.memory.write(a3, 1 if v1 < v2 else 0)

def eq(vm, a1: Tuple[int, int], a2: Tuple[int, int], a3: Tuple[int, int]):
    v1 = vm.get(*a1)
    v2 = vm.get(*a2)
    if vm.debug:
        print("{} == {} ?".format(v1,v2))
    vm.memory.write(a3, 1 if v1 == v2 else 0)

def hlt(vm):
    vm.halt()
