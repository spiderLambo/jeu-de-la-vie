from random import *

# Taille du plateau
HEIGH = 16
WIDTH = 16

# création de la grille
grille = [[choice((True, False)) for i in range(WIDTH)] for i in range(HEIGH)]


# * Tentatives pour avoir tout ce quil y as autours
liste = []

for i in range(len(grille)):
    for j in range(len(grille[i])):
        somme = []
        somme.append(grille[i - 1][j - 1])
        somme.append(grille[i - 1][j])
        try:
            somme.append(grille[i - 1][j + 1])
        except:
            somme.append(grille[i - 1][0])

        somme.append(grille[i][j - 1])
        somme.append(grille[i][j])
        try:
            somme.append(grille[i][j + 1])
        except:
            somme.append(grille[i][0])

        try:
            somme.append(grille[i + 1][j - 1])
            somme.append(grille[i + 1][j])
            try:
                somme.append(grille[i + 1][j + 1])
            except:
                somme.append(grille[i + 1][0])
        except:
            somme.append(grille[0][j - 1])
            somme.append(grille[0][j])
            try:
                somme.append(grille[0][j + 1])
            except:
                somme.append(grille[0][0])

        liste.append(somme)

print(grille)
print(liste[0])
