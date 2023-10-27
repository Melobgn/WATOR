import random

# Initialisation des valeurs
longueur = 10
largueur = 8
nombre_poissons = 10
nombre_requins = 5

poissons = []  # Liste pour stocker les poissons
requins = []   # Liste pour stocker les requins

class Planete:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.monde = []  # Initialiser la variable "monde"
    
    # fonction pour créer le monde de départ
    def creation_monde(self, longueur, largueur, nombre_poissons, nombre_requins):
        self.longueur = longueur
        self.largueur = largueur
        self.nombre_poissons = nombre_poissons
        self.nombre_requins = nombre_requins
        monde = [[0 for i in range(largueur)] for y in range(longueur)]  # Créer une grille 2D pour le monde
        random.seed(12)
        coordonnees_possibles = [(x, y) for x in range(longueur) for y in range(largueur)]
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

        self.monde = monde  # Mets à jour la variable de la planète avec le monde créé
        
        return monde

    #affiche le monde
    def affichage(self):
        for i in self.monde:
            print(*i)

    #deplace les poissons
    def deplacer_poissons(self, dx, dy):
        self.pos_x += dx
        self.pos_y += dy


# création de l'instance de la classe Planete
ma_planete = Planete(0, 0)

# initialisation du monde
ma_planete.creation_monde(longueur, largueur, nombre_poissons, nombre_requins)

# affichage du monde
ma_planete.affichage()


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


