from func import *
import pygame as pgm
from random import *

dimentions, taille_pixels = int(input("Quelle dimentions : ")), int(
    input("Quelle taille de pixels : ")
)
grille = [[randint(0, 1) for i in range(dimentions)] for i in range(dimentions)]

pgm.init()  # Initialiser la fenetre

screen = pgm.display.set_mode(
    (dimentions * taille_pixels, dimentions * taille_pixels + 50)
)  # Afficher la fenetre

compteur = 0  # Initalisation du compteur
font = pgm.font.Font(None, 24)
text = font.render("Generation 0", 1, (0, 0, 0))

run = True
while run:
    # Fermeture de la fenetre
    for event in pgm.event.get():
        if event.type == pgm.QUIT:
            run = False
        if event.type == pgm.KEYDOWN and event.key == pgm.K_RIGHT:
            grille = new_grid(grille)
            compteur += 1  # Incrementation du compteur
            text = font.render(f"Generation {compteur}", 1, (0, 0, 0))

    screen.fill((250, 250, 250))  # Changer la couleur de fond

    # Dessin de la grille
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
    screen.blit(text, (5, dimentions * taille_pixels + 5))

    pgm.display.flip()  # Actualisation de la fenetre
