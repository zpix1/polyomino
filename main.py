import parser
import solver

figure = parser.load('figure.pol')
# File contains
# XXXX
# XXXX
# XXXX
# XXXX

# auto_congruent_polyomino_split will do all for you
for idx, s in enumerate(solver.auto_congruent_polyomino_split(figure, 4)):
    parser.save_solution_to_svg(s, str(idx)+'th_sol.svg')
    parser.pretty_print_solution(s)
    print()