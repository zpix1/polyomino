import parser
import solver

figure = parser.load('figure.pol')

def get_nth_result(generator, n):
    i = 0
    for ans in generator:
        if i == n:
            return ans
        i += 1

for s in solver.polyomino_split(figure, 4):
    parser.save_solution_to_svg(s, '123.svg')
    parser.pretty_print_solution(s)
    print()
    break
