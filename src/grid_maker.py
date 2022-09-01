import numpy as np
import random


class grid:

    def __init__(self, grid_dim = [50, 100], terrain = [50, 20, 20, 10], start = None):
        self.grid_dim = grid_dim
        self.terrain = terrain
        self.start = start

    def grid_gen(self):
        y = self.grid_dim[0]
        x = self.grid_dim[1]
        area = x*y

        h_cells = int(self.terrain[1]/100 * area)
        t_cells = int(self.terrain[2]/100 * area)
        b_cells = int(self.terrain[3]/100 * area)

        state_space = np.full(shape=(y,x), fill_value='N')


        for h in range(h_cells):
            _y = random.randint(0, y-1)
            _x = random.randint(0, x-1)
            while state_space[_y, _x] != 'N':
                _y = random.randint(0, y-1)
                _x = random.randint(0, x-1)
            state_space[_y, _x] = 'H'
        
        for t in range(t_cells):
            _y = random.randint(0, y-1)
            _x = random.randint(0, x-1)
            while state_space[_y, _x] != 'N':
                _y = random.randint(0, y-1)
                _x = random.randint(0, x-1)
            state_space[_y, _x] = 'T'

        for b in range(b_cells):
            _y = random.randint(0, y-1)
            _x = random.randint(0, x-1)
            while state_space[_y, _x] != 'N' and [_y, _x] != self.start:
                _y = random.randint(0, y-1)
                _x = random.randint(0, x-1)
            state_space[_y, _x] = 'B'

        if self.start == None:
            state_values = np.full(shape=(y,x), fill_value=1/(area-b_cells))
            for i in range(0, x):
                for j in range(0, y):
                    if state_space[j,i] == 'B':
                        state_values[j,i] = 0

        return state_space, state_values
            