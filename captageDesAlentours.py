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


def voisins(x, y, grille):
    nb = 0  # Initalisation du nombre de voisins
    # Calcul des dimentions de la grille
    largeur = len(grille[0])
    hauteur = len(grille)

    # diagonale haut-gauche
    if grille[(y - 1) % largeur][(x + 1) % hauteur] == 1:
        nb += 1

    # haut
    if grille[y][(x + 1) % hauteur] == 1:
        nb += 1

    # Diagonale haut-droite
    if grille[(y + 1) % largeur][(x + 1) % hauteur] == 1:
        nb += 1

    # gauche
    if grille[(y - 1) % largeur][x] == 1:
        nb += 1

    # droite
    if grille[(y + 1) % largeur][x] == 1:
        nb += 1

    # Diagonale bas-gauche
    if grille[(y - 1) % largeur][(x - 1) % hauteur] == 1:
        nb += 1

    # bas
    if grille[y][(x - 1) % hauteur] == 1:
        nb += 1

    # diagonale bas-droite
    if grille[(y + 1) % largeur][(x - 1) % hauteur] == 1:
        nb += 1

    return nb
