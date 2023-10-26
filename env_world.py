from random import randint
import copy
import random


taille = 10
nombre_poissons = 30
nombre_requins = 10

def creation_monde(taille, nombre_poissons, nombre_requins):
    monde = [[0 for i in range(taille)] for y in range(taille)]
    random.seed(12) 

    for _ in range(nombre_poissons):
            row, col = randint(0, taille -1), randint(0, taille -1)
            if monde[row][col] == 0:
                monde[row][col] = 1

    
    for _ in range(nombre_requins):
            row, col = randint(0, taille -1), randint(0, taille -1)
            if monde[row][col] == 0:
                monde[row][col] = 2
    
    return monde 

monde_init = creation_monde(taille, nombre_poissons, nombre_requins)
random.seed(12) 
monde_ready = copy.deepcopy(monde_init)
    
for i in monde_ready:
      print(*i)

      
        




