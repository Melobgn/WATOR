from random import randint
import random

monde = [[0 for i in range(10)] for y in range(10)]

# logique des poissons
count = 0
while count < 10:
    row = random.randint(0, 9)  # Génére une ligne aléatoire de 0 à 9
    col = random.randint(0, 9)  # Génére une colonne aléatoire de 0 à 9

    if monde[row][col] == 0:
        monde[row][col] = 1
        count += 1

# logique des requins
count = 0
while count < 5:
    row = random.randint(0,9)
    col = random.randint(0,9)

    if monde[row][col] == 0:
        monde[row][col] = 2
        count += 1

# affiche la grille
for row in monde:
    print(row)