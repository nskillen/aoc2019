from helpers import read_input
from typing import List
from collections import defaultdict

def part1(input: List[str]):
    min = 183564
    max = 657474

    passwords = 0
    for x in range(min, max+1):
        chars = [char for char in ("%d" % x)]
        all_good = True
        has_double = False
        for y in range(0, len(chars)-1):
            if y == 0:
                c1,c2,c3 = chars[y:y+3]
                if c1 == c2 and c2 != c3:
                    has_double = True
                if c2 < c1:
                    all_good = False
            elif y == len(chars) - 2:
                c0,c1,c2 = chars[y-1:y+2]
                if c1 == c2 and c0 != c1:
                    has_double = True
                if c2 < c1:
                    all_good = False
            else:
                c0,c1,c2,c3 = chars[y-1:y+3]
                if c1 == c2 and c0 != c1 and c2 != c3:
                    has_double = True
                if c2 < c1:
                    all_good = False
        if all_good and has_double:
            passwords += 1
    print(passwords)



def part2(input: List[str]):
    pass

if __name__ == '__main__':
    input = read_input()
    part1(input)
    part2(input)
