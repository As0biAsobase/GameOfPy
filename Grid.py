from Cell import Cell
import numpy as np

class Grid():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # Initialize 2d grid of cells
        self.grid = np.array([[Cell() for _ in range(height)] for _ in range(width)])

    def get_number_of_alive_neighbours(neighbours):
        alive = 0
        for each in neighbours:
            if each.value == 1:
                alive += 1

        return alive

    def is_dead(self, row, column):
        # Is cell dead?
        is_dead = True if self.grid[row][column].value == 0 else False
        # if no neighbours wrap around
        one_left = column-1 if column > 0 else self.width-1
        one_right = column+1 if column < self.width-1 else 0
        one_top = row-1 if row > 0 else self.height-1
        one_bottom = row+1 if row < self.height-1 else 0

        # each cell has 8 neighbours, store them all in array
        neighbours = [
            self.grid[one_top][one_left], self.grid[one_top][column], self.grid[one_top][one_right],
            self.grid[row][one_left]                                , self.grid[row][one_right],
            self.grid[one_bottom][one_left], self.grid[one_bottom][column], self.grid[one_bottom][one_right],
        ]

        # calculate number of alive neighbours
        alive = Grid.get_number_of_alive_neighbours(neighbours)

        if is_dead == True: # Any dead cell
            if alive == 3: # with three live neighbours
                is_dead = False #becomes a live cell.
        else: # Any live cell
            if alive not in [2, 3]: # not with two or three live neighbours
                is_dead = True # dies.
        # All other cell keep their state for the next generation.


        return is_dead
