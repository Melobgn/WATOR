"""
Ce qui fonctionne : Mon code affiche la matrice de gouttes d'eau avec 10 poissons et 2 requins, 
                    le compteur fonctionne

Ce qui ne fonctionne pas : Les poissons et les requins ne se déplacent pas*

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

    # je crée une fonction pour afficher le monde (=see_the_world)
    def see_world(self):
        for row in self.world_map:
            print(*row)
        # ajout d'un compteur de poissons et de requins
        print(f"Poissons : {len(self.list_fishes)}")
        print(f"Requins : {len(self.list_sharks)}")

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
            fish = Fish(1, '\U0001f420', x, y, self)
            self.world_map[x][y] = fish.icons_fish # utiliser une fonction pour récupérer l'icône
            self.list_fishes.append(fish)

        #  ajouter les requins
        for _ in range(self.nb_sharks):
            if not self.coord_possible:
                break
            x, y = self.coord_possible.pop()
            shark = Sharks(2, '\U0001f988', x, y, self)
            self.world_map[x][y] = shark.icons_shark # accéder à l'icône directement (attribut public)
            self.list_sharks.append(shark)

    """
    À CE STADE LE CODE AFFICHE UNE MATRICE DE 'gouttes' AVEC LES POISSONS ET LES REQUINS FIGÉS (icônes)
    """
     
    def play_a_round(self):
        for fish in self.list_fishes: # pour chaque 'poisson' dans la liste poisson
            fish.move_fishes(fish.x, fish.y) 
        for shark in self.list_sharks:
            shark.move_sharks(shark.x, shark.y) 

# TODO : Consignes Jérémy
# faire une boucle sur les poissons et sur les requins qui sont dans les listes 
# appliquer la méthode pour les faire se déplacer
    # /!\ convention! = attention ne pas mettre le nom de l'objet dans la methode

class Fish:
    def __init__(self, type_id, icons_fish, x, y, world):
        self.x = x
        self.y = y
        self.world = world
        self.type_id = type_id
        self.icons_fish = icons_fish

    
# on crée une méthode pour récupérer les cases disponibles pour le déplacement futur des poissons (ainsi que les requins plus tard)
# MEMO : X(rangées ou lignes) = (0, 1) = bas et (0, -1) = haut, | Y(colonne) = (1, 0) = droite et (-1, 0) = à gauche
    def adjacent_empty_cells(self, entity_pos_x, entity_pos_y): 
        list_adjacent_cells = [] # liste les positions adjacentes vides sur lesquels les créatures pourront se déplacer
        list_travel_possible = [(0, 1), (1, 0), (0, -1), (-1, 0)] 
        
        for travel_possible in list_travel_possible: 
            temporary_direction = ((entity_pos_x + travel_possible[0]) % self.world.width, (entity_pos_y + travel_possible[1]) % self.world.length) 
            if temporary_direction not in self.world.list_fishes and temporary_direction not in self.world.list_sharks:
                list_adjacent_cells.append(temporary_direction)

        """ 
        List Fishes: [(5, 7), (9, 2), (4, 7)]
        MEMO de 'def adjacent_empty_cells()' :
        Fish #1
        Postion 5, 7 (x, y)
        1ere boucle va donner des directions possibles
          [(5, 8), (6, 7), (5, 6), (4, 7)] --> list_adjacent_cells
        condition va vérifier ..
          if il y a (5, 8) dans List Fishes
          if il y a (6, 7) dans List Fishes
          if il y a (5, 6) dans List Fishes
          if il y a (4, 7) dans List Fishes
          
        """

        direction = random.randint(0, len(list_adjacent_cells) -1) 
        return list_adjacent_cells[direction] 
    
    def move_fishes(self, x, y): 
        # on récupère dans 'direction' ses possibilités de déplacement
        direction = self.adjacent_empty_cells(x, y) 
        
        new_pos_x = x + direction[0] 
        new_pos_y = y + direction[1] 
        if new_pos_x == self.world.drops and new_pos_y == self.world.drops: 
            new_pos_x, new_pos_y = self.icons_fish 
            x, y = self.world.drops    

                


#     def reproduct_fishes(self):
#         pass



class Sharks(Fish):
    def __init__(self, type_id, icons_shark, x, y, world):
        self.x = x
        self.y = y
        self.world = world
        self.type_id = type_id
        self.icons_shark = icons_shark

    def move_sharks(self, x, y):
        # on récupère dans 'direction' ses possibilités de déplacement
        direction = self.adjacent_empty_cells(x, y) 
        new_pos_x = x + direction[0] 
        new_pos_y = y + direction[1]
        if new_pos_x == self.world.drops and new_pos_y == self.world.drops: # si la nouvelle position x et y est une goutte d'eau
            new_pos_x, new_pos_y = self.icons_shark # alors on remplace la goutte par un icône poisson
            x, y = self.world.drops # et on remplace l'ancienne position par un icône   

    #  Pour plus tard (déplacement REQUINS)
        # for dx, dy in travel_possible: # pour chaque direction (direction x et direction y) dans 'directions_possibles'
        #     self.new_x, self.new_y = (self.pos_x + dx) % self.width, (self.pos_y + dy) % self.length # nouvelle position x et nouvelle position y sont = à [position x actuelle + direction x] et [position y actuelle + direction y]
        #     if self.world_map[self.new_x][self.new_y] == self.drops: # SI la nouvelle position de x et la nouvelle position y est == icône 'gouttes'
        #         list_adjacent_cells.append((dx, dy)) # => ajout des nouvelles position x et y la liste

        # return random.shuffle(self.list_adjacent_cells) # génère une direction aléatoire


#     def reproduct_sharks(self):
#         pass
    
# je donne des valeurs pour 'Monde.def _ _init_ _' et 'def see_world'
my_world = World(10, 10, '\U0001f4a7') # donc :  'def __init__(self, length=10, width=10):'
my_world.populate_world(10, 2)
my_world.see_world()

# Gestion du temps :
chronons = 0
while chronons < 100:
    os.system('clear')
    my_world.play_a_round()
    my_world.see_world()
    print(f"Nombre de tour(s) : {chronons}")
    print()
    chronons += 1
    time.sleep(0.8)