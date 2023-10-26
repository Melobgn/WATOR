from random import randint
import copy
import random


monde = [[0 for i in range(10)] for y in range(10)]
nombre_poissons = 10
nombre_requins = 5

random.seed(12)   
# Logique des poissons
for i in range(nombre_poissons):
    
    row = randint(0, 9)
    col = randint(0, 9)
    if monde[row][col] == 0:
            monde[row][col] = 1

# Logique des requins
for i in range(nombre_requins):
    row = randint(0, 9)
    col = randint(0, 9)
    if monde[row][col] == 0:
        monde[row][col] = 2

monde_init = copy.deepcopy(monde)

    
# affiche le monde
for i in monde_init:
    print(*i)
print()









      
        




