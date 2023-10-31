import os
import time
import random


class Monde:
    def __init__(self, longueur, hauteur):
        self.longueur = longueur
        self.hauteur = hauteur
        self.monde = [['\U0001f4a7' for _ in range(longueur)] for _ in range(hauteur)]
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
        coordonnees_possibles = [(x, y) for x in range(self.longueur) for y in range(self.hauteur)]
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
        return 0 <= x < self.monde.longueur and 0 <= y < self.monde.hauteur

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
    def __init__(self, monde):
        super().__init__(monde)
        self.energie = 20
        

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
        return 0 <= x < self.monde.longueur and 0 <= y < self.monde.hauteur

    def se_deplacer(self):
        new_requins = []
        for x, y in self.monde.requins:
            cases_vides = self.cases_vides_adjacentes(x, y)
            if cases_vides:
                direction_choisie = random.choice(cases_vides)
                new_x, new_y = self.deplacer_requin(x, y, direction_choisie)
                new_requins.append((new_x, new_y))
        self.monde.requins = new_requins


    def starvation(self):
        requins_a_retirer = []

        for x, y in self.monde.requins:
            if self.energie <= 0:  # Si l'énergie est épuisée
                self.monde.monde[x][y] = '\U0001f4a7'  # Mettre de l'eau à la place du requin
                requins_a_retirer.append((x, y))
            else:
                self.energie -= 1 # Réduire l'énergie du requin à chaque tour

        for requin in requins_a_retirer:
            self.monde.requins.remove(requin)

    
    def manger_poisson(self):
        poissons_a_retirer = []

        for requin_x, requin_y in self.monde.requins:
            for poisson_x, poisson_y in self.monde.poissons:
                if (abs(requin_x - poisson_x) <= 1 and abs(requin_y - poisson_y) <= 1):
                    self.monde.monde[poisson_x][poisson_y] = '\U0001f4a7'
                    self.energie += 5
                    poissons_a_retirer.append((poisson_x, poisson_y))

        for poisson in poissons_a_retirer:
            self.monde.poissons.remove(poisson)


    
    # def deplacer_poisson(self, poisson, direction):
    #     return super().deplacer_poisson(poisson, direction)

    

chronons = 0
mon_monde = Monde(10, 10)
deplacement_poisson = Poisson(mon_monde)
deplacement_requin = Requin(mon_monde)
mon_monde.peupler_le_monde(10,3)
mon_monde.affichage_monde()

#Compteur chronons
while chronons < 100:
    os.system('clear')
    deplacement_poisson.se_deplacer()
    deplacement_requin.se_deplacer()
    deplacement_requin.starvation()
    deplacement_requin.manger_poisson()
    mon_monde.affichage_monde()
    print()
    chronons += 1
    time.sleep(1)
    
