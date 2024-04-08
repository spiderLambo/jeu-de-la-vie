from random import *

HEIGH = 16
WIDTH = 16
lagrille = [[randint(0, 1) for i in range(WIDTH)] for i in range(HEIGH)]

NB_TOURS = 12


def change(grille):
    for i in grille:
        for j in i:
            # Code pour observer les alentours
            if 2 <= tour <= 3 and j == 1:
                # Code
                pass
            elif tour == 3 and j == 0:
                # Code
                pass


for i in range(NB_TOURS):
    print(lagrille)
    change(lagrille)
