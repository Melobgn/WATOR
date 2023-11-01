"""
partie du Nouveau code du 01/11/2023
effectué totalement seule et sans GPT
Plutôt compris, reste encore beaucoup de chose à améliorer 
Blocage à partir des boucles for dans méthode populate_world (line 45 et 53)
 => suite dans develop.py

"""

import os
import time
import random


class World:
    def __init__(self, length, width, water_drop):
        # je donne une notion de longueur(=length) et une largeur(=width) au monde
        self.length = length
        self.width = width
        self.drops = water_drop
        # je crée une matrice vide de taille length * width
        self.world = [[self.drops for _ in range(width)] for _ in range(length)]
        # je crée une liste de liste de requins et une liste de poissons
        self.list_fishes = []
        self.list_sharks = []
        

    # je crée une fonction pour afficher le monde (=see the world) :
    def see_world(self):
        for row in self.world:
            print(*row)

    """
    À CE STADE LE CODE AFFICHE UNE MATRICE DE '0' AVEC UNE LARGEUR DE 10 ET UNE LONGUEUR DE 10
    """

# Puis on peuple le monde
    def populate_world(self, nb_fishes, nb_sharks):
        self.nb_fishes = nb_fishes
        self.nb_sharks = nb_sharks
        # CORRECTION : Pas placé au bon endroit (⇡) .voir:newcode
        self.coord_possible = [(x, y) for x in range(self.width) for y in range(self.length)]
        random.shuffle(self.coord_possible)

        # ajouter les poissons
        for _ in range(self.nb_fishes):
            if not self.coord_possible:
                break
            x, y = self.coord_possible.pop()
            self.world[x][y] = Fishes.__init__
            self.list_fishes.append((x, y))

        #  ajouter les requins
        for _ in range(self.nb_sharks):
            if not self.coord_possible:
                break
            x, y = self.coord_possible.pop()
            self.world[x][y] = Fishes.__init__
            self.list_sharks.append((x, y))

#  CORRECTION : les deux identités déplacés dans leur classes respectives
class Fishes(World):
    # Création des poissons
    def __init__(self, type_id, icons):
        self.type_id = type_id
        self.icons = icons
        self.pos_fish = self.coord_possible

# REQUINS
class Sharks(World):
    # Créations requins :
    def __init__(self, type_id, icons):
        self.type_id = type_id
        self.icons = icons
        self.pos_shark = self.coord_possible


# je donne des valeurs pour 'Monde.def _ _init_ _' et 'def see_world'
my_world = World(10, 10, '\U0001f4a7') # donc :  'def __init__(self, length=10, wiconsth=10):'
my_world.see_world()
my_world.populate_world(10, 2)

#  CORRECTION : déplacement dans la Word > 'init'
my_fishes = Fishes(1, '\U0001f41f')
my_sharks = Sharks(2, '\U0001f988') 

# N'arrive pas à afficher nombre de poissons et nombre de requins (à voir sur la fin)
# my_world(f"Nombre de poissons : {}")

# Gestion du temps :
chronons = 0
while chronons < 100:
    os.system('clear')

    # deplacement_requin.starvation()
    my_world.see_world()
    print(f"Nombre de tour(s) : {chronons}")
    print()
    chronons += 1
    time.sleep(0.8)





#  structure classe mise de côté pour plus tard 


#     def adjacentes_cells(self, monde):
#         pass
#         # # ADJACENTE : qui se trouve dans le voisinage immédiat !!!
#         # cases_adjacentes = []
#         # # permet d'indiquer comment les poissons se déplacent : X(rangées ou lignes) = (0, 1) = bas, (0, -1) = haut, | Y(colonne) = (1, 0) = droite, (-1, 0) = à gauche
#         # deplacement_possible = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#         # # directions_possibles = deplacement_possible[:]
#         # # condition
#         # # random.shuffle(directions_possibles) # line 48 et 49 génère une direction aléatoire : (0, 1) ou (1, 0) ou (0, -1) ou (-1, 0)

#         # for dx, dy in deplacement_possible: # pour chaque direction (direction x et direction y) dans 'directions_possibles'
#         #     new_x, new_y = (self.x + dx) % self.largeur, (self.y + dy) % self.longueur # nouvelle position x et nouvelle position y sont = à [position x actuelle + direction x] et [position y actuelle + direction y]
#         #     if self.monde.monde[new_x][new_y] == '\U0001f4a7': # '== eau'
#         #         cases_adjacentes.append((dx, dy))

#         # return cases_adjacentes

#     def move_fishes(self):
#         pass

#     def reproduct_fishes(self):
#         pass