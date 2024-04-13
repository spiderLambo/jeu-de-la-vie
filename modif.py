from random import *
from captageDesAlentours import *

HEIGH = 16
WIDTH = 16
lagrille = [[randint(0, 1) for i in range(WIDTH)] for i in range(HEIGH)]

NB_TOURS = 2


def change(grille, height, width):
    index = alentours(grille)
    new_grille = [[] for i in range(HEIGH)]
    for i in range(HEIGH * WIDTH + 1):
        somme = index[i]
        # Code pour observer les alentours
        if (2 <= somme <= 3 and grille[i // WIDTH][i % WIDTH] == 1) or (somme == 3 and grille[i // WIDTH][i % WIDTH] == 0):
            grille[i // WIDTH].append(1)
        else:
            grille[i // WIDTH].append(0)
    return new_grille


for i in range(NB_TOURS):
    print(lagrille)
    change(lagrille)
