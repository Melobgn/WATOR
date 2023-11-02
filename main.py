import pygame
from simulation import Simulation

def main():
    pygame.init()

    simulation = Simulation(12, 12, 50, 20, 4, 800)
    simulation.initialiser()

    while simulation.en_cours():
        simulation.gerer_evenements()
        simulation.mise_a_jour()
        simulation.afficher()

    pygame.quit()

if __name__ == "__main__":
    main()