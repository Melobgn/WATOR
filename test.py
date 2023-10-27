import random
import time
import os


class Planete:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.monde = []  # Initialiser la variable "monde"
    
    # fonction pour créer le monde de départ
    def creation_monde(self, longueur, largeur, nombre_poissons, nombre_requins):
        self.longueur = longueur
        self.largeur = largeur
        self.nombre_poissons = nombre_poissons
        self.nombre_requins = nombre_requins
        monde = [['\U0001f4a7' for i in range(largeur)] for y in range(longueur)]  # Créer une grille 2D pour le monde
        random.seed(12)
        coordonnees_possibles = [(x, y) for x in range(longueur) for y in range(largeur)]
        random.shuffle(coordonnees_possibles)

        self.poissons = []  # Liste pour stocker les poissons
        self.requins = []   # Liste pour stocker les requins

        # Place les poissons dans la grille
        for poisson in range(nombre_poissons):
            if not coordonnees_possibles:
                break  # Si on a utilisé toutes les coordonnées possibles, sortir de la boucle
            row, col = coordonnees_possibles.pop()
            monde[row][col] = '\U0001f41f'
            self.poissons.append({'row': row, 'col': col})

        # Place les requins dans la grille
        for requin in range(nombre_requins):
            if not coordonnees_possibles:
                break  # Si on a utilisé toutes les coordonnées possibles, sortir de la boucle
            row, col = coordonnees_possibles.pop()
            monde[row][col] = '\U0001f988'
            self.requins.append({'row': row, 'col': col})

        self.monde = monde  # Mets à jour la variable de la planète avec le monde créé
        
        return monde

    def coordoonees_poissons_requins(self):
        # Afficher les coordonnées des poissons
        for poisson in self.poissons:
            print(f"Coordonnées du poisson : ({poisson['row']}, {poisson['col']})")

        # Afficher les coordonnées des requins
        for requin in self.requins:
            print(f"Coordonnées du requin : ({requin['row'], requin['col']})")

    #affiche le monde
    def affichage(self):
        for i in self.monde:
            print(*i)

class Poisson:
    def __init__(self, planete, reproduction=8):
        self.planete = planete
        self.reproduction = reproduction

    def deplacer_poissons(self):
        deplacement_possible = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
        for poisson in self.planete.poissons:
            directions_possibles = deplacement_possible[:]
            random.shuffle(directions_possibles)

            deplacement_reussi = False

            for direction in directions_possibles:
                new_row = poisson['row'] + direction[0]
                new_col = poisson['col'] + direction[1]
                if 0 <= new_row < self.planete.longueur and 0 <= new_col < self.planete.largeur:
                    if self.planete.monde[new_row][new_col] == '\U0001f4a7':
                        self.planete.monde[poisson['row']][poisson['col']] = '\U0001f4a7'
                        self.planete.monde[new_row][new_col] = '\U0001f41f'
                        poisson['row'] = new_row
                        poisson['col'] = new_col
                        deplacement_reussi = True
                        break
            if not deplacement_reussi:
               
                return self.monde
            
    def gestation(self):
        self.gestation_time = 0
        if self.gestation_time >= self.gestation_finie:     # if the gestation clock is past due:
                self.poisson['row']
                self.poisson['col']       #   place a new fish at the current position
                self.gestation_time = 0
        else: self.gestation_time += 1

            


# time.sleep(0.4)
  


# Initialisation des valeurs
longueur = 10
largeur = 8
nombre_poissons = 10
nombre_requins = 5
chronons = 0

# création de l'instance de la classe Planete


ma_planete = Planete(0, 0)

# initialisation du monde
ma_planete.creation_monde(longueur, largeur, nombre_poissons, nombre_requins)

# affichage du monde
ma_planete.affichage()
poisson_instance = Poisson(ma_planete)
#affiche les coordonnees des poissons et des requins
# ma_planete.coordoonees_poissons_requins()
while chronons < 100:
    os.system('clear')
    poisson_instance.deplacer_poissons()
    ma_planete.affichage()
    print()
    chronons += 1
    time.sleep(0.4)