from config.config import grid_height as gh, grid_width as gw
from random import randint

class Fish:
    def __init__(self, x:int, y:int):
        self.x=x
        self.y=y

    
    def move(self):
        new_x=0
        new_y=0

        while new_x==0 and new_y==0:
            new_x=randint(-1,1)
            new_y=randint(-1,1)

        self.x+=new_x
        self.y+=new_y
        if not (0 <= self.x < gw): self.x %= gw
        if not (0 <= self.y < gh): self.y %= gh