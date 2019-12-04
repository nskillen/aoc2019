from helpers import read_input
from typing import List

def part1(input: List[str]):
    memory = list(map(int, ",".join(input).split(",")))
    pc = 0
    while memory[pc] != 99:
        if memory[pc] == 1:
            memory[memory[pc + 3]] = memory[memory[pc + 1]] + memory[memory[pc + 2]]
        elif memory[pc] == 2:
            memory[memory[pc + 3]] = memory[memory[pc + 1]] * memory[memory[pc + 2]]
        else:
            print("Unknown instruction: %d" % memory[pc])
        pc += 4
    print(memory[0])


def part2(input: List[str]):
    pass

if __name__ == '__main__':
    input = read_input()
    part1(input)
    part2(input)
