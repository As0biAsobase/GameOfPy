from Cell import Cell
import numpy as np

class Grid():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # Initialize 2d grid of cells
        self.grid = np.array([[Cell() for _ in range(height)] for _ in range(width)])

        # 2d array to keep track of cells that might change
        self.change_grid = np.array([[1 for _ in range(height)] for _ in range(width)])

        # self.create_spaceship()
        
    def create_spaceship(self):
        self.grid[105][10].value = 1
        self.grid[105][11].value = 1
        self.grid[106][9].value = 1
        self.grid[106][10].value = 1
        self.grid[107][11].value = 1

        self.grid[108][13].value = 1
        self.grid[108][14].value = 1

        self.grid[109][12].value = 1

        self.grid[111][11].value = 1
        self.grid[111][14].value = 1

        self.grid[112][8].value = 1
        self.grid[112][9].value = 1
        self.grid[112][11].value = 1

        self.grid[113][7].value = 1
        self.grid[113][8].value = 1
        self.grid[113][13].value = 1

        self.grid[114][9].value = 1
        self.grid[114][11].value = 1
        self.grid[114][14].value = 1

        self.grid[115][14].value = 1

        self.grid[116][11].value = 1
        self.grid[116][14].value = 1

        self.grid[117][12].value = 1
        self.grid[117][14].value = 1

        self.grid[118][12].value = 1
        self.grid[118][14].value = 1

        self.grid[119][13].value = 1
        self.grid[119][14].value = 1

        self.grid[120][13].value = 1

    # kill or revive specific cell 
    def revert_cell(self, row, column):
        # if cell is alive - kill it, revive it otherwise
        value = self.grid[row, column].reverse_value()

        one_left = column-1 if column > 0 else self.width-1
        one_right = column+1 if column < self.width-1 else 0
        one_top = row-1 if row > 0 else self.height-1
        one_bottom = row+1 if row < self.height-1 else 0

        neighbours = [
            (one_top, one_left), (one_top, column), (one_top, one_right),
            (row, one_left),                             (row, one_right),
            (one_bottom, one_left), (one_bottom, column), (one_bottom, one_right),
        ]

        alive = self.get_number_of_alive_neighbours(neighbours)
        self.update_change(row, column, neighbours, value, alive)

        
        return value

    # kill all cells on the grid
    def clear_grid(self):
        self.grid = np.array([[Cell(mode="zeroes") for _ in range(self.height)] for _ in range(self.width)])
        self.change_grid = np.array([[1 for _ in range(self.height)] for _ in range(self.width)]) 

    # generate states for cells randomly
    def generate_random_grid(self):
        self.grid = np.array([[Cell() for _ in range(self.height)] for _ in range(self.width)])
        self.change_grid = np.array([[1 for _ in range(self.height)] for _ in range(self.width)])


    def get_number_of_alive_neighbours(self, neighbours):
        alive = 0
        for x, y in neighbours:
            alive += self.grid[x, y].value

        return alive

    def is_dead(self, row, column):
        # Is cell dead?
        is_dead = True if self.grid[row, column].value == 0 else False
        # if no neighbours wrap around
        one_left = column-1 if column > 0 else self.width-1
        one_right = column+1 if column < self.width-1 else 0
        one_top = row-1 if row > 0 else self.height-1
        one_bottom = row+1 if row < self.height-1 else 0

        # each cell has 8 neighbours, store their coordinates in array
        neighbours = [
            (one_top, one_left), (one_top, column), (one_top, one_right),
            (row, one_left),                             (row, one_right),
            (one_bottom, one_left), (one_bottom, column), (one_bottom, one_right),
        ]

        # calculate number of alive neighbours
        alive = self.get_number_of_alive_neighbours(neighbours)

        resurrected = 0
        if is_dead == True: # Any dead cell
            if alive == 3: # with three live neighbours
                is_dead = False #becomes a live cell.
                resurrected = 1
        else: # Any live cell
            if alive not in [2, 3]: # not with two or three live neighbours
                is_dead = True # dies.
        # All other cell keep their state for the next generation.

        # update "danger zone" array
        self.update_change(row, column, neighbours, resurrected, alive)

        return is_dead

    def update_change(self, row, column, neighbours, resurrected, alive):
        # if cell has alive neighbours it might change its state next time
        self.change_grid[row, column] = 1 if alive > 0 else 0
        # if cell became revived this generation all its neighbours are now in "danger zone" as well
        if resurrected == 1:
            for x, y in neighbours:
                self.change_grid[x, y] = 1
