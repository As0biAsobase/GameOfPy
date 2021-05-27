import random
class Cell():
    def __init__(self, width=0, height=0, row=0, column=0, mode="default"):
        # various modes for starting value
        if mode == "default":
            self.value = random.choice([0, 1])
        elif mode == "zeroes":
            self.value = 0
