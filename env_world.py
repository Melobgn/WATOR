from random import randint
import copy
import random

# Définir la taille de la map (10 = 10X10)
taille = 10

# Définir le nombre de poissons de départ
nombre_poissons = 10

# Définir le nombre de requins de départ
nombre_requins = 5

# sauvergade des indices poissons et requins
poissons = []
requins = []


# fonction pour créer le monde de départ
def creation_monde(taille, nombre_poissons, nombre_requins):
    monde = [[0 for i in range(taille)] for y in range(taille)]
    random.seed(12) 

    # Place les poissons dans la grille
    for _ in range(nombre_poissons+1):
            row, col = randint(0, taille -1), randint(0, taille -1)
            if monde[row][col] == 0:
                monde[row][col] = 1
                poissons.append((row, col))

    # Place les requins dans la grille
    for _ in range(nombre_requins+1):
            row, col = randint(0, taille -1), randint(0, taille -1)
            if monde[row][col] == 0:
                monde[row][col] = 2
                requins.append((row, col))
    
    return monde



# Encapsule la map dans la variable monde
monde = creation_monde(taille, nombre_poissons, nombre_requins)

# Affiche la carte monde primaire
def affichage(monde):
    for i in monde:
        print(*i)

# Affiche la carte monde secondire
def affichage_bis(monde_bis):
     for i in monde_bis:
          print(*i)

# Le monde pour les verrous
monde_bis = [[0 for i in range(taille)] for y in range(taille)]
random.seed(12)


        
              
        
creation_monde(taille, nombre_poissons, nombre_requins)
affichage(monde)
print()
print(poissons)
print()
print(requins)


