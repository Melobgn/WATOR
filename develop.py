"""
Nouveau code : recommencer de zéro le 01/11/2023 pour comprendre l'ensemble du code et son fonctionnement 
Partie final effectué avec l'aide de Vincent pour la partie déplacement des créatures

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
        self.world_map = [[None for _ in range(width)] for _ in range(length)]
        # je crée la liste des coordonnées possibles que je j'aléatoirise
        self.coord_possible = [(x, y) for x in range(self.width) for y in range(self.length)]
        random.shuffle(self.coord_possible)
        # je crée une liste de liste de requins et une liste de poissons
        self.list_fishes = []
        self.list_sharks = []
        # pour donner à World l'accès aux composants de fish et shark
        self.my_fishes = Fishes(1, '\U0001f420')
        self.my_sharks = Sharks(2, '\U0001f988') 
        

    # je crée une fonction pour afficher le monde (=see_the_world)
    def see_world(self):
        for row in self.world_map:
            print(*row)

    """
    À CE STADE LE CODE AFFICHE UNE MATRICE DE 'icônes gouttes' AVEC UNE LARGEUR DE 10 ET UNE LONGUEUR DE 10
    """

# On peuple le monde
    def populate_world(self, nb_fishes, nb_sharks):
        self.nb_fishes = nb_fishes
        self.nb_sharks = nb_sharks
        
        for pos in self.coord_possible:
            self.world_map[pos[0]][pos[1]] = self.drops

        # ajouter les poissons
        for _ in range(self.nb_fishes):
            if not self.coord_possible:
                break
            x, y = self.coord_possible.pop()
            self.world_map[x][y] = self.my_fishes.return_icons_fish() # utiliser une fonction pour récupérer l'icône
            self.list_fishes.append((x, y))

        #  ajouter les requins
        for _ in range(self.nb_sharks):
            if not self.coord_possible:
                break
            x, y = self.coord_possible.pop()
            self.world_map[x][y] = self.my_sharks.icons_shark # accéder à l'icône directement (attribut public)
            self.list_sharks.append((x, y))

    """
    À CE STADE LE CODE AFFICHE UNE MATRICE DE 'gouttes' AVEC LES POISSONS ET LES REQUINS FIGÉS (icônes)
    """

# on crée une méthode pour récupérer les cases disponibles pour le déplacements futurs des poissons, ainsi que les requins plus tard
    def adjacentes_empty_cells(self, entity_pos_x, entity_pos_y):
        list_adjacentes_cells = [] # permet de lister les poissons pourront se déplacer : X(rangées ou lignes) = (0, 1) = bas et (0, -1) = haut, | Y(colonne) = (1, 0) = droite et (-1, 0) = à gauche
        list_travel_possible = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # pour chaque déplacement possible dans la liste des déplacements possibles
        for travel_possible in list_travel_possible: 
            # direction temporaire est = à la pos. X de l'entité + le déplacement possible (modulo), et la position Y de l'entité + le déplacement possible (modulo)
            temporary_direction = ((entity_pos_x + travel_possible[0]) % self.width, (entity_pos_y + travel_possible[1]) % self.length)
            #  SI la direction temporaire N'EST PAS DANS la liste des poissons (positions actuelles) et N'EST PAS DANS la liste des requins,  
            if temporary_direction not in self.list_fishes and temporary_direction not in self.list_sharks:
                # On ajoute la direction temporaire dans la listes des cellules adjacentes
                list_adjacentes_cells += [temporary_direction]

        direction = random.randint(0, len(list_adjacentes_cells) -1) # my_direction = la direction choisi aléatiorement pour un poisson précis

        # List Fishes: [(5, 7), (9, 2), (4, 7)]
        # Fish #1
        # Postion 5, 7 (x, y)
        # 1ere boucle
        #   [(5, 8), (6, 7), (5, 6), (4, 7)]
        # 2eme boucle
        #   if il y a (5, 8) dans List Fishes
        #   if il y a (6, 7) dans List Fishes
        #   if il y a (5, 6) dans List Fishes
        #   if il y a (4, 7) dans List Fishes

#  référence pour plus tard (déplacement REQUINS)
        # for dx, dy in travel_possible: # pour chaque direction (direction x et direction y) dans 'directions_possibles'
        #     self.new_x, self.new_y = (self.pos_x + dx) % self.width, (self.pos_y + dy) % self.length # nouvelle position x et nouvelle position y sont = à [position x actuelle + direction x] et [position y actuelle + direction y]
        #     if self.world_map[self.new_x][self.new_y] == self.drops: # SI la nouvelle position de x et la nouvelle position y est == icône 'gouttes'
        #         list_adjacentes_cells.append((dx, dy)) # => ajout des nouvelles position x et y la liste

        # return random.shuffle(self.list_adjacentes_cells) # génère une direction aléatoire
        return list_adjacentes_cells[direction]

    def move_creatures(self):
        for x, y in self.list_fishes:
            direction = self.adjacentes_empty_cells(x, y) # pour chaque poisson on récupère ses possibilités de déplacements
            new_pos_x = direction[0] # nouvelle position x récup précéd. en ligne 100
            new_pos_y = direction[1] # nouvelle position y récup précéd. en ligne 100
            self.world_map[x][y] = self.drops
            self.world_map[new_pos_x][new_pos_y] = self.my_fishes.icons_fish

#  TODO : Gérer la MàJ de list_fishes pour enlever le déplacement effectué et ajouter la nouvelle position du poisson
#  Ex. mon poisson été en 5.7 et il se déplace en 6.7 (visuellement ok, dans le code pas ok)
#  "en gros on a déménagé mais on a pas fait le changement d'adresse" 
# to do (tout collé) commentaire mis en avant
        


class Fishes(World):
    # création des poissons
    def __init__(self, type_id, icons_fish):
        self.type_id = type_id
        self.icons_fish = icons_fish

    # permet de récupérer l'icônes 'poisson'
    def return_icons_fish(self):
        return self.icons_fish
    
    def move_fishes(self):
        pass

#     def reproduct_fishes(self):
#         pass


class Sharks(Fishes):
    # Créations requins :
    def __init__(self, type_id, icons_shark):
        self.type_id = type_id
        self.icons_shark = icons_shark
        self.pos_shark = 0

    def return_icons_shark(self):
        return self.icons_shark
    
#     def move_sharks(self):
#         pass

#     def reproduct_sharks(self):
#         pass
    
# je donne des valeurs pour 'Monde.def _ _init_ _' et 'def see_world'
my_world = World(10, 10, '\U0001f4a7') # donc :  'def __init__(self, length=10, wiconsth=10):'
my_world.populate_world(10, 2)
my_world.see_world()


# N'arrive pas à afficher nombre de poissons et nombre de requins (à voir sur la fin)
# my_world(f"Nombre de poissons : {}")

# Gestion du temps :
chronons = 0
while chronons < 100:
    os.system('clear')

    # deplacement_requin.starvation()
    my_world.move_creatures()
    my_world.see_world()
    print(f"Nombre de tour(s) : {chronons}")
    print()
    chronons += 1
    time.sleep(0.8)