import pygame
import copy
import numpy as np
import time

from Grid import Grid
from Cell import Cell

class Interface():
    BLACK = (0, 0, 0)
    WHITE = (200, 200, 200)
    # Color vars here

    # Grid vars
    WIDTH = 4
    HEIGHT = 4
    MARGIN = 0

    # Initialize pygame
    def draw(self):
        pygame.init()
        WINDOW_SIZE = [1000, 1000]
        screen = pygame.display.set_mode(WINDOW_SIZE)

        # Initialize grid
        grid = Grid(250, 250)


        # Loop until the user clicks the close button.
        done = False

        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()

        # -------- Main Program Loop -----------
        i = 0
        while done != True:
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            # Set the screen background
            screen.fill(Interface.BLACK)

            # Create another grid to preserve state throughout checks
            grid_new = np.array([[Cell(mode="zeroes") for row in range(grid.height)] for column in range(grid.width)])

            # Draw the grid
            for row in range(grid.height):
                for column in range(grid.width):
                    # check if cell is in "danger zone", i.e. can be changed on this iteration
                    if grid.change_grid[row, column] == 1:
                    # Check if cell should die in next iteration and change color
                        if grid.is_dead(row, column):
                            color = Interface.BLACK
                            grid_new[row, column].value = 0
                        else:
                            color = Interface.WHITE
                            grid_new[row, column].value = 1
                        # Draw rectangle

                        pygame.draw.rect(screen, color, [
                                    (Interface.MARGIN + Interface.WIDTH) * column + Interface.MARGIN,
                                    (Interface.MARGIN + Interface.HEIGHT) * row + Interface.MARGIN, Interface.WIDTH, Interface.HEIGHT])
            # update grid with the new state
            grid.grid = grid_new
            # Limit to 60 frames per second
            clock.tick(60)

            # Update the screen
            pygame.display.update()

        # Prevent hang if idle
        pygame.quit()
