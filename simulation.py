import os
import time
import random
import pygame
import matplotlib.pyplot as plt

class World:
    def __init__(self, length, height):
        self.length = length
        self.height = height
        self.water_drop = 0
        self.world_map = [[self.water_drop for _ in range(length)] for _ in range(height)]
        self.list_fishes = []
        self.list_sharks = []

    def see_world(self):
        for row in self.world_map:
            print(*row)
        print(f"Poissons : {len(self.list_fishes)}")
        print(f"Requins : {len(self.list_sharks)}")

    def populate(self, nb_fishes, nb_sharks):
        coord_possible = [(x, y) for x in range(self.length) for y in range(self.height)]
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
        for fish in self.list_fishes:
            self.world_map[fish.x][fish.y] = fish.icons_fish
        for shark in self.list_sharks:
            self.world_map[shark.x][shark.y] = shark.icons_shark

class Fish:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.type_id = 1
        self.icons_fish = '\U0001f420'
        self.gestation = 0
        self.gestation_time = 10

    def adjacent_empty_cells(self):
        
        list_travel_possible = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        random.shuffle(list_travel_possible)
        empty_cells = []

        for dx, dy in list_travel_possible:
            new_x, new_y = (self.x + dx) % self.world.length, (self.y + dy) % self.world.height
            if self.world.world_map[new_x][new_y] == 0:
                empty_cells.append((dx, dy))

        return empty_cells

    def move_prey(self):
        empty_cells = self.adjacent_empty_cells()
        if not empty_cells:
            self.gestation += 1
            return
        else:
            dx, dy = random.choice(empty_cells)
            new_x = (self.x + dx) % self.world.length
            new_y = (self.y + dy) % self.world.height
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
    def __init__(self, world, x, y):
        super().__init__(world, x, y)
        self.type_id = 2
        self.icons_shark = '\U0001f988'
        self.energy = 8
        self.gestation_time = 40

    def move_carnivore(self):
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
                self.energy += 3
                self.world.list_fishes.remove(fish)


class Simulation:
    def __init__(self, length, height, nb_fishes, nb_sharks, delay_chronon, cell_size):
        self.world = World(length, height)
        self.chronons = 0
        self.delay_chronon = delay_chronon
        self.on = True
        self.list_fishes = nb_fishes
        self.list_sharks = nb_sharks
        self.cell_size = cell_size

        self.time = [0]
        self.list_fishes_data = [nb_fishes]
        self.list_sharks_data = [nb_sharks]

    def initialisation(self):
        pygame.init()
        length = self.world.length * self.cell_size
        height = self.world.height * self.cell_size
        screen = pygame.display.set_mode((length, height + 80))
        pygame.display.set_caption("Projet Wa_tor")

        fish_picture = pygame.image.load("fish.png").convert_alpha()
        shark_picture = pygame.image.load("shark.png").convert_alpha()

        fish_picture = pygame.transform.scale(fish_picture, (self.cell_size, self.cell_size))
        shark_picture = pygame.transform.scale(shark_picture, (self.cell_size, self.cell_size))
        color_background = (0, 127, 255)
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
            screen.fill((255, 255, 255))

            for fish in self.world.list_fishes:
                fish.move_prey()
            for shark in self.world.list_sharks:
                shark.move_carnivore()
                shark.starvation()
                shark.eat_prey()
            for fish in self.world.list_fishes:
                self.world.world_map[fish.x][fish.y] = '\U0001f41f'

            for shark in self.world.list_sharks:
                self.world.world_map[shark.x][shark.y] = '\U0001f988'

            for i in range(self.world.height):
                for j in range(self.world.length):
                    cell = self.world.world_map[i][j]
                    x = j * self.cell_size
                    y = i * self.cell_size
                    pygame.draw.rect(screen, color_background, (x, y, self.cell_size, self.cell_size))
                    if cell == '\U0001f41f':
                        screen.blit(fish_picture, (x, y))
                    elif cell == '\U0001f988':
                        screen.blit(shark_picture, (x, y))

            text_chronons = font.render(f"Chronons: {self.chronons}", True, (0, 0, 0))
            shark_txt = font.render(f"Sharks: {len(self.world.list_sharks)}", True, (0, 0, 0))
            fish_txt = font.render(f"Fishes: {len(self.world.list_fishes)}", True, (0, 0, 0))
            screen.blit(text_chronons, (10, height + 10))
            screen.blit(shark_txt, (10, height + 40))
            screen.blit(fish_txt, (10, height + 60))
            pygame.display.flip()
            #self.chronons += 1
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
            self.chronons += 1
            pygame.time.delay(self.delay_chronon)

    def manage_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.ending_simulation()

    def ending_simulation(self):
        self.on = False
        pygame.quit()