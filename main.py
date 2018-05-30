import parser
import solver

figure = parser.load('figure.pol')

for idx, s in enumerate(solver.auto_congruent_polyomino_split(figure, 5)):
    parser.save_solution_to_svg(s, str(idx)+'th_sol.svg')
    parser.pretty_print_solution(s)
    print()