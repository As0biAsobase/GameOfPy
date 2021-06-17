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
    ROWS = 100
    COLUMNS = 100

    # Initialize pygame and start a main loop
    def draw(self):
        pygame.init()
        WINDOW_SIZE = [1000, 1000]
        screen = pygame.display.set_mode(WINDOW_SIZE)

        # Initialize grid
        grid = Grid(Interface.ROWS, Interface.COLUMNS)

        # Set pause
        pause = False

        # Loop until the user clicks the close button.
        done = False

        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()

        # -------- Main Program Loop -----------
        i = 0
        while done != True:
            i += 1
            for event in pygame.event.get():
                # end loop if user quits
                if event.type == pygame.QUIT:
                    done = True
                # if user presses button
                elif event.type == pygame.KEYDOWN:
                    # If it is a space bar puse the game
                    if event.key == pygame.K_SPACE:
                        pause = not  pause
                    # if it is a right arrow key create one generation
                    elif event.key == pygame.K_RIGHT:
                        # only crete genertion if game is paused
                        if pause == True:
                            grid_new = self.draw_epoch(grid, screen)
                            grid.grid = grid_new
                    # if DELETE key was pressed clear the grid
                    elif event.key == pygame.K_DELETE:
                        grid.clear_grid()
                    # if an up arrow key was pressed generae new random grid
                    elif event.key == pygame.K_UP:
                        grid.generate_random_grid()
                # check if mouse button was pressed
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # only do that in pause mode
                    if pause == True: 
                        # record coursor position
                        pos = pygame.mouse.get_pos() 
                        # updae cell at which mouse points
                        self.update_cell(grid, screen, pos)

            # if game is not paused create generations normally
            if pause == False:
                # Set the screen background
                screen.fill(Interface.BLACK)

                # generate and draw epcoch
                grid_new = self.draw_epoch(grid, screen)

                # update grid with the new state
                grid.grid = grid_new

            # Limit to 60 frames per second
            clock.tick(60)

            # Update the screen
            pygame.display.update()

        # Prevent hang if idle
        pygame.quit()

    def update_cell(self, grid, screen, pos):
        # unpack mouse positions
        horizontal, vertical = pos 
        # check if a cell on a grid was clicked
        if horizontal <= Interface.WIDTH * Interface.ROWS and vertical <= Interface.WIDTH*Interface.COLUMNS:
            # calculate which cell should b updated
            column = horizontal // Interface.WIDTH 
            row = vertical // Interface.HEIGHT

            # get new cell state to draw
            if grid.revert_cell(row, column) == 0:
                color = Interface.BLACK
            else:
                color = Interface.WHITE

            rect = pygame.draw.rect(screen, color, [
                                        (Interface.MARGIN + Interface.WIDTH) * column + Interface.MARGIN,
                                        (Interface.MARGIN + Interface.HEIGHT) * row + Interface.MARGIN, Interface.WIDTH, Interface.HEIGHT])

            pygame.display.update(rect)

    def draw_epoch(self, grid, screen):
        # Create another grid to preserve state throughout checks
        grid_new = np.array([[Cell(mode="zeroes", width=Interface.COLUMNS, height=Interface.ROWS, row=row, column=column) for column in range(grid.height)] for row in range(grid.width)])

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

        return grid_new