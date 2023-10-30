import time
import os
import random


class Monde:
    def __init__(self, largeur, longueur):
        self.largeur = largeur
        self.longueur = longueur
        self.nb_poissons = nb_poissons
        self.nb_requins = nb_requins
        self.temps_reproduction_poisson = 8
        self.temps_reproduction_requin = 12
        self.poissons = []
        self.requins = []
        self.grille = [['\U0001f4a7' for i in range(largeur)] for y in range(longueur)]
        
        

  


    def compter(self):
        coordonnees_possibles = [(x, y) for x in range(longueur) for y in range(largeur)]
        random_choice = random.shuffle(coordonnees_possibles)
        return random_choice


    # def jouer_un_tour():


    def peupler_le_monde(self):
        # Place les poissons dans la grille
        for poisson in range(nb_poissons):
            if not self.compter():
                break  # Si on a utilisé toutes les coordonnées possibles, sortir de la boucle
            row, col = self.compter().pop()
            Monde.grille[row][col] = '\U0001f41f'
            self.poissons.append(row, col)
            print(self.poissons)
            
        # Place les requins dans la grille
        for requin in range(nb_requins):
            if not self.compter():
                break  # Si on a utilisé toutes les coordonnées possibles, sortir de la boucle
            row, col = self.compter().pop()
            Monde.grille[row][col] = '\U0001f988'
            self.requins.append(row, col)

    def afficher_le_monde(self):
        for i in self.grille:
            print(*i)

class Poisson:
    def __init__(self, monde):
        self.monde = monde
        self.temps_reproduction = 8

    def poisson_x(self):
        for poisson in Monde.poissons:
            poisson['row']
            
    def poisson_y(self):
        for poisson in Monde.poissons:
            poisson['col']




longueur = 10
largeur = 8
nb_poissons = 10
nb_requins = 2
temps_reproduction_poisson = 12
temps_reproduction_requin = 8
ma_planete = Monde(10,10)

chronons = 0
while chronons < 100:
    os.system('clear')
    ma_planete.afficher_le_monde()
    print()
    chronons += 1
    time.sleep(0.8)
        





