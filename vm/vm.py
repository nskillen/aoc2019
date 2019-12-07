from .memory import Memory
from . import ops
from typing import List, Tuple, Union
import traceback

class VM:
    def __init__(self):
        self.reset()

    def setDebug(self, enable):
        self.debug = enable
    
    def setPrintAsm(self, enable):
        self.print_asm = enable
    
    def reset(self):
        self.memory = Memory()
        self.halted = False
        self.ip = 0
        self.sp = 0
        self.debug = False
        self.print_asm = False
        self.queue_inputs = False
        self.queued_inputs = list()
        self.waiting_for_input = False
        self.queue_outputs = False
        self.queued_outputs = list()
    
    def load(self, instructions: str):
        instrlist = list(map(int, instructions.split(",")))
        if len(instrlist) > self.memory.size():
            self.memory.resize(len(instrlist))

        address = 0
        for instr in instrlist:
            self.memory.write(address, instr)
            address += 1

    def run(self):
        while not self.halted and not self.waiting_for_input:
            self.step()
        if self.waiting_for_input:
            self.waiting_for_input = False
    
    def step(self):
        instruction = self.memory.read(self.ip)
        pmodes, opcode, ilen = self.parse(instruction)
        values = self.memory[self.ip+1:self.ip+len(pmodes)+1]
        pvtuples = list(zip(pmodes, values))

        orig_ip = self.ip
        self.ip += ilen

        opcodes = {
            1: { 'fn': ops.add, 'name': 'ADD' },
            2: { 'fn': ops.mul, 'name': 'MUL' },
            3: { 'fn': ops.inp, 'name': 'IN' },
            4: { 'fn': ops.out, 'name': 'OUT' },
            5: { 'fn': ops.jnz, 'name': 'JNZ' },
            6: { 'fn': ops.jz, 'name': 'JZ' },
            7: { 'fn': ops.lt, 'name': 'LT' },
            8: { 'fn': ops.eq, 'name': 'EQ' },
            99: { 'fn': ops.hlt, 'name': 'HLT' },
        }

        if opcode in opcodes:
            op = opcodes[opcode]
            if self.print_asm:
                print("@{}: {} {}".format(orig_ip, op['name'], pvtuples))
            try:
                op['fn'](self, *pvtuples)
            except:
                traceback.print_exc()

        if self.waiting_for_input:
            self.ip -= ilen

    
    def jump(self, location: Union[int, Tuple[int, int]]):
        if isinstance(location, tuple):
            loc = self.get(location)
        else:
            loc = location

        if self.debug:
            print("Jumping to %d" % loc)

        self.ip = loc

    def halt(self):
        self.halted = True

    def parse(self, instruction: int) -> (List[int], int, int):
        argcs = { 1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 99: 0 }

        opcode = instruction % 100
        pmodes = list()
        argc = argcs[opcode]

        if argc > 0:
            pmodes = [int(char) for char in ("%d" % (instruction // 100))[::-1]]
            while len(pmodes) < argc:
                pmodes.append(0)
        
        return pmodes, opcode, argc + 1

    def get(self, *args):
        if len(args) == 1 and isinstance(args[0], tuple):
            pmode, value = args[0]
        elif len(args) == 2:
            pmode, value = args
            
        if pmode == 0:
            return self.memory.read(value)
        elif pmode == 1:
            return value
        else:
            print("Unknown pmode: %d" % pmode)
            exit(1)

    def queue_input(self, input):
        if isinstance(input, list):
            self.queued_inputs.extend(input)
        else:
            self.queued_inputs.append(input)

    def get_output(self):
        if len(self.queued_outputs) > 0:
            output = self.queued_outputs[0]
            self.queued_outputs = self.queued_outputs[1:]
            return output
        else:
            return None