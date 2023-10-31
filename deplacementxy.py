import os
import time
import random


class Monde:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
        self.monde = [['\U0001f4a7' for _ in range(largeur)] for _ in range(longueur)]
        self.poissons = []
        self.requins = []
        self.temps_starvation = 8

    def affichage_monde(self):
        for row in self.monde:
            print(*row)

    def peupler_le_monde(self, nb_poissons, nb_requins):
        self.nb_poissons = nb_poissons
        self.nb_requins = nb_requins
        random.seed(12)
        coordonnees_possibles = [(x, y) for x in range(self.largeur) for y in range(self.longueur)]
        random.shuffle(coordonnees_possibles)

        for _ in range(self.nb_poissons):
            if not coordonnees_possibles:
                break
            x, y = coordonnees_possibles.pop()
            self.monde[x][y] = '\U0001f41f'
            self.poissons.append((x, y))

        for _ in range(self.nb_requins):
            if not coordonnees_possibles:
                break
            x, y = coordonnees_possibles.pop()
            self.monde[x][y] = '\U0001f988'
            self.requins.append((x, y))

class Poisson:
    def __init__(self, monde):
        self.monde = monde

    def cases_vides_adjacentes(self, x, y):
        deplacement_possible = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        directions_possibles = deplacement_possible[:]
        random.shuffle(directions_possibles)
        cases_vides = []

        for dx, dy in directions_possibles:
            new_x, new_y = x + dx, y + dy
            if self.est_dans_le_monde(new_x, new_y) and self.monde.monde[new_x][new_y] == '\U0001f4a7':
                cases_vides.append((dx, dy))

        return cases_vides

    def deplacer_poisson(self, x, y, direction):
        new_x = x + direction[0]
        new_y = y + direction[1]
        self.monde.monde[x][y] = '\U0001f4a7'
        self.monde.monde[new_x][new_y] = '\U0001f41f'
        return new_x, new_y

    def est_dans_le_monde(self, x, y):
        return 0 <= x < self.monde.largeur and 0 <= y < self.monde.longueur

    def se_deplacer(self):
        new_poissons = []
        for x, y in self.monde.poissons:
            cases_vides = self.cases_vides_adjacentes(x, y)
            if cases_vides:
                direction_choisie = random.choice(cases_vides)
                new_x, new_y = self.deplacer_poisson(x, y, direction_choisie)
                new_poissons.append((new_x, new_y))
        self.monde.poissons = new_poissons

class Requin(Poisson):
    def __init__(self, monde, energie):
        super().__init__(monde)
        self.energie = energie
        

    def cases_vides_adjacentes(self, x, y):
        deplacement_possible = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        directions_possibles = deplacement_possible[:]
        random.shuffle(directions_possibles)
        cases_vides = []

        for dx, dy in directions_possibles:
            new_x, new_y = x + dx, y + dy
            if self.est_dans_le_monde(new_x, new_y) and self.monde.monde[new_x][new_y] == '\U0001f4a7':
                cases_vides.append((dx, dy))

        return cases_vides

    def deplacer_requin(self, x, y, direction):
        new_x = x + direction[0]
        new_y = y + direction[1]
        self.monde.monde[x][y] = '\U0001f4a7'
        self.monde.monde[new_x][new_y] = '\U0001f988'
        return new_x, new_y

    def est_dans_le_monde(self, x, y):
        return 0 <= x < self.monde.largeur and 0 <= y < self.monde.longueur

    def se_deplacer(self):
        new_requins = []
        for x, y in self.monde.requins:
            cases_vides = self.cases_vides_adjacentes(x, y)
            if cases_vides:
                direction_choisie = random.choice(cases_vides)
                new_x, new_y = self.deplacer_requin(x, y, direction_choisie)
                new_requins.append((new_x, new_y))
        self.monde.requins = new_requins

chronons = 0
mon_monde = Monde(10, 10)
deplacement_poisson = Poisson(mon_monde)
deplacement_requin = Requin(mon_monde, 2)
mon_monde.peupler_le_monde(10,2)
mon_monde.affichage_monde()

#Compteur chronons
while chronons < 100:
    os.system('clear')
    deplacement_poisson.se_deplacer()
    deplacement_requin.se_deplacer()
    # deplacement_requin.starvation()
    mon_monde.affichage_monde()
    print()
    chronons += 1
    time.sleep(0.8)
    