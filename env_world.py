from random import randint
import random

monde = [[0 for i in range(10)] for y in range(10)]

# logique des poissons
poissons = 0
while poissons < 10:
    row = random.randint(0, 9)  # Génére une ligne aléatoire de 0 à 9
    col = random.randint(0, 9)  # Génére une colonne aléatoire de 0 à 9

    if monde[row][col] == 0:
        monde[row][col] = 1
        poissons += 1

# logique des requins
requins = 0
while requins < 5:
    row = random.randint(0,9)
    col = random.randint(0,9)

    if monde[row][col] == 0:
        monde[row][col] = 2
        requins += 1
    

# affiche la grille
for row in monde:
    print(row)


#HAUT,BAS,GAUCHE,DROITE
mouvement = [[0,-1],[0,1],[-1,0],[1,0]]
 
for poisson in poissons:
    deplacement = random.choice(mouvement) #On choisit son mouvement
    print(deplacement)

def choisir_case(row, col):
    ligne = random.mouvement()
    colonne = random.mouvement()
    if x > row-1 or y > col-1:
        ligne = random.mouvement()
        colonne = random.mouvement()
    return (ligne, colonne)

