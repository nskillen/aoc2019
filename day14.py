from helpers import read_input
from collections import defaultdict
from math import ceil

def combine_like_terms(eqn):
    #print("***COMBINE***")
    terms = defaultdict(int)
    for term in eqn:
        mult, name = term
        terms[name] += mult
    return list(map(lambda t: (terms[t], t), terms))

# eqn looks like [(1,'ABC'),(2,'DEF'),(3,'GHI')]
# eqns looks like {'DEF': (2, [(7,'JKL'),(11,'MNO')]),'GHI': (4, [(12,'ORE')])}
def expand(eqn, eqns):
    #print("***EXPAND***")
    expanded = list()
    for (mult, name) in eqn:
        if mult < 0 or name not in eqns:
            expanded.append((mult, name))
        else:
            produces,terms = eqns[name]
            nmult = ceil(mult / produces)
            produced = nmult * produces
            for (tmult,tname) in terms:
                expanded.append((tmult * nmult, tname))
            if produced > mult: # "overproduced", keep the leftovers
                leftovers = mult - produced
                #print("{} {} produced, {} consumed, {} leftover".format(produced, name, mult, leftovers))
                expanded.append((leftovers, name))
    return expanded

eqns = dict()

def ore_cost_for(fuel_amount):
    eqn = [(fuel_amount, 'FUEL')]
    eqn_pos_only = eqn
    while len(eqn_pos_only) > 1 or eqn_pos_only[0][1] != 'ORE':
        eqn = expand(eqn, eqns)
        eqn = combine_like_terms(eqn)
        eqn_pos_only = [(m,n) for (m,n) in eqn if m > 0] # ignore negative terms caused by overproduction
    return eqn_pos_only[0][0]

def part1(lines):
    for eqn in lines:
        inputs, output = map(lambda s: s.strip(), eqn.split("=>"))
        mult, name = map(lambda s: s.strip(), output.split(" "))
        mult = int(mult)
        eqns[name] = (mult, list())
        for inp in map(lambda s: s.strip(), inputs.split(",")):
            mult, term = inp.split(" ")
            eqns[name][1].append((int(mult), term))
    print(ore_cost_for(1))

def part2(lines):
    print("{:,}".format(ore_cost_for(1639374)))

if __name__ == '__main__':
    lines = list(map(lambda s: s.strip(), read_input()))
    part1(lines)
    part2(lines)
