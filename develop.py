import os
import time
import random
import pygame
import matplotlib.pyplot as plt




class World:
    def __init__(self, length, width ):
        # je donne une notion de longueur(=length) et une largeur(=width) au monde
        self.length = length
        self.width = width
        self.water_drop = 0
        # je crée une matrice vide de taille length * width
        self.world_map = [[self.water_drop for _ in range(width)] for _ in range(length)]
        
        # je crée une liste de liste de requins et une liste de poissons
        self.list_fishes = []
        self.list_sharks = []

     # je crée une fonction pour afficher le monde (=see_the_world)
    def see_world(self):
        for row in self.world_map:
            print(*row)
        print(f"Poissons : {len(self.list_fishes)}")
        print(f"Requins : {len(self.list_sharks)}")


    # On peuple le monde
    def populate(self, nb_fishes, nb_sharks):
        
        # je crée la liste des coordonnées possibles que je j'aléatoirise
        coord_possible = [(x, y) for x in range(self.width) for y in range(self.length)]
        random.shuffle(coord_possible)
        
       

        # ajouter les poissons
        for _ in range(self.nb_fishes):
            if not coord_possible:
                break
            x, y = coord_possible.pop()
            fish = Fish(self, x, y)
            self.world_map[x][y] = fish.icons_fish # utiliser une fonction pour récupérer l'icône
            self.list_fishes.append(fish)

        #  ajouter les requins
        for _ in range(self.nb_sharks):
            if not coord_possible:
                break
            x, y = coord_possible.pop()
            shark = Shark(self, x, y)
            self.world_map[x][y] = shark.icons_shark # accéder à l'icône directement (attribut public)
            self.list_sharks.append(shark)

    """
    À CE STADE LE CODE AFFICHE UNE MATRICE DE 'gouttes' AVEC LES POISSONS ET LES REQUINS FIGÉS (icônes)
    """
     # a mettre dans la classe simulation
    def play_a_round(self):
        for fish in self.list_fishes: # pour chaque 'poisson' dans la liste poisson
            fish.move_prey() 
        for shark in self.list_sharks:
            shark.starvation()
            shark.move_carnivore()
            shark.eat_prey()
        for fish in self.list_fishes:
            self.world_map[fish.x][fish.y] = fish.icons_fish 
        for shark in self.list_sharks:
            self.world_map[shark.x][shark.y] = shark.icons_shark 
        
             

# TODO : Consignes Jérémy
# 1. faire une boucle sur les poissons et sur les requins qui sont dans les listes
# 2. appliquer la méthode pour les faire se déplacer => Pas dans cette méthodes mais dans move_fish et sharks !!
    # /!\ convention! = attention ne pas mettre le nom de l'objet dans la methode

    #  TODO remarque : il ne fallait rien mettre entre les parenthèses de fish.move_prey() et fish.move_prey(), pourquoi ? je ne sais pas !



class Fish:
    def __init__(self, world, x, y ):
        self.world = world
        self.x = x
        self.y = y
        self.type_id = 1
        self.icons_fish = '\U0001f420'
        self.gestation = 0
        self.gestation_time = 8

    
# on crée une méthode pour récupérer les cases disponibles pour le déplacement futur des poissons (ainsi que les requins plus tard)
# MEMO : X(rangées ou lignes) = (0, 1) = bas et (0, -1) = haut, | Y(colonne) = (1, 0) = droite et (-1, 0) = à gauche

    def adjacent_empty_cells(self):
        adjacentes_empty_cells = []
        list_travel_possible = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dx, dy in list_travel_possible: # pour chaque direction (direction x et direction y) dans 'directions_possibles'
            new_x, new_y = (self.x + dx) % self.world.width, (self.y + dy) % self.world.length
            # SI 0 est plus petit que largeur et que 0 est plus petit que longueur et que la nouvelle position x et y est un goutte d'eau :
            if self.world.world_map[new_x][new_y] == 0:
                adjacentes_empty_cells.append((new_x, new_y)) # alors la nouvelle position x et y est apporter dans la liste des cases adjacentes vides

        return adjacentes_empty_cells # et on retourne cette liste

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
    
    def move_prey(self):
        # T'avais grave raison Melo (she is the best) !!!! :) Random.choice !!
        empty_cells = self.adjacent_empty_cells()
        if not empty_cells:
            self.gestation += 1
            return
        else:
            direction = random.choice(self.adjacent_empty_cells()) # je choisi un élément au hasard dans la liste (élément = cases adjacentes vides dispo)
            dx, dy = direction 
            new_x = (self.x + dx) % self.world.length
            new_y = (self.y + dy) % self.world.width
            if self.gestation >= self.gestation_time:
                self.reproduct_prey()
                self.gestation = 0
            else:
                self.world.world_map[new_x][new_y] = self.icons_fish
                self.world.world_map[self.x][self.y] = self.world.water_drop
                self.x, self.y = new_x, new_y
                self.gestation += 1

    def reproduct_prey(self):
        baby_fish = Fish(self.world, self.x, self.y)
        self.world.list_fishes.append(baby_fish)
        self.world.world_map[self.x][self.y] = self.world.water_drop
        


class Shark(Fish):
    def __init__(self,world, x, y ):
        self.x = x
        self.y = y
        self.world = world
        self.type_id = 2
        self.icons_shark = '\U0001f988'
        self.energy = 10
        self.gestation = 0
        self.gestation_time = 40


    def move_carnivore(self):
        # for empty_cells in self.adjacent_empty_cells():
        empty_cells = self.adjacent_empty_cells()
        if not empty_cells:
            self.gestation += 1
            return
        else:
            self.following_prey()
        if not self.following_prey():
            if empty_cells:
                direction = random.choice(self.adjacent_empty_cells()) # je choisi un élément au hasard dans la liste (élément = cases adjacentes vides dispo)
                dx, dy = direction
                new_x = (self.x + dx) % self.world.length
                new_y = (self.y + dy) % self.world.width
                if self.gestation >= self.gestation_time:
                    self.reproduct_sharks()
                    self.gestation = 0
                else:
                    self.world.world_map[new_x][new_y] = self.icons_shark
                    self.world.world_map[self.x][self.y] = self.world.water_drop
                    self.x, self.y = new_x, new_y
                    self.gestation += 1

    def following_prey(self):
        fish_nearby = None
        for fish in self.world.list_fishes:
            if abs(self.x - fish.x) <= 1 and abs(self.y - fish.y) <= 1:
                fish_nearby = fish
        if fish_nearby:
            # Si un poisson est proche, se déplacer vers lui
            if self.x < fish_nearby.x:
                new_x, new_y = self.x + 1, self.y
            elif self.x > fish_nearby.x:
                new_x, new_y = self.x - 1, self.y
            elif self.y < fish_nearby.y:
                new_x, new_y = self.x, self.y + 1
            else:
                new_x, new_y = self.x, self.y - 1
            if self.gestation >= self.gestation_time:
                self.reproduct_sharks()
                self.gestation = 0
            else:
                self.world.world_map[self.x][self.y] = 0
                self.world.world_map[new_x][new_y] = '\U0001f988'
                self.x, self.y = new_x, new_y
                self.gestation += 1

    def reproduct_sharks(self):
        baby_shark = Shark(self.world, self.x, self.y)
        self.world.list_sharks.append(baby_shark)
        self.world.world_map[self.x][self.y] = self.world.water_drop
    
    def starvation(self):
        if self.energy <= 0:
            self.world.world_map[self.x][self.y] = 0
            self.world.list_sharks.remove(self)
        else:
            self.energy -= 1

    def eat_prey(self):
        for fish in self.world.list_fishes:
            if (abs(self.x - fish.x) <= 1 and abs(self.y - fish.y) == 0) or (abs(self.x - fish.x) == 0 and abs(self.y - fish.y) <= 1):
                self.world.world_map[fish.x][fish.y] = 0
                self.energy += 2
                self.world.list_fishes.remove(fish)



class Simulation:
    def __init__(self, length, width, fish, shark, delay_chronon, cell_size):
        self.world = World(length,width)
        self.chronons = 0
        self.delay_chronon = delay_chronon
        self.on= True
        self.fish = fish
        self.shark= shark
        self.cell_size = cell_size  # Nouvel attribut pour la taille des cellules

        # Initialisation des données pour le graphique
        self.time = [0]
        self.list_fishes_data = [self.fish]
        self.list_sharks_data = [self.shark]

    def initialisation(self):
        # Initialisation de Pygame
        pygame.init()
        width = self.world.width * self.cell_size  # Calcul de la taille de l'écran en fonction des cellules
        length = self.world.length * self.cell_size # Calcul de la taille de l'écran en fonction des cellules
        screen = pygame.display.set_mode((width, length + 80))
        pygame.display.set_caption("Projet Wa_tor")

        # Chargement des images
        fish_picture = pygame.image.load("fish.png").convert_alpha()
        shark_picture= pygame.image.load("shark.png").convert_alpha()

        # Redimensionnement des images en fonction de la taille de la cellule
        fish_picture = pygame.transform.scale(fish_picture, (self.cell_size, self.cell_size))
        shark_picture = pygame.transform.scale(shark_picture, (self.cell_size, self.cell_size))
        color_background = (0, 127, 255)
        self.world.populate(self.list_fishes, self.list_sharks)

        running = True
        font = pygame.font.Font(None, 25)

        # Initialisation du graphique
        plt.ion()
        fig, ax = plt.subplots()
        ax.set_title("Evolution of fish and shark numbers")
        ax.set_xlabel("Time")
        ax.set_ylabel("Number")

        fishes_line, = ax.plot(self.time, self.list_fishes_data, label="Fishes")
        sharks_line, = ax.plot(self.time, self.list_sharks_data, label="Sharkes")

        ax.legend(loc="upper left")

        plt.show()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.ending_simulation()
            screen.fill((255, 255, 255))

            # Appel des méthodes de déplacement et d'interaction des poissons et requins
            for fish in self.world.list_fishes:
                fish.move_prey()
            for shark in self.world.list_sharks:
                shark.move_carnivore()
                shark.starvation()
                shark.eat_prey()
            for fish in self.world.list_fishes:
                self.world.world_map[fish.x][fish.y] = '\U0001f41f' #poisson
            for shark in self.world.nb_sharks:
                self.world.world_map[shark.x][shark.y] = '\U0001f988' #requin

            # Dessin des cellules
            for i in range(self.world.length):
                for j in range(self.world.width):
                    cell = self.world.world_map[i][j]
                    x = j * self.cell_size
                    y = i * self.cell_size
                    pygame.draw.rect(screen, color_background, (x, y, self.cell_size ,self.cell_size))
                    if cell == '\U0001f41f':
                        screen.blit(fish_picture, (x, y))
                    elif cell == '\U0001f988':
                        screen.blit(shark_picture, (x, y))

            # Affichage des informations
            text_chronons = font.render(f"Chronons: {self.chronons}", True, (0, 0, 0))
            shark_txt = font.render(f"Sharks: {len(self.world.list_sharks)}", True, (0, 0, 0))
            fish_txt= font.render(f"Fishes: {len(self.world.list_fishes)}", True, (0, 0, 0))
            screen.blit(text_chronons, (10, length + 10))
            screen.blit(shark_txt, (10, length + 40))
            screen.blit(fish_txt (10, length + 60))
            pygame.display.flip()
            self.chronons += 1
            pygame.time.delay(self.delay_chronon)

            # Mise à jour des données du graphique
            self.temps.append(self.chronons)
            self.list_fishes_data.append(len(self.world.list_fishes))
            self.list_sharks_data.append(len(self.world.list_sharks))

            # Mise à jour du graphique en temps réel
            fishes_line.set_data(self.time, self.list_fishes_data)
            sharks_line.set_data(self.time, self.list_sharks_data)

            ax.relim()
            ax.autoscale_view()

            plt.pause(0.01)
            plt.draw()

            pygame.display.flip()
            self.chronons += 1
            pygame.time.delay(self.delay_chronon)

    def manage_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.ending_simulation()

    def update(self):
        self.move_prey()
        self.shark.starvation()
        self.move_carnivore()
        self.shark.eat_prey()
        self.chronons += 1
        pygame.time.delay(self.delay_chronon)

    def display(self):
        pass

    def on(self):
        return self.on

    def ending_simulation(self):
        self.on= False
        pygame.quit()


   