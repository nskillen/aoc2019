from helpers import read_input
from vm import vm as vmachine
from collections import defaultdict
import operator

visited = set()
opposites = {1: 2, 2: 1, 3: 4, 4: 3}
offsets = {1: (0, -1), 2: (0, 1), 3: (-1, 0), 4: (1, 0)}

def tadd(a,b):
    return tuple(map(operator.add, a, b))

def final_coord(move):
    x = len([x for x in move if x == 4]) - len([x for x in move if x == 3]) # east moves - west moves
    y = len([y for y in move if y == 2]) - len([y for y in move if y == 1]) # south moves - north moves
    return (x,y)

def handle_result(move, result):
    if result == 0: # did not move, hit wall
        return None
    elif result == 1 or result == 2:
        x, y = final_coord(move)
        last_dir = move[-1]
        new_moves = []
        for m in range(1,5):
            if m == opposites[last_dir]:
                continue
            nextpos = tadd((x,y), offsets[m])
            if nextpos in visited:
                continue
            new_moves.append(move + [m])
            visited.add(nextpos)
        return new_moves
    else:
        print("ERROR: unsupported result %d" % result)
        exit(1)

def fill(layout):
    nextlayout = defaultdict(lambda: '#')
    for pos in layout:
        nextlayout[pos] = layout[pos]
        if layout[pos] == ' ':
            for offset in [(0,1),(1,0),(0,-1),(-1,0)]:
                adj_pos = tadd(pos, offset)
                if adj_pos in layout and layout[adj_pos] == 'O':
                    nextlayout[pos] = 'O'
                    break
    return nextlayout

def part1(lines):
    visited.add((0,0))
    pending_sequences = [[1],[2],[3],[4]]
    shortest_path = None
    longest_path = 0
    layout = defaultdict(lambda: '#')
    while len(pending_sequences) > 0:
        move = pending_sequences.pop(0)
        if len(move) > longest_path:
            longest_path = len(move)
            print("LONGEST PATH: {}".format(longest_path))
            print("PATHS TO CHECK: {}".format(len(pending_sequences)))
        vm = vmachine.VM()
        vm.load(lines[0])
        vm.queue_inputs = True
        vm.queued_inputs = move
        vm.queue_outputs = True
        vm.run()
        result = vm.queued_outputs.pop()
        x, y = final_coord(move)
        if result == 1:
            layout[(x,y)] = ' '
        if result == 2:
            layout[(x,y)] = 'O'
            if shortest_path is None:
                shortest_path = move
        new_moves = handle_result(move, result)
        if new_moves is None:
            continue
        else:
            for new_move in new_moves:
                pending_sequences.append(new_move)
    if shortest_path is not None:
        print("Shortest path is %d" % len(shortest_path))
    else:
        print("O2 Generator not found!")
        exit(1)
    minutes = 0
    area = len([x for x in layout.values() if x == ' ']) + 1
    print("Need to fill {} units of area".format(area))
    while len([x for x in layout.values() if x == ' ']) > 0:
        layout = fill(layout)
        minutes += 1
    print("Took %d minutes to fill the empty space" % minutes)

def part2(lines):
    pass

if __name__ == '__main__':
    lines = list(map(lambda s: s.strip(), read_input()))
    part1(lines)
    part2(lines)
