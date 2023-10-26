from random import randint
import copy
import random

# Définir la taille de la map (10 = 10X10)
taille = 10

# Définir le nombre de poissons de départ
nombre_poissons = 23

# Définir le nombre de requins de départ
nombre_requins = 10

# fonction pour créer le monde de départ
def creation_monde(taille, nombre_poissons, nombre_requins):
    monde = [[0 for i in range(taille)] for y in range(taille)]
    random.seed(12) 

    # Place les poissons dans la grille
    for _ in range(nombre_poissons):
            row, col = randint(0, taille -1), randint(0, taille -1)
            if monde[row][col] == 0:
                monde[row][col] = 1

    # Place les requins dans la grille
    for _ in range(nombre_requins):
            row, col = randint(0, taille -1), randint(0, taille -1)
            if monde[row][col] == 0:
                monde[row][col] = 2
    
    return monde 

# Encapsule la map dans la variable monde
monde = creation_monde(taille, nombre_poissons, nombre_requins)

# Affiche la carte monde primaire
def affichage(monde):
    for i in monde:
        print(*i)

# déplace les poissons et les requins et créer le monde pour les verrous    
def deplacer_les_poissons_et_les_requins(monde):
     monde_bis = [[0 for i in range(taille)] for y in range(taille)]
     random.seed(12)

     return monde_bis
        
                 
        

affichage(monde)
print(deplacer_les_poissons_et_les_requins(monde))

