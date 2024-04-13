from func import *
import pygame as pgm
from random import *

HEIGH = 16
WIDTH = 16
grille = [[randint(0, 1) for i in range(WIDTH)] for i in range(HEIGH)]

pgm.init()  # Initialiser la fenetre

TAILLE_FENETRE = (WIDTH * 40, HEIGH * 40)

screen = pgm.display.set_mode(TAILLE_FENETRE)  # Afficher la fenetre


run = True
while run:
    # Fermeture de la fenetre
    for event in pgm.event.get():
        if event.type == pgm.QUIT:
            run = False
        if event.type == pgm.KEYDOWN and event.key == pgm.K_RIGHT:
            grille = new_grid(grille)

    screen.fill((250, 250, 250))  # Changer la couleur de fond

    # Dessin de la grille
    for y in range(len(grille)):
        for x in range(len(grille[y])):
            if grille[y][x] == 1:
                pgm.draw.rect(screen, (0, 0, 0), [x * 40, y * 40, 40, 40])
            else:
                pgm.draw.rect(screen, (0, 0, 0), [x * 40, y * 40, 40, 40], 1)

    pgm.display.flip()  # Actualisation de la fenetre
