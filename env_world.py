from random import randint
import copy
import random


taille = 10
nombre_poissons = 23
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

monde = creation_monde(taille, nombre_poissons, nombre_requins)


def affichage(monde):
    for i in monde:
        print(*i)

def deplacer_les_poissons_et_les_requins(monde):
     monde_bis = [[0 for i in range(taille)] for y in range(taille)]
     random.seed(12)

     return monde_bis
        
                 
        

affichage(monde)
print(deplacer_les_poissons_et_les_requins(monde))

