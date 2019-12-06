from helpers import read_input
from typing import List
from collections import defaultdict

names = set()
nodes = defaultdict(lambda: None)

def part1(input: List[str]):
    for orbited, orbitee in map(lambda x: x.split(")"), input):
        if orbitee in names:
            print("Error: attempted to add %s twice!" % orbitee)
            exit(1)
        nodes[orbitee] = orbited
        names.add(orbitee)

    total = 0
    for name in names:
        if name in ['YOU', 'SAN']:
            continue
        length = 0
        n = nodes[name]
        while n is not None:
            length += 1
            n = nodes[n]
        total += length
    print(total)

def part2(input: List[str]):
    y = nodes['YOU']
    s = nodes['SAN']

    seen = set()
    dists = dict()

    yd = 0
    sd = 0

    while y not in seen or s not in seen:
        if y not in seen:
            #print("y got to %s after %d transfers" % (y, yd))
            seen.add(y)
            dists[y] = yd
            y = nodes[y]
            yd += 1
        if s not in seen:
            #print("s got to %s after %d transfers" % (s, sd))
            seen.add(s)
            dists[s] = sd
            s = nodes[s]
            sd += 1

    #print("y=%s,yd=%d\ns=%s,sd=%d" % (y, yd, s, sd))
    #print(dists)

    if y is not None and s is None:
       print(dists[y] + yd)
    elif s is not None and y is None:
        print(dists[s] + sd)
    else:
        print("Either both y and s are none, or neither. Something is wrong")

if __name__ == '__main__':
    input = map(lambda s: s.strip(), read_input())
    part1(input)
    part2(input)
