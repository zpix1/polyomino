from polyomino import Polyomino

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

    # grid = [[-1 for j in range(max(data))] for i in range(len(data))]

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 'X':
                pol.append((i,j))

    return Polyomino(pol).normalize()


