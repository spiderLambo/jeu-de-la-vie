from funcLENIA import *
import pygame as pgm
from random import *

# dimentions, taille_pixels = int(input("Quelle dimentions : ")), int(
#     input("Quelle taille de pixels : ")
# )
# grille = [[random() for i in range(dimentions)] for i in range(dimentions)]

pgm.init()  # Initialiser la fenetre


screen = pgm.display.set_mode((300, 300))  # Afficher la fenetre
pgm.display.set_caption("Jeu de la vie")

compteur = 0  # Initalisation du compteur
arialFont = pgm.font.SysFont("arial", 20)
texte_compteur = arialFont.render("Generation 0", 1, (0, 0, 0))
titre = arialFont.render("Le jeu de la vie de Conway", 1, (0, 0, 0))
play = arialFont.render("Jouer", 1, (0, 0, 0))
dim_txt = arialFont.render("Nombre de cellules par coté", 1, (0, 0, 0))
taille_txt = arialFont.render("Taille des pixels", 1, (0, 0, 0))
start = arialFont.render("Commencer", 1, (0, 0, 0))
parametre = False
jouer = False
play_rect = pgm.Rect(120, 150, 43, 20)
start_rect = pgm.Rect(100, 250, 92, 20)
dim_rect = pgm.Rect(10, 100, 100, 30)
taille_rect = pgm.Rect(10, 200, 100, 30)
dimentions = ""
taille_pixels = ""

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
                jouer = True
            # Zones de textes
            if dim_rect.collidepoint(event.pos):
                dim_active = True
            else:
                dim_active = False

        if event.type == pgm.KEYDOWN:
            if dim_active:
                # Ecrire dans les zones de textes
                if event.key == pgm.K_BACKSPACE:
                    dimentions = dimentions[:-1]  # Faire fonctionner la fleche retours
                else:
                    dimentions += event.unicode

            # Changer de grille
            if event.key == pgm.K_RIGHT:
                grille = new_grid(grille)
                compteur += 1  # Incrementation du compteur
                texte_compteur = arialFont.render(
                    f"Generation {compteur}", 1, (0, 0, 0)
                )  # Actualisation du compteur

    screen.fill((250, 250, 250))  # Changer la couleur de fond

    if parametre:
        # Dessin des textes
        screen.blit(dim_txt, (10, 50))
        screen.blit(taille_txt, (10, 150))
        screen.blit(start, (100, 250))

        # Changer la couleur du cadre
        if dim_active:
            dim_color = (100, 200, 255)
        else:
            dim_color = (100, 100, 100)

        # Dessin des zones de textes
        pgm.draw.rect(screen, dim_color, dim_rect, 2)

        # Afficher le texte capté
        dim_txt_surface = arialFont.render(dimentions, 1, (0, 0, 0))
        screen.blit(dim_txt_surface, (dim_rect.x + 5, dim_rect.y))

        # Elargir le rectangle au besoin
        dim_rect.w = max(100, dim_txt_surface.get_width() + 10)
        # screen = pgm.display.set_mode(
        #     (dimentions * taille_pixels, dimentions * taille_pixels + 50)
        # )  # Afficher la fenetre
        # # Dessin de la grille
        # for y in range(len(grille)):
        #     for x in range(len(grille[y])):
        #         pgm.draw.rect(
        #             screen,
        #             (0, int(grille[y][x] * 255), int(grille[y][x] * 255)),
        #             [
        #                 x * taille_pixels,
        #                 y * taille_pixels,
        #                 taille_pixels,
        #                 taille_pixels,
        #             ],
        #         )

        # screen.blit(texte_compteur, (5, dimentions * taille_pixels + 5))
    else:
        screen.blit(titre, (50, 50))
        screen.blit(play, (120, 150))

    pgm.display.flip()  # Actualisation de la fenetre
