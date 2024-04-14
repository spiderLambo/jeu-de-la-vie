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

    return nb


def new_grid(grille):
    # Calcul des dimentions de la grille
    largeur = len(grille[0])
    hauteur = len(grille)

    nouvelle_grille = [[0 for i in range(largeur)] for i in range(hauteur)]

    # Parcourir les cellules
    for y in range(len(grille)):
        for x in range(len(grille[0])):
            alentours = voisins(x, y, grille)
            # Règle 1 - Mort d'isolement
            if (
                grille[y][x] == 1 and alentours < 2
            ):  # Si la cellule est vivante et qu'elle a un nombre de voisins inférieur à deux
                nouvelle_grille[y][x] = 0  # alors elle meurt

            # Règle 2 - Toute cellule avec 2 ou 3 voisins survit.
            if grille[y][x] == 1 and (
                alentours in [2, 3]
            ):  # Si une cellule est vivante et qu'elle a deux ou trois voisins
                nouvelle_grille[y][x] = 1  # alors elle reste en vie

            # Règle 3 - Mort par surpopulation
            if (
                grille[y][x] == 1 and alentours > 3
            ):  # si une cellule est vivante et qu'elle a plus de trois voisins
                nouvelle_grille[y][x] = 0  # alors elle meurt

            # Règle 4 - Naissance
            if (
                grille[y][x] == 0 and alentours == 3
            ):  # si une cellule est morte et qu'elle a trois voisins
                nouvelle_grille[y][x] = 1  # alors elle nait (son état est à vivant)

    return nouvelle_grille
