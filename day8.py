from helpers import read_input
from typing import List
from collections import defaultdict
from itertools import permutations
from vm import vm as vmachine

def part1(lines: List[str]):
    image = list(map(int, lines[0]))
    chunk_size = 150
    layers = [image[i:i+chunk_size] for i in range(0, len(image), chunk_size)]
    fewest_sixes = 9999999
    selected_layer = None
    cur_layer = 0
    for layer in layers:
        cur_layer += 1
        chars = [x for x in list(layer) if x == 0]
        if len(chars) < fewest_sixes:
            fewest_sixes = len(chars)
            selected_layer = layer
    ones = len([x for x in selected_layer if x == 1])
    twos = len([x for x in selected_layer if x == 2])
    print(ones * twos)

def part2(lines: List[str]):
    image = list(map(int, lines[0]))
    chunk_size = 150
    chunks = len(image) // chunk_size
    layers = [image[i:i+chunk_size] for i in range(0, len(image), chunk_size)]
    width = 25
    height = 6
    message = [list(), list(), list(), list(), list(), list()]
    for y in range(0, height):
        for x in range(0, width):
            message[y].append(0)
            for l in range(0, chunks):
                offset = y * width + x
                if layers[l][offset] != 2:
                    message[y][x] = layers[l][offset]
                    break
    for y in range(0, 6):
        line = "".join(map(lambda x: '1' if x == 1 else ' ', message[y]))
        print(line)

if __name__ == '__main__':
    lines = list(map(lambda s: s.strip(), read_input()))
    part1(lines)
    part2(lines)
