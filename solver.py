import dancing_links as dl
import polyomino as pm
from collections import defaultdict
import itertools

def _generate_x_y(figure, pols):
    creatures = []
    xfigure = defaultdict(set)

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

    return (xfigure, Y)

def _solution_generator(figure,pols):
    X,Y = _generate_x_y(figure,pols)
    for solution in dl.solve(X,Y):
        # print(solution)
        ans = []
        for pol_id in solution:
            ans.append(pm.Polyomino(Y[pol_id]))

        # pretty_print_solution(ans)
        if ans == []:
            raise StopIteration
        yield ans

def polyomino_split(figure, n):
    """
    Split given `figure` to polyominos of size `n`.
    """

    pols = pm.generate(n)

    return _solution_generator(figure, pols)

def congruent_polyomino_split(figure, n):
    """
    Split given `figure` to congruent polyominos of size `n`.
    """
    ans = []
    for pol in pm.free(pm.generate(n)):
        ans.append( _solution_generator(figure, set(pol.transforms())))
    # print(zip(*ans)
    return itertools.chain(*ans)


    