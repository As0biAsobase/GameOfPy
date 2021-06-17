import random
class Cell():
    def __init__(self, width=0, height=0, row=0, column=0, mode="default"):
        # various modes for starting value
        if mode == "default":
            self.value = random.choice([0, 1])
        elif mode == "zeroes":
            self.value = 0 

        self.neighbours = self.calculate_neighbours(row, column, width, height)
        

    def reverse_value(self):
        if self.value == 0:
            self.value = 1
        else:
            self.value = 0 

        return self.value

    def calculate_neighbours(self, row, column, width, height):
        # if no neighbours wrap around
        one_left = column-1 if column > 0 else width-1
        one_right = column+1 if column < width-1 else 0
        one_top = row-1 if row > 0 else height-1
        one_bottom = row+1 if row < height-1 else 0
        
         # each cell has 8 neighbours, store their coordinates in array
        neighbours = [
            (one_top, one_left), (one_top, column), (one_top, one_right),
            (row, one_left),                             (row, one_right),
            (one_bottom, one_left), (one_bottom, column), (one_bottom, one_right),
        ]

        return neighbours
