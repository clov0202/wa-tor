from config.config import grid_height as gh, grid_width as gw
from random import randint

# Classe parente pour gérer tous les poissons (thons et requins)
class Fish:
    def __init__(self, x:int, y:int):
        self.x = x 
        self.y = y
        # Cordonnées des poissons

    
    def move(self):
        new_x = 0
        new_y = 0

        while new_x==0 and new_y==0:
            new_x = randint(-1,1)
            new_y = randint(-1,1)
            # On instancie au hasard deux valeurs valant soit 1,
            # soit -1 ou 0 (on continue la boucle tant que 0 les deux vallent 0 pour que le
            # poisson ne reste pas sur place)
        
        self.x += new_x
        self.y += new_y
        # On incrémente/décrémente les coordonnées du poissons selon les valeurs obtenues
        # avec randint

        if not (0 <= self.x < gw): self.x %= gw

        if not (0 <= self.y < gh): self.y %= gh

        # Dans les conditions, on vérifie si x ou y sont plus petit que 0 ou dépasse la
        # longueur/largeur du tableau.

        # Si c'est le cas, on utilise le modulo pour calculer les nouvelles coordonées