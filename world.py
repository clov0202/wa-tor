import os
import config as cfg
import grid

from time   import sleep
from random import randint, choice

from classes.fish  import Fish
from classes.tuna  import Tuna
from classes.shark import Shark


class World:

    def __init__(self):

        self._chronons_counter = 0
        self._grid_width = cfg.grid_width
        self._grid_height = cfg.grid_height
        
        self._tuna_population = cfg.tuna_population
        self._shark_population = cfg.shark_population
        self._world_grid_env = grid.WorldGrid(self._grid_width, self._grid_height)
        self.world_grid = self._world_grid_env.world_grid

        self._tunas_entities = []
        self._shark_entities = []

        self.first_fish_instanciations(Tuna, self._tuna_population)
        self.first_fish_instanciations(Shark, self._tuna_population)
                        


    def first_fish_instanciations(self, fish_kind:Tuna|Shark, fish_amount:int=1):

        water = set()
        for coordinate_y in range(self._grid_height):
            for coordinate_x in range(self._grid_width):
                if self.world_grid[coordinate_y, coordinate_x] == 0: 
                    water += (coordinate_x, coordinate_y)

        for fish in range(fish_amount):
            area = choice(water)
            self.fish_instanciation(self, fish_kind:Tuna|Shark, area[0], area[1]):
        

    def fish_instanciation(self, fish_kind:Tuna|Shark, x, y):

        self.world_grid[y][x] = fish_kind(x, y)


    def count_fish(self, fish_kind:Tuna|Shark|Fish):

        fish_count = 0
        if fish_kind == Fish : fish_kind = any(Tuna, Shark)

        for each_line in self.world_grid:
            fish_count += each_line.count(fish_kind)

        return fish_count

    


# def wator():

#     tunas = []
#     for i in range(1):
#         tunas.append(Fish(randint(0, cfg.grid_width),randint(0, cfg.grid_height)))

#     while True:

#         os.system('cls' if os.name == 'nt' else 'clear')  # efface le terminal



#         # grid = []
#         # for j in range(gh):
#         #     line=[]
#         #     for k in range(gw):
#         #         line.append(0)
#         #     grid.append(line)


#         for tuna in tunas:
#             grid[tuna.y][tuna.x]=1
#         for lines in grid:
#             for element in lines:
#                 if element==0:
#                     print("\033[94m ■ \033[0m", end="")
#                 else:
#                     print("\033[92m ■ \033[0m", end="")
#             print("")

#         for tuna in tunas:
#             tuna.move()

#         sleep(0.8)



# wator()