# Polyomino Lib
polyomino.py forked from [this](https://github.com/tesseralis/polyomino) repo

This lib uses [Knuth's Algorithm X](https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X) to arrange polyominoes on given figure. 
Also it have parser.py module to load polyominoes from .pol files and pretty-print them to console or write to svg files.

## Installation
Just clone this repo: 

`$ git clone `

`$ cd polyomino`

`$ python main.py`

## Examples
Find some arrangement of dominoes on 6x6 board:
```Python3
import parser
import solver

figure = parser.load('figure.pol')
# File contains
# XXXXXX
# XXXXXX
# XXXXXX
# XXXXXX
# XXXXXX
# XXXXXX

part = parser.load('part.pol')
# File contains
# XX

for idx, s in enumerate(solver.split_into_parts(figure, part)):
    parser.save_solution_to_svg(s, str(idx)+'th_sol.svg')
    parser.pretty_print_solution(s)
    break # Because there are 6727 different arrangements
```
Find all arrangements of equal tetraminoes on 4x4 board:
```Python3
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
```
You'll have 15 different solutions:

![Picture](http://i.imgur.com/0kkfwTU.png)