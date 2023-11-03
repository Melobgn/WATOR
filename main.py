import pygame
from simulation import Simulation
import sys

def main():
    pygame.init()

    simulation = Simulation(20, 20, 100, 40, 1000, 20)
    simulation.initialisation()

    running = True

    while running:
        simulation.manage_events()
        simulation.update()
        simulation.display()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    simulation.ending_simulation()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()