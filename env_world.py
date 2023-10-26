from random import randint
import copy

monde = [[0 for i in range(10)] for y in range(10)]



# Logique des poissons
count_poissons = 0
while count_poissons < 10:
    row = randint(0, 9)
    col = randint(0, 9)
    if monde[row][col] == 0:
        monde[row][col] = 1
        count_poissons += 1
            
# Logique des requins
count_requins = 0
while count_requins < 5:
    row = randint(0, 9)
    col = randint(0, 9)
    if monde[row][col] == 0:
        monde[row][col] = 2
        count_requins += 1

# Créer une copie de la grille après l'apparition des poissons et des requins
monde_initial = copy.deepcopy(monde)

# print 3 fois la grille pour vérifier si les poissons et requins bougent
for i in monde_initial:
    print(*i)
print()
for i in monde_initial:
    print(*i)
print()
for i in monde_initial:
    print(*i)