# Importation des librairies
from func import *
import pygame as pgm
from random import randint


pgm.init()  # Initialiser la fenetre
clock = pgm.time.Clock()

# Afficher la fenetre
screen = pgm.display.set_mode((300, 300))
pgm.display.set_caption("Ludo de la Vivo")

compteur = 0  # Initalisation du compteur
# Création des textes
arialFont = pgm.font.SysFont("arial", 20)
titre = arialFont.render("Ludo de la Vivo de Conway", 1, (0, 0, 0))
play = arialFont.render("Ludadi", 1, (0, 0, 0))
dim_txt = arialFont.render("Nombro de ĉeloj po flanko", 1, (0, 0, 0))
taille_txt = arialFont.render("Grandeco de pikselo", 1, (0, 0, 0))
start = arialFont.render("Komenci", 1, (0, 0, 0))
gen = arialFont.render("Generacio 0", 1, (0, 0, 0))
# Booleen pour l'affichage des fenetres
parametre = False
jouer = False
# Zones de click
play_rect = pgm.Rect(120, 150, 43, 20)
start_rect = pgm.Rect(100, 250, 92, 20)
dim_rect = pgm.Rect(10, 100, 100, 30)
taille_rect = pgm.Rect(10, 200, 100, 30)
# Zones de texte des zones clickables
dimentions = ""
taille_pixels = ""
# Booleen pour la selection des zones de texte
dim_active = False
taille_active = False


run = True
while run:
    for event in pgm.event.get():
        # Fermeture de la fenetre
        if event.type == pgm.QUIT:
            run = False

        if event.type == pgm.MOUSEBUTTONDOWN:
            # Activer la fenetre des parametres
            if play_rect.collidepoint(event.pos):
                parametre = True

            # Demarer la simulation
            if start_rect.collidepoint(event.pos):
                dimentions = int(dimentions)
                taille_pixels = int(taille_pixels)
                jouer = True
                grille = [
                    [randint(0, 1) for i in range(dimentions)]
                    for i in range(dimentions)
                ]
            # Zones de textes
            if dim_rect.collidepoint(event.pos):
                dim_active = True
            else:
                dim_active = False
            if taille_rect.collidepoint(event.pos):
                taille_active = True
            else:
                taille_active = False

        if event.type == pgm.KEYDOWN:
            if dim_active:
                # Ecrire dans les zones de textes
                if event.key == pgm.K_BACKSPACE:
                    dimentions = dimentions[:-1]  # Faire fonctionner la fleche retours
                else:
                    dimentions += event.unicode

            if taille_active:
                # Ecrire dans les zones de textes
                if event.key == pgm.K_BACKSPACE:
                    taille_pixels = taille_pixels[
                        :-1
                    ]  # Faire fonctionner la fleche retours
                else:
                    taille_pixels += event.unicode

            # Changer de grille
            if event.type == pgm.KEYDOWN and event.key == pgm.K_RIGHT:
                grille = new_grid(grille)
                compteur += 1  # Incrementation du compteur
                gen = arialFont.render(
                    f"Generacio {compteur}", 1, (0, 0, 0)
                )  # Actualisation du compteur

    screen.fill((250, 250, 250))  # Changer la couleur de fond

    if parametre and not jouer:
        # Dessin des textes
        screen.blit(dim_txt, (10, 50))
        screen.blit(taille_txt, (10, 150))
        screen.blit(start, (100, 250))

        # Changer la couleur du cadre
        if dim_active:
            dim_color = (100, 200, 255)
        else:
            dim_color = (100, 100, 100)
        if taille_active:
            taille_color = (100, 200, 255)
        else:
            taille_color = (100, 100, 100)

        # Dessin des zones de textes
        pgm.draw.rect(screen, dim_color, dim_rect, 2)
        pgm.draw.rect(screen, taille_color, taille_rect, 2)

        # Afficher le texte capté
        dim_txt_surface = arialFont.render(dimentions, 1, (0, 0, 0))
        screen.blit(dim_txt_surface, (dim_rect.x + 5, dim_rect.y))
        taille_txt_surface = arialFont.render(taille_pixels, 1, (0, 0, 0))
        screen.blit(taille_txt_surface, (taille_rect.x + 5, taille_rect.y))

        # Elargir le rectangle au besoin
        dim_rect.w = max(100, dim_txt_surface.get_width() + 10)
        taille_rect.w = max(100, taille_txt_surface.get_width() + 10)
    # Commencer la simulation
    elif jouer:
        screen = pgm.display.set_mode(
            (dimentions * taille_pixels, dimentions * taille_pixels + 50)
        )  # Afficher la fenetre
        screen.fill((250, 250, 250))  # Changer la couleur de fond
        # Parcourir la grille
        for y in range(len(grille)):
            for x in range(len(grille[y])):
                if grille[y][x] == 1:
                    pgm.draw.rect(
                        screen,
                        (0, 0, 0),
                        [
                            x * taille_pixels,
                            y * taille_pixels,
                            taille_pixels,
                            taille_pixels,
                        ],
                    )
                else:
                    pgm.draw.rect(
                        screen,
                        (0, 0, 0),
                        [
                            x * taille_pixels,
                            y * taille_pixels,
                            taille_pixels,
                            taille_pixels,
                        ],
                        1,
                    )
        screen.blit(
            gen, (5, dimentions * taille_pixels + 5)
        )  # Affichage de la zone du numéro de la generation
    # Ecran titre
    else:
        screen.blit(titre, (50, 50))
        screen.blit(play, (120, 150))

    pgm.display.flip()  # Actualisation de la fenetre
    clock.tick(60)  # 60 images par secondes
