import svgwrite

from polyomino import Polyomino

_colors = [
    (60, 180, 75),
    (255, 225, 25),
    (0, 130, 200),
    (70, 240, 240),
    (245, 130, 48),
    (145, 30, 180),
    (240, 50, 230),
    (210, 245, 60),
    (250, 190, 190),
    (230, 190, 255),
    (170, 110, 40),
    (255, 250, 200),
    (128, 0, 0),
    (170, 255, 195),
    (128, 128, 0),
    (255, 215, 180),
    (0, 0, 128),
    (128, 128, 128)
]

def _console_color(text, index):
    return '\033[48;5;{}m{}\033[0m'.format(index+1, text)

def _svg_color(index):
    if index == -1:
        return 'white'
    return svgwrite.rgb(*_colors[index % len(_colors)])

def _solution_to_data(solution):
    d = {}

    width = max(solution, key = lambda x: x.width).width
    height = max(solution, key = lambda x: x.height).height

    data = [[-1 for _1 in range(width)] for _0 in range(height)]
    for s in solution:
        if s in d:
            mapped = d[s]
        else:
            d[s] = len(d)
            mapped = d[s]

        for cell in s:
            data[cell[0]][cell[1]] = mapped

    return data

def load(filepath):
    """
    Load polyomino from .pol file
    
    Example T-polyomino:
    XXX
     X
     X

    """
    f = open(filepath)
    data = f.read().split("\n")

    pol = []

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 'X':
                pol.append((i,j))

    return Polyomino(pol).normalize()

def pretty_print_solution(solution):
    data = _solution_to_data(solution)

    for i in data:
        for j in i:
            print(_console_color('  ',j), end="")
        print()


def save_solution_to_svg(solution, filepath):
    data = _solution_to_data(solution)

    dwg = svgwrite.Drawing(filepath, profile='tiny')

    for i in range(len(data)):
        for j in range(len(data[0])):
            if type(data[i][j]) == int:
                dwg.add(dwg.rect((j*100, i*100), (100, 100), fill=_svg_color(data[i][j])))
    
    dwg.save()




