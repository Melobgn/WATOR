import pygame
from simulation import Simulation, World
import sys


def main():
    world = World(50, 50)
    simulation = Simulation(world, 1000, 40, 10, 15)
    simulation.initialisation()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    simulation.ending_simulation()

if __name__ == "__main__":
    main()
