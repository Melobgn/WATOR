# fonction pour créer le monde de départ
import random

# Définir la taille de la map (10 = 10X10)
taille = 10

# Définir le nombre de poissons de départ
nombre_poissons = 23

# Définir le nombre de requins de départ
nombre_requins = 10

poissons = []
requins = []

# fonction pour créer le monde de départ
def creation_monde(taille, nombre_poissons, nombre_requins):
    monde = [[0 for i in range(taille)] for y in range(taille)]
    random.seed(12) 

    coordonnees_possibles = [(x, y) for x in range(taille) for y in range(taille)]
    random.shuffle(coordonnees_possibles)



    # Place les poissons dans la grille
    for poisson in range(nombre_poissons):
        if not coordonnees_possibles:
            break  # Si on a utilisé toutes les coordonnées possibles, sortir de la boucle
        row, col = coordonnees_possibles.pop()
        monde[row][col] = 1
        poissons.append({'row': row, 'col': col})

    # Place les requins dans la grille
    for requin in range(nombre_requins):
        if not coordonnees_possibles:
            break  # Si on a utilisé toutes les coordonnées possibles, sortir de la boucle
        row, col = coordonnees_possibles.pop()
        monde[row][col] = 2
        requins.append({'row': row, 'col': col})
    
    return monde

resultat = creation_monde(taille, nombre_poissons, nombre_requins)

# Afficher les coordonnées des poissons
for poisson in poissons:
    print(f"Coordonnées du poisson : ({poisson['row']}, {poisson['col']})")

    # Afficher les coordonnées des requins
for requin in requins:
    print(f"Coordonnées du requin : ({requin['row']}, {requin['col']})")


print(poissons)
print(requins)

# def deplacer_les_poissons_et_les_requins(monde):
#     monde_bis = [[0 for i in range(taille)] for y in range(taille)]
#     random.seed(12)
    
#     for i in range(len(monde)):  # Parcours des indices de ligne
#         for j in range(len(monde[0])):  # Parcours des indices de colonne
#             if monde[i][j]:
#                 deplacement_possible = [(0, 1), (1, 0), (0, -1), (-1, 0)] 
#                 direction = random.choice() # déplacement en random des déplacement possible
#                 x, y = (i + direction[0]) % taille, (j + direction[1]) % taille
#                 monde_bis[x][y] = 1 # Permet de gérer la spécificité du torus
#             else:
#                 monde_bis[i][j] = monde[i][j]
    
#     return monde_bis


