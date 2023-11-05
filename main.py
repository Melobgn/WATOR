import pygame
from simulation import Simulation, World
import sys


def main():
    pygame.init()
    world = World(50,50)
    simulation = Simulation(world,1000, 40, 10, 15)
    simulation.initialisation()

    simulation.ending_simulation()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()