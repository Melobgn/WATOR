import os
import time
import random
import pygame
import matplotlib.pyplot as plt

class World:
    def __init__(self, length, height):
        """
        Initialise le monde.

        Args:
            length (int): Longueur du monde.
            height (int): Hauteur du monde.
        """
        self.length = length
        self.height = height
        self.water_drop = 0
        self.world_map = [[self.water_drop for _ in range(length)] for _ in range(height)]
        self.list_fishes = []
        self.list_sharks = []
        self.available_cells = set([(x, y) for x in range(length) for y in range(height)])  # Suivre les cellules disponibles


    def see_world(self):
        """
        Affiche l'état du monde avec le nombre de poissons et de requins.
        """
        for row in self.world_map:
            print(*row)
        print(f"Poissons : {len(self.list_fishes)}")
        print(f"Requins : {len(self.list_sharks)}")


    def populate(self, nb_fishes, nb_sharks):
        """
        Peuple le monde avec un certain nombre de poissons et de requins.

        Args:
            nb_fishes (int): Nombre de poissons à peupler.
            nb_sharks (int): Nombre de requins à peupler.
        """
        coord_possible = list(self.available_cells)
        random.shuffle(coord_possible)

        for _ in range(nb_fishes):  # Utiliser nb_fishes au lieu de self.nb_fishes
            if not coord_possible:
                break
            x, y = coord_possible.pop()
            fish = Fish(self, x, y)
            self.world_map[x][y] = fish.icons_fish
            self.list_fishes.append(fish)

        for _ in range(nb_sharks):  # Utiliser nb_sharks au lieu de self.nb_sharks
            if not coord_possible:
                break
            x, y = coord_possible.pop()
            shark = Shark(self, x, y)
            self.world_map[x][y] = shark.icons_shark
            self.list_sharks.append(shark)


    def play_a_round(self):
        for fish in self.list_fishes:
            fish.move_prey()
        for shark in self.list_sharks:
            shark.starvation()
            shark.move_carnivore()
            shark.eat_prey()
            shark.cannibalism()

        for fish in self.list_fishes:
            self.world_map[fish.x][fish.y] = fish.icons_fish
        for shark in self.list_sharks:
            self.world_map[shark.x][shark.y] = shark.icons_shark




class Fish:
    def __init__(self, world, x, y):
        """
        Initialise un poisson dans le monde.

        Args:
            world (World): Le monde dans lequel le poisson existe.
            x (int): Coordonnée x du poisson.
            y (int): Coordonnée y du poisson.
        """
        self.world = world
        self.x = x
        self.y = y
        self.icons_fish = '\U0001f420'
        self.gestation = 0
        self.gestation_time = 22
        

    def adjacent_empty_cells(self):
        """
        Recherche les cellules vides adjacentes à ce poisson.

        Returns:
            list de tuples: Liste des coordonnées (dx, dy) des cellules vides adjacentes.
        """
        list_travel_possible = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        random.shuffle(list_travel_possible)
        empty_cells = []

        for dx, dy in list_travel_possible:
            new_x, new_y = self.x + dx, self.y + dy
            if 0 <= new_x < self.world.length and 0 <= new_y < self.world.height and self.world.world_map[new_x][new_y] == 0:
                empty_cells.append((dx, dy))

        if empty_cells:
            return empty_cells
        return None

        

    def move_prey(self):
        """
        Déplace le poisson dans le monde, gère la reproduction et la gestation.
        """
        empty_cells = self.adjacent_empty_cells()
        if not empty_cells:
            self.gestation += 1
            return

        dx, dy = random.choice(empty_cells)
        new_x, new_y = self.x + dx, self.y + dy

        if self.gestation >= self.gestation_time:
            self.reproduct_prey()
            self.gestation = 0
        else:
            self.world.world_map[new_x][new_y] = self.icons_fish
            self.world.world_map[self.x][self.y] = self.world.water_drop
            self.x, self.y = new_x, new_y
            self.gestation += 1


    def reproduct_prey(self):
        """
        Fait se reproduire un poisson, créant un nouveau poisson à une cellule vide aléatoire.
        """
        baby_x, baby_y = random.choice(list(self.world.available_cells))
        if (baby_x, baby_y) in self.world.available_cells:
            baby_fish = Fish(self.world, baby_x, baby_y)
            self.world.list_fishes.append(baby_fish)
            self.world.world_map[baby_x][baby_y] = self.icons_fish
            self.world.available_cells.remove((baby_x, baby_y))
            self.world.available_cells.add((self.x, self.y))



class Shark(Fish):
    def __init__(self, world, x, y):
        """
        Initialise un requin dans le monde.

        Args:
            world (World): Le monde dans lequel le requin existe.
            x (int): Coordonnée x du requin.
            y (int): Coordonnée y du requin.
        """
        super().__init__(world, x, y)
        self.icons_shark = '\U0001f988'
        self.energy = 8
        self.gestation_time = 35
        self.cannibal = False



    def move_carnivore(self):
        """
        Gère le déplacement du requin dans le monde.

        - Le requin se déplace vers une cellule vide aléatoire s'il n'y a pas de proie à proximité.
        - Gère la reproduction du requin.

        """
        empty_cells = self.adjacent_empty_cells()
        if not empty_cells:
            self.gestation += 1
            return
        else:
            if not self.following_prey():
                
                dx, dy = random.choice(empty_cells)
                new_x = (self.x + dx) % self.world.length
                new_y = (self.y + dy) % self.world.height
                if self.gestation >= self.gestation_time:
                    self.reproduct_sharks()
                    self.gestation = 0
                else:
                    self.world.world_map[new_x][new_y] = self.icons_shark
                    self.world.world_map[self.x][self.y] = self.world.water_drop
                    self.x, self.y = new_x, new_y
        self.gestation += 1


    def following_prey(self):
        """
        Vérifie si une proie est à proximité et la suit s'il y en a une.

        Returns:
            bool: True si une proie est suivie, False sinon.
        """
        fish_nearby = None
        for fish in self.world.list_fishes:
            if abs(self.x - fish.x) <= 1 and abs(self.y - fish.y) <= 1:
                fish_nearby = fish
        if fish_nearby:
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
                self.world.world_map[new_x][new_y] = self.icons_shark
                self.x, self.y = new_x, new_y
                self.gestation += 1
    
    

    def reproduct_sharks(self):
        """
        Gère la reproduction des requins en créant un nouveau requin dans une cellule vide aléatoire.
        """
        baby_x, baby_y = random.choice(list(self.world.available_cells))
        if (baby_x, baby_y) in self.world.available_cells:
            baby_shark = Shark(self.world, baby_x, baby_y)
            self.world.list_sharks.append(baby_shark)
            self.world.world_map[baby_x][baby_y] = self.icons_shark
            self.world.available_cells.remove((baby_x, baby_y))
            self.world.available_cells.add((self.x, self.y))



    def starvation(self):
        """
        Gère la faim du requin et le supprime du monde s'il n'a plus d'énergie.
        """
        if self.energy <= 0:
            self.world.world_map[self.x][self.y] = 0
            self.world.list_sharks.remove(self)
        else:
            self.energy -= 1


    def eat_prey(self):
        """
        Gère le fait que le requin mange une proie s'il y en a une à proximité.
        """
        for fish in self.world.list_fishes:
            if (abs(self.x - fish.x) <= 1 and abs(self.y - fish.y) == 0) or (abs(self.x - fish.x) == 0 and abs(self.y - fish.y) <= 1):
                self.world.world_map[fish.x][fish.y] = 0
                self.energy += 3
                self.world.list_fishes.remove(fish)

    
    def cannibalism(self):
        """
        Gère le cannibalisme du requin, le fait de manger un autre requin à proximité s'il a faim.
        """
        if self.energy < 5:
            for shark in self.world.list_sharks:
                if (abs(self.x - shark.x) <= 1 and abs(self.y - shark.y) == 0) or (abs(self.x - shark.x) == 0 and abs(self.y - shark.y) <= 1):
                    self.world.world_map[shark.x][shark.y] = 0
                    self.energy += 3
                    self.world.list_sharks.remove(shark)
                    


class Simulation:
    def __init__(self, world,  nb_fishes, nb_sharks, delay_chronon, cell_size):
        """
        Initialise la simulation.

        Args:
            world (World): Le monde dans lequel se déroule la simulation.
            nb_fishes (int): Nombre de poissons initiaux.
            nb_sharks (int): Nombre de requins initiaux.
            delay_chronon (int): Délai entre les chronons.
            cell_size (int): Taille de la cellule pour l'affichage graphique.
        """
        self.world = world
        self.delay_chronon = delay_chronon
        self.chronons = 0
        self.on = True
        self.list_fishes = nb_fishes
        self.list_sharks = nb_sharks
        self.cell_size = cell_size

        self.time = [0]
        self.list_fishes_data = [nb_fishes]
        self.list_sharks_data = [nb_sharks]

    def update(self):
        """
        Met à jour l'état du monde en faisant avancer d'un chronon la simulation.
        """
        for fish in self.world.list_fishes:
            fish.move_prey()
        for shark in self.world.list_sharks:
            shark.move_carnivore()
            shark.cannibalism()
            shark.starvation()
            shark.eat_prey()
            shark.cannibalism()

        for fish in self.world.list_fishes:
            self.world.world_map[fish.x][fish.y] = '\U0001f41f'

        for shark in self.world.list_sharks:
            self.world.world_map[shark.x][shark.y] = '\U0001f988'

        self.chronons += 1

    def draw(self, screen, font, fish_picture, shark_picture):
        """
        Dessine l'état du monde dans la fenêtre graphique de la simulation.

        Args:
            screen: Fenêtre de la simulation.
            font: Police de caractères.
            fish_picture: Image du poisson.
            shark_picture: Image du requin.
        """
        screen.fill((0, 123, 167))
        for y in range(self.world.height):
            for x in range(self.world.length):
                cell = self.world.world_map[x][y]
                if cell == '\U0001f41f':
                    screen.blit(fish_picture, (x*self.cell_size, y*self.cell_size))
                elif cell == '\U0001f988':
                    screen.blit(shark_picture, (x*self.cell_size, y*self.cell_size))

        text_chronons = font.render(f"Chronons: {self.chronons}", True, (0, 0, 0))
        shark_txt = font.render(f"Sharks: {len(self.world.list_sharks)}", True, (0, 0, 0))
        fish_txt = font.render(f"Fishes: {len(self.world.list_fishes)}", True, (0, 0, 0))
        screen.blit(text_chronons, (10, self.world.height*self.cell_size + 10))
        screen.blit(shark_txt, (10, self.world.height*self.cell_size + 40))
        screen.blit(fish_txt, (10, self.world.height*self.cell_size + 60))
        pygame.display.flip()

    def initialisation(self):
        """
        Initialise la fenêtre graphique de la simulation et exécute la boucle principale de la simulation.
        """
        pygame.init()
        length = self.world.length * self.cell_size
        height = self.world.height * self.cell_size
        screen = pygame.display.set_mode((length, height + 80))
        pygame.display.set_caption("Projet Wa_tor")

        fish_picture = pygame.image.load("fish.png").convert_alpha()
        shark_picture = pygame.image.load("shark.png").convert_alpha()

        fish_picture = pygame.transform.scale(fish_picture, (self.cell_size, self.cell_size))
        shark_picture = pygame.transform.scale(shark_picture, (self.cell_size, self.cell_size))

        self.world.populate(self.list_fishes, self.list_sharks)

        running = True
        font = pygame.font.Font(None, 25)

        plt.ion()
        fig, ax = plt.subplots()
        ax.set_title("Evolution of fish and shark numbers")
        ax.set_xlabel("Time")
        ax.set_ylabel("Number")

        fishes_line, = ax.plot(self.time, self.list_fishes_data, label="Fishes")
        sharks_line, = ax.plot(self.time, self.list_sharks_data, label="Sharks")

        ax.legend(loc="upper left")

        plt.show()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.ending_simulation()

            self.update()
            self.draw(screen, font, fish_picture, shark_picture)

            pygame.time.delay(self.delay_chronon)

            self.time.append(self.chronons)
            self.list_fishes_data.append(len(self.world.list_fishes))
            self.list_sharks_data.append(len(self.world.list_sharks))

            fishes_line.set_data(self.time, self.list_fishes_data)
            sharks_line.set_data(self.time, self.list_sharks_data)

            ax.relim()
            ax.autoscale_view()

            plt.pause(0.01)
            plt.draw()

            pygame.display.flip()

    def ending_simulation(self):
        """
        Termine la simulation en fermant la fenêtre graphique.
        """
        self.on = False
        pygame.quit()
