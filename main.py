import parser
import solver

figure = parser.load('figure.pol')
part = parser.load('part.pol')

for idx, s in enumerate(solver.polyomino_split(figure, 4)):
    parser.save_solution_to_svg(s, str(idx)+'123.svg')
    parser.pretty_print_solution(s)
    print()
    break
