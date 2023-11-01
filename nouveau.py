import random
import os
import time


class Monde():
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
        self.monde = [['\U0001f4a7' for i in range(largeur)] for y in range(longueur)]
        self.poissons = []
        self.requins = []
        
    def affichage_monde(self):
        for i in self.monde:
            print(*i)

    
    def jouer_un_tour(self):
        chronons = 0
        while chronons < 100:
            os.system('clear')
            chronons += 1
            self.time.sleep= time.sleep()

    def peupler_le_monde(self, nb_poissons, nb_requins):
        self.nb_poissons = nb_poissons
        self.nb_requins = nb_requins
        random.seed(12)
        coordonnees_possibles = [(x, y) for x in range(self.longueur) for y in range(self.largeur)]
        random.shuffle(coordonnees_possibles)
        
        # Place les poissons dans la grille
        for poisson in range(self.nb_poissons):
            if not coordonnees_possibles:
                break  # Si on a utilisé toutes les coordonnées possibles, sortir de la boucle
            row, col = coordonnees_possibles.pop()
            self.monde[row][col] = '\U0001f41f'
            self.poissons.append({'row': row, 'col': col})
        
        # Place les requins dans la grille
        for requin in range(self.nb_requins):
            if not coordonnees_possibles:
                break  # Si on a utilisé toutes les coordonnées possibles, sortir de la boucle
            row, col = coordonnees_possibles.pop()
            self.monde[row][col] = '\U0001f988'
            self.requins.append({'row': row, 'col': col})


class Poisson():
    def __init__(self, monde):
        self.monde = monde

    
    def cases_vides_adjacentes(self):
        deplacement_possible = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.directions_possibles = deplacement_possible[:]
        return random.shuffle(self.directions_possibles)

    def faire_un_tour(self, grille):
        self.grille = grille
        pass

    def se_deplacer(self):
        for poisson in self.monde.poissons:
            self.cases_vides_adjacentes()
        for direction in self.directions_possibles:
                new_row = poisson['row'] + direction[0]
                new_col = poisson['col'] + direction[1]

                if 0 <= new_row < self.monde.longueur and 0 <= new_col < self.monde.largeur:
                    if self.monde.monde[new_row][new_col] == '\U0001f4a7':  # eau
                        self.monde.monde[poisson['row']][poisson['col']] = '\U0001f4a7'  # eau
                        self.monde.monde[new_row][new_col] = '\U0001f41f'  # poisson
                        poisson['row'] = new_row
                        poisson['col'] = new_col
                        break

    def se_reproduire(self, grille, animal, y_target:int, x_target:int):
        self.grille = grille
        self.animal = animal
        self.y_target = y_target
        self.x_target = x_target
        pass


class Requin(Poisson):
    def __init__(self, compteur_reproduction, temps_de_reproduction, x, y, energie) -> None:
        super().__init__(compteur_reproduction, temps_de_reproduction, x, y)
        self.energie = energie

    def cases_poissons_adjacentes(self, monde):
        self.monde = monde
        pass
        
    def faire_un_tour(self,monde):
        self.monde = monde
        pass

    def se_deplacer(self, monde):
        pass

mon_monde = Monde(10, 10)
mon_monde.peupler_le_monde(10,2)
mon_monde.affichage_monde()
deplacement_poisson = Poisson(mon_monde)
deplacement_poisson.se_deplacer()
print()
mon_monde.affichage_monde()





