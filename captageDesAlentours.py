from random import *


# Capter les alentours
def alentours(grille):
    indexSommes = []
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            if i == 0 and j == 0:  # Si la cellule est dans le coin en haut a gauche
                somme = grille[i][j + 1] + grille[i + 1][j + 1] + grille[i + 1][j]

            elif i == 0 and j == (
                WIDTH - 1
            ):  # Si la cellule est dans le coin en haut a droite
                somme = grille[i + 1][j] + grille[i + 1][j - 1] + grille[i][j - 1]

            elif i == (HEIGH - 1) and j == (
                WIDTH - 1
            ):  # Si la cellule est dans le coin en bas a droite
                somme = grille[i - 1][j] + grille[i - 1][j - 1] + grille[i][j - 1]

            elif (
                i == (HEIGH - 1) and j == 0
            ):  # Si la cellule est dans le coin en bas a gauche
                somme = grille[i - 1][j] + grille[i - 1][j + 1] + grille[i][j + 1]

            elif i == 0:  # Si la cellule est sur le bord en haut
                somme = (
                    grille[i][j + 1]
                    + grille[i + 1][j + 1]
                    + grille[i + 1][j]
                    + grille[i + 1][j - 1]
                    + grille[i][j - 1]
                )

            elif j == (WIDTH - 1):  # Si la cellule est sur le bord a droite
                somme = (
                    grille[i + 1][j]
                    + grille[i + 1][j - 1]
                    + grille[i][j - 1]
                    + grille[i - 1][j - 1]
                    + grille[i - 1][j]
                )

            elif i == (HEIGH - 1):  # Si la cellule est sur le bord en bas
                somme = (
                    grille[i - 1][j]
                    + grille[i - 1][j + 1]
                    + grille[i][j + 1]
                    + grille[i - 1][j - 1]
                    + grille[i][j - 1]
                )

            elif j == 0:  # Si la cellule est sur le bord a gauche
                somme = (
                    grille[i - 1][j]
                    + grille[i - 1][j + 1]
                    + grille[i][j + 1]
                    + grille[i + 1][j + 1]
                    + grille[i + 1][j]
                )
            else:  # Si la cellule est au milieu
                somme = grille[i - 1][j]
                +grille[i - 1][j + 1]
                +grille[i - 1][j - 1]
                +grille[i][j + 1]
                +grille[i][j - 1]
                +grille[i + 1][j]
                +grille[i + 1][j - 1]
                +grille[i + 1][j + 1]
        indexSommes.append(somme)
    return indexSommes
