import generator as gn
from collections import defaultdict
from dancing_links import *
import pprint as pp
from blessings import Terminal
from random import choice
import parser
from polyomino import free
t = Terminal()

#pols = list(map(list, parser.load('part.pol').transforms()))#
pols = gn.get(n)
print()
size = 10

figure = []
xfigure = defaultdict(set)

creatures = []

figure = list(parser.load('figure.pol'))
# print([figure])

for index, pol in enumerate(pols):
    for cell in figure:
        for pol_cell in pol:
            if (cell[0] + pol_cell[0], cell[1] + pol_cell[1]) not in figure:
                break
        else:
            s = []
            for pol_cell in pol:
                s.append((cell[0] + pol_cell[0], cell[1] + pol_cell[1]))
                xfigure[(cell[0] + pol_cell[0], cell[1] + pol_cell[1])].add(len(creatures))
            creatures.append(s)


Y = {}
for index, pol in enumerate(creatures):
    Y[index] = pol

X = xfigure

# pp.pprint(Y)

def color(text, index):
    return '\033[48;5;{}m{}\033[0m'.format(index+1, text)

data = [['  ' for _1 in range(size)] for _0 in range(size)]


d = {}
for solution in solve(X,Y):
    for s in solution:
        if s in d:
            mapped = d[s]
        else:
            d[s] = len(d)
            mapped = d[s]

        for cell in Y[s]:
            # print(cell)
            data[cell[0]][cell[1]] = color('  ', mapped)

    for i in data:
        for j in i:
            print(j, end="")
        print()

    print()
    # break