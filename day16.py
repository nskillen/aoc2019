from helpers import read_input
from vm import vm as vmachine
from collections import defaultdict
import math

def fft(inp):
    pattern = [0, 1, 0, -1]
    output = [0] * len(inp)

    for out_index in range(len(inp)):
        output[out_index] = abs(sum([inp[i] * pattern[((i+1)//(out_index+1)) % 4] for i in range(len(inp))])) % 10
    #for out_index in range(len(inp)):
    #    if out_index == 0:
    #        # first element in output list, so no repetation in pattern
    #        sum_elems = [inp[i] * pattern[(i+1) % len(pattern)] for i in range(len(inp))]
    #        output[0] = abs(sum(sum_elems)) % 10
    #    else:
    #        offset = 0
    #        block_size = out_index + 1
    #        total = 0
    #        blocks = math.ceil((len(inp) + 1) / block_size)
    #        for block in range(blocks):
    #            print("{}/{}".format(block+1,blocks))
    #            slice_size = block_size
    #            if block % 4 == 0 or block % 4 == 2:
    #                offset += slice_size
    #                continue
    #            if block == 0:
    #                slice_size -= 1
    #            total += sum(inp[offset:slice_size]) * pattern[block % 4]
    #            offset += slice_size
    #        output[out_index] = abs(total) % 10
    return output

def part1(lines):
    pass
    #digits = list(map(int, [c for c in lines[0]]))
    #for i in range(100):
    #    print(i+1)
    #    digits = fft(digits)
    #print("".join(map(str, digits[:8])))

def part2(lines):
    """
    solution is taken from
    https://github.com/mebeim/aoc/blob/master/2019/README.md#day-16---flawed-frequency-transmission
    I had no clue how to do this one, as I never spotted the thing with the fact that you can just sum up
    the back half of the new digits
    """
    digits = list(map(int, [c for c in lines[0]])) * 10000
    skip = int(lines[0][:7])
    if skip < len(digits) / 2:
        print("ERROR: can't use fast method, not skipping enough digits")
        exit(1)
    digits = digits[skip:]
    for _ in range(100):
        for i in range(len(digits) - 2, -1, -1):
            digits[i] += digits[i+1]
            digits[i] %= 10
    print(''.join(map(str, digits[:8])))

if __name__ == '__main__':
    lines = list(map(lambda s: s.strip(), read_input()))
    part1(lines)
    part2(lines)
