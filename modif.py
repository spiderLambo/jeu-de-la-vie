from random import *
from captageDesAlentours import *

HEIGH = 16
WIDTH = 16
lagrille = [[randint(0, 1) for i in range(WIDTH)] for i in range(HEIGH)]

NB_TOURS = 12


def change(grille):
    index = alentours(grille)
    for i in range(HEIGH * WIDTH + 1):
        somme = index[i]
        # Code pour observer les alentours
        if 2 <= somme <= 3 and (i % WIDTH) == 1:
            pass
        elif somme == 3 and (i % WIDTH) == 0:
            pass


for i in range(NB_TOURS):
    print(lagrille)
    change(lagrille)
