# Fonction qui revoie la nouvelle valeur en fonction du nombre de voisins
def lenia_graph(number):
    if 0.444 < number < 3.156:
        return -0.5 * number * number + 1.8 * number - 0.7
    else:
        return 0


def voisins(x, y, grille):
    nb = 0  # Initalisation du nombre de voisins
    # Calcul des dimentions de la grille
    largeur = len(grille[0])
    hauteur = len(grille)

    # calcul de la somme des voisins
    nb = (
        grille[(y - 1) % largeur][(x + 1) % hauteur]  # diagonale haut-gauche
        + grille[y][(x + 1) % hauteur]  # haut
        + grille[(y + 1) % largeur][(x + 1) % hauteur]  # Diagonale haut-droite
        + grille[(y - 1) % largeur][x]  # gauche
        + grille[(y + 1) % largeur][x]  # droite
        + grille[(y - 1) % largeur][(x - 1) % hauteur]  # Diagonale bas-gauche
        + grille[y][(x - 1) % hauteur]  # bas
        + grille[(y + 1) % largeur][(x - 1) % hauteur]  # diagonale bas-droite
    )

    return lenia_graph(nb)


def new_grid(grille):
    # Calcul des dimentions de la grille
    largeur = len(grille[0])
    hauteur = len(grille)

    nouvelle_grille = [[0 for i in range(largeur)] for i in range(hauteur)]

    # Parcourir les cellules
    for y in range(len(grille)):
        for x in range(len(grille[0])):
            # Nouvelle valeur
            nouvelle_grille[y][x] = voisins(x, y, grille)

    return nouvelle_grille
