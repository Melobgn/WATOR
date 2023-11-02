import pygame
from simulation import Simulation
import sys

def main():
    pygame.init()

    simulation = Simulation(12, 12, 50, 20, 4, 800)
    simulation.initialiser()

    running = True

    while running:
        simulation.gerer_evenements()
        simulation.mise_a_jour()
        simulation.afficher()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    simulation.terminer_simulation()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
