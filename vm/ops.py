from typing import Tuple

def add(vm, a1: Tuple[int, int], a2: Tuple[int, int], a3: Tuple[int, int]):
    v1 = vm.get(*a1)
    v2 = vm.get(*a2)
    if vm.debug:
        print("[{}] = {} + {}".format(a3, v1, v2))
    vm.put(a3, v1 + v2)

def mul(vm, a1: Tuple[int, int], a2: Tuple[int, int], a3: Tuple[int, int]):
    v1 = vm.get(*a1)
    v2 = vm.get(*a2)
    if vm.debug:
        print("[{}] = {} * {}".format(a3, v1, v2))
    vm.put(a3, v1 * v2)

def inp(vm, a1: Tuple[int, int]):
    if vm.input_function is not None:
        val = vm.input_function()
    elif vm.queue_inputs:
        if len(vm.queued_inputs) == 0:
            vm.waiting_for_input = True
            return
        val = vm.queued_inputs[0]
        vm.queued_inputs = vm.queued_inputs[1:]
    else:
        val = int(input("> "))

    if vm.debug:
        print("[{}] = {}".format(a1, val))
    vm.put(a1, val)

def out(vm, a1: Tuple[int, int]):
    v1 = vm.get(a1)
    if vm.output_function is not None:
        vm.output_function(v1)
    elif vm.queue_outputs:
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
    vm.put(a3, 1 if v1 < v2 else 0)

def eq(vm, a1: Tuple[int, int], a2: Tuple[int, int], a3: Tuple[int, int]):
    v1 = vm.get(*a1)
    v2 = vm.get(*a2)
    if vm.debug:
        print("{} == {} ?".format(v1,v2))
    vm.put(a3, 1 if v1 == v2 else 0)

def arb(vm, a1: Tuple[int, int]):
    v1 = vm.get(*a1)
    vm.relative_base += v1

def hlt(vm):
    vm.halt()
