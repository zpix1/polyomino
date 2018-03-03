import polyomino as pm
from itertools import groupby

n = 4

polys = list(pm.generate(n))

def get(n):
    s = list(map(list, pm.generate(n))) 
    inverted = []
    for i in s:
        pol = []
        for cell in i:
            pol.append((-cell[0], -cell[1]))
        inverted.append(pol)
    return s + inverted

