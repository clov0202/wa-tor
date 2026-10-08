import config as cfg

# cg.grid_height


world_grid = []

for line in range(cfg.grid_height):
    world_grid.append([])
    lane = ""
    for colonne in range(cfg.grid_width):
        lane = ""
        world_grid[line].append(0)


for i in range(100):
    print(f"{i} \033[{i}m██    \033[0m")

# for i in range(len(world_grid)):
#     print(world_grid[line])



grid_width:int = 15
grid_height:int = 15

x=-1
y=17


# gestion des dépassements de frontières.
if x < 0 : x = grid_width + x 
if y < 0 : y = grid_height + y 

if x > grid_width : x =  x - grid_width
if y > grid_height : y =  y - grid_height

print("\n", x, y)

# cherche autour des coordonnées.
for line in range(y-1, y+2):
    for colonne in range(x-1, x-2):
        world_grid[x][y] == '???'