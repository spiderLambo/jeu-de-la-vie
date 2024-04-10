from random import *

# Taille du plateau
HEIGH = 4
WIDTH = 4

# création de la grille
grille = [[choice((1, 0)) for i in range(WIDTH)] for i in range(HEIGH)]
grille2=grille

# # * Tentatives pour avoir tout ce quil y as autours
# liste = []

# for i in range(len(grille)):
#     for j in range(len(grille[i])):
#         somme = []
#         somme.append(grille[i - 1][j - 1])
#         somme.append(grille[i - 1][j])
#         try:
#             somme.append(grille[i - 1][j + 1])
#         except:
#             somme.append(grille[i - 1][0])

#         somme.append(grille[i][j - 1])
#         somme.append(grille[i][j])
#         try:
#             somme.append(grille[i][j + 1])
#         except:
#             somme.append(grille[i][0])

#         try:
#             somme.append(grille[i + 1][j - 1])
#             somme.append(grille[i + 1][j])
#             try:
#                 somme.append(grille[i + 1][j + 1])
#             except:
#                 somme.append(grille[i + 1][0])
#         except:
#             somme.append(grille[0][j - 1])
#             somme.append(grille[0][j])
#             try:
#                 somme.append(grille[0][j + 1])
#             except:
#                 somme.append(grille[0][0])

#         liste.append(somme)

print("Grille1")
print(grille[0])
print(grille[1])
print(grille[2])
print(grille[3])
# print(grille[4])
# print(grille[5])
# print(grille[6])
# print(grille[7])
# print(grille[8])
# print(grille[9])
# print(grille[10])
# print(grille[11])
# print(grille[12])
# print(grille[13])
# print(grille[14])
# print(grille[15])
# print(liste[0])


#Capter les alentours

for i in range(len(grille)):
    for j in range(len(grille[i])):
        if i==0 and j==0:#Si la cellule est dans le coin en haut a gauche
            somme=grille[i][j+1]+grille[i+1][j+1]+grille[i+1][j]

        elif i==0 and j==(WIDTH-1):#Si la cellule est dans le coin en haut a droite
            somme=grille[i+1][j]+grille[i+1][j-1]+grille[i][j-1]

        elif i==(HEIGH-1) and j==(WIDTH-1):#Si la cellule est dans le coin en bas a droite
            somme=grille[i-1][j]+grille[i-1][j-1]+grille[i][j-1]

        elif i==(HEIGH-1) and j==0:#Si la cellule est dans le coin en bas a gauche
            somme=grille[i-1][j]+grille[i-1][j+1]+grille[i][j+1]

        elif i==0 :#Si la cellule est sur le bord en haut
            somme=grille[i][j+1]+grille[i+1][j+1]+grille[i+1][j]+grille[i+1][j-1]+grille[i][j-1]

        elif j==(WIDTH-1):#Si la cellule est sur le bord a droite
            somme=grille[i+1][j]+grille[i+1][j-1]+grille[i][j-1]+grille[i-1][j-1]+grille[i-1][j]

        elif i==(HEIGH-1):#Si la cellule est sur le bord en bas
            somme=grille[i-1][j]+grille[i-1][j+1]+grille[i][j+1]+grille[i-1][j-1]+grille[i][j-1]

        elif j==0:#Si la cellule est sur le bord a gauche
            somme=grille[i-1][j]+grille[i-1][j+1]+grille[i][j+1]+grille[i+1][j+1]+grille[i+1][j]
        else: #Si la cellule est au milieu
            somme=grille[i-1][j]
            +grille[i-1][j+1]
            +grille[i-1][j-1]
            +grille[i][j+1]
            +grille[i][j-1]
            +grille[i+1][j]
            +grille[i+1][j-1]
            +grille[i+1][j+1]
            

        #Savoir si la cellule est morte ou vivant
        if grille[i][j] == 1:#Si cellule vivante
            if somme == 2 or somme ==3:
                grille2[i][j]=1 #Reste comme elle est
            else:
                grille2[i][j]=0 #Elle meurt
        else:#Si cellule morte
            if somme ==3:
                grille2[i][j]=1 #Naissance d'une cellule
            else:
                grille2[i][j]=0 #Reste comme elle est
        somme=0 #Reinitialisation de la somme

print("Grille2")
print(grille2[0])
print(grille2[1])
print(grille2[2])
print(grille2[3])
# print(grille2[4])
# print(grille2[5])
# print(grille2[6])
# print(grille2[7])
# print(grille2[8])
# print(grille2[9])
# print(grille2[10])
# print(grille2[11])
# print(grille2[12])
# print(grille2[13])
# print(grille2[14])
# print(grille2[15])







