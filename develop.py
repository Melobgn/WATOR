import random

#     '''partie à Antoine '''
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

        poissons = []  # Liste pour stocker les poissons
        requins = []   # Liste pour stocker les requins

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

# Initialisation des valeurs
longueur = 10
largueur = 8
nombre_poissons = 10
nombre_requins = 5

# création de l'instance de la classe Planete
ma_planete = Planete(0, 0)

# initialisation du monde
ma_planete.creation_monde(longueur, largueur, nombre_poissons, nombre_requins)

# affichage du monde
ma_planete.affichage()




# 1 récupérer LES positions des requins et des poissons ---------------------------

# class Position(Planete):
#     def __init__(self,x ,y):
#         self.x = x
#         self.y = y

# position des poissons
class Poissons(Planete):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.tpos_ype = 1

# position des requins
class Requins(Planete):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.items = 2

# renvoyer les positions
class Coordonnées(Planete):
    def trouver_position(self, matrice, items):
        for i in range(len(matrice)):
            for j in range(len(matrice[0])):
                if matrice[i][j] == items:
                    yield i, j


# retourne la position des poissons et des requins 'x, y'
# définit la variable monde avant d'appeler la fonction trouver_position()
monde = ma_planete.creation_monde(longueur, largueur, nombre_poissons, nombre_requins)
poisson = Coordonnées().trouver_position(monde, 1)
for i, j in poisson:
    print(i, j)

requin = Coordonnées().trouver_position(monde, 2)
for i, j in requin:
    print(i, j)




# matrice d'essai Cécile
# monde = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 2, 1, 0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 2, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
# for row in monde:
#     print(*row)
'''partie à Antoine '''


# 2 créer une condition : si le requin se place sur un poisson (2 remplace 1)
    # le requin gagne 1 chronons (c.à.d. de l'énergie = 6 chronons au max)
    # le poisson meurt et disparait