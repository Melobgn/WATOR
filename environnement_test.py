import random

# Initialisation des valeurs
longueur = 10
largeur = 8
nombre_poissons = 10
nombre_requins = 5

poissons = []  # Liste pour stocker les poissons
requins = []   # Liste pour stocker les requins

class Planete:
    def __init__(self, longueur, largeur, nombre_poissons, nombre_requins):
        self.longueur = longueur
        self.largeur = largeur
        self.nombre_poissons = nombre_poissons
        self.nombre_requins = nombre_requins
        self.monde = []
        self.poissons = []
        self.requins = []
        

        # random.seed(12)
    
    def coord(self):
        coordonnees_possibles = [(x, y) for x in range(longueur) for y in range(largeur)]
        monde = [[0 for i in range(largeur)] for y in range(longueur)]  # Créer une grille 2D pour le monde
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



    #déplace les poissons
    def deplacer_poissons(self):
        deplacement_possible = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
        for poisson in self.poissons:
            direction = random.choice(deplacement_possible)
            new_row = poisson['row'] + direction[0]
            new_col = poisson['col'] + direction[1]

            if 0 <= new_row < self.longueur and 0 <= new_col < self.largeur:
                 self.monde[poisson['row']][poisson['col']] = 0
                 self.monde[new_row[new_col]] = 1
                 poisson['row'] = new_row
                 poisson['col'] = new_col


ma_planete = Planete(10, 10, 10, 5)
ma_planete.affichage()
ma_planete.coord()
print()
ma_planete.deplacer_poissons()
#Afficher la planète après déplacement
ma_planete.affichage()

# initialisation du monde

# affichage du monde
# for poisson in poissons:
#         print(f"Coordonnées du poisson : ({poisson['row']}, {poisson['col']})")

#     # Afficher les coordonnées des requins
# for requin in requins:
#         print(f"Coordonnées du requin : ({requin['row']}, {requin['col']})")




# création de l'instance de la classe Planete



# Afficher les coordonnées des poissons





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


