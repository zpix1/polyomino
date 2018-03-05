import sys

import functools as _ft

def generate(n):
    
    
    if n == 0:
        return set()
    
    minos = {Polyomino([(0,0)])}
    
    for i in range(n-1):
        minos = childset(minos)
    return minos

def gen_all_to(n):
    global n_track
    if n == 0:
        return set()
    
    minos = {Polyomino([(0,0)])}
    
    for i in range(n-1):
        import gc
        # print(len(gc.get_objects()))
        # print('minos=',sys.getsizeof(list(minos)[-1])*len(minos)/10**9)
        # tracker.print_diff()
        minos.update(childset(minos))
    return minos

def childset(minos):
    
    children = set()
    for mino in minos:
        children.update(mino.children())
    return children

def one_sided(minos, sort=True):
    
    vis = set() 
    result = set()
    for mino in minos:
        
        
        if mino not in vis:
            mino_rots = mino.rotations()
            vis.update(mino_rots)
            
            result.add(max(mino_rots, key=mino_key) if sort else mino)
    return result

def free(minos, sort=True):
    
    vis = set() 
    result = set()
    for mino in minos:
        
        
        if mino not in vis:
            mino_trans = mino.transforms()
            vis.update(mino_trans)
            
            result.add(max(mino_trans, key=mino_key) if sort else mino)
    return result

#
#
def mino_key(m):
    h, w = m.shape
    return (len(m), h/w, sum(2**(i+j*w) for i, j in m))

def _neighbors(point):
    
    i, j = point
    return {(i-1, j), (i+1, j), (i, j-1), (i, j+1)}

##@_ft.total_ordering
class Polyomino(frozenset):
    
    def grid(self):
        
        
        h, w = self.shape
        grid = [[False]*w for row in range(h)]
        
        for i, j in self:
            grid[i][j] = True
        return grid


    def __hash__(self):
        
        return super().__hash__()
    
    def __str__(self, cell="[]", empty="  "):
        
        grid = self.grid()
        result = []
        for row in grid:
            result.append("".join(cell if c else empty for c in row))
        return '\n'.join(result)

    def __eq__(self, other):
        
        return super().__eq__(other)

    @property
    def size(self):
        return len(self)
    @property
    def shape(self):
        
        rows, cols = zip(*self)
        return max(rows)+1, max(cols)+1
    @property
    def width(self):
        return self.shape[1]
    @property
    def height(self):
        return self.shape[0]
    

    @property
    def perimeter(self):
        near_cells = [(1,0),(0,-1),(-1,0),(0,1)]
        grid = self.grid()
        ans = 0
        for i in range(self.height):
            for j in range(self.width):
                if grid[i][j]:
                    
                    for di,dj in near_cells:
                        if -1 < i + di < self.height and -1 < j + dj < self.width:
                            if not grid[i+di][j+dj]:
                                
                                ans += 1
                        else:
                            ans += 1
                else:
                    flag = 0
                    for di,dj in near_cells:
                        if -1 < i + di < self.height and -1 < j + dj < self.width:
                            if grid[i+di][j+dj]:
                               flag += 1
                    if flag == 4:
                        return -1
        return ans

    
    def normalize(self):
        
        rows, cols = zip(*self)
        imin, jmin = min(rows), min(cols)
        return Polyomino((i-imin, j-jmin) for i, j in self)

    def translate(self, numrows, numcols):
        
        return Polyomino((i+numrows, j+numcols) for i, j in self)
    
    def rotate_left(self):
        
        return Polyomino((-j, i) for i, j in self).normalize()

    def rotate_half(self):
        
        return Polyomino((-i, -j) for i, j in self).normalize()
    
    def rotate_right(self):
        
        return Polyomino((j, -i) for i, j in self).normalize()

    def reflect_vert(self):
        
        return Polyomino((-i, j) for i, j in self).normalize()

    def reflect_horiz(self):
        
        return Polyomino((i, -j) for i, j in self).normalize()

    def reflect_diag(self):
        
        return Polyomino((j, i) for i, j in self)

    def reflect_skew(self):
        
        return Polyomino((-j, -i) for i, j in self).normalize()

    
    def rotations(self):
        
        return [self,
                self.rotate_left(),
                self.rotate_half(),
                self.rotate_right()]

    # def

    def transforms(self):
        
        return [self,
                self.rotate_left(),
                self.rotate_half(),
                self.rotate_right(),
                self.reflect_vert(),
                self.reflect_horiz(),
                self.reflect_diag(),
                self.reflect_skew()]

    
    def symmetry(self):
        sym = ''
        if self == self.reflect_horiz():
            sym += '|'
        if self == self.reflect_vert():
            sym += '-'
        if self == self.reflect_diag():
            sym += '\\'
        if self == self.reflect_skew():
            sym += '/'
        if self == self.rotate_half():
            sym += '%'
        if self == self.rotate_left():
            sym += '@'
        if '|-' in sym:
            sym += '+'
        if '\\/' in sym:
            sym += 'X'
        if '@+X' in sym:
            sym += 'O'
        if not sym:
            sym = '?'
        return sym

    def children(self):
        
        childset = set()
        
        nbrs = set()
        for square in self:
            nbrs.update(_neighbors(square))
        nbrs -= self
        
        for nbr in nbrs:
            new = Polyomino(self | {nbr})
            
            if nbr[0] == -1:
                new = new.translate(1, 0)
            elif nbr[1] == -1:
                new = new.translate(0, 1)
            childset.add(new)
        return childset
