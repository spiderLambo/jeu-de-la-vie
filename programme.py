from random import *

# Taille du plateau
HEIGH = 16
WIDTH = 16

# création de la grille
grille = [[choice((True, False)) for i in range(WIDTH)] for i in range(HEIGH)]
