## GameOfPy

Basic Python implementation for [Conways Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life  "Conway's Game of Life"). 
Project uses naive approach, where each epoch state of each cell is calculated separately resulting in 8*x*y checks each generation for grid of width x and height y. However, there are some minor improvements:
- Cells "Wrap around", i.e. cells in the leftmost column have neighbours in the rightmost column 
- Number of checks made each generation is reduced through mantaining list of cells that might change, i.e. we know for certain that dead cell with no alive neighbours will stay dead for next generation, so we don't need to check it untill one if it neighbours becomes alive. 

#### Controls:
<kbd>Space</kbd> - Pause simulation
<kbd>→</kbd> - Show next generation (oly works in pause)
<kbd>Del</kbd> - Clear the grid
<kbd>↑</kbd> - Generate new random grid

#### To run:

1. Clone the repository

2. Install pygame with `pip install -U pygame --user`

3. run `python main.py`
