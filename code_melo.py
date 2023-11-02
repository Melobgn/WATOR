import os
import time
import random


class Monde:
    def __init__(self, longueur, hauteur):
        self.longueur = longueur
        self.hauteur = hauteur
        self.grille = [[0 for _ in range(longueur)] for _ in range(hauteur)]
        self.poissons = []
        self.requins = []

    def affichage_monde(self):
        for row in self.grille:
            print(*row)

    def peupler_le_monde(self, nb_poissons, nb_requins):
        self.nb_poissons = nb_poissons
        self.nb_requins = nb_requins
        # random.seed(12)
        coordonnees_possibles = [(x, y) for x in range(self.longueur) for y in range(self.hauteur)]
        random.shuffle(coordonnees_possibles)

        for _ in range(self.nb_poissons):
            if not coordonnees_possibles:
                break
            x, y = coordonnees_possibles.pop()
            self.grille[x][y] = '\U0001f41f'
            poiscaille = Poisson(self, x, y)
            self.poissons.append(poiscaille)

        for _ in range(self.nb_requins):
            if not coordonnees_possibles:
                break
            x, y = coordonnees_possibles.pop()
            self.grille[x][y] = '\U0001f988'
            requinx = Requin(self, x, y)
            self.requins.append(requinx)


class Poisson:
    def __init__(self, monde, x, y):
        self.monde = monde
        self.x = x
        self.y = y
        self.temps_de_reproduction = 8
        self.gestation = 0

    def cases_vides_adjacentes(self):
        deplacement_possible = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(deplacement_possible)
        cases_vides = []

        for dx, dy in deplacement_possible:
            new_x = (self.x + dx) % self.monde.longueur
            new_y = (self.y + dy) % self.monde.hauteur
            if self.monde.grille[new_x][new_y] == 0:
                cases_vides.append((dx, dy))

        return cases_vides

    
    def deplacer_poisson(self):
        cases_vides = self.cases_vides_adjacentes()
        if not cases_vides:
            self.gestation += 1
            return
        elif cases_vides:
            direction_choisie = random.choice(cases_vides)
            dx, dy = direction_choisie
            new_x = (self.x + dx) % self.monde.longueur
            new_y = (self.y + dy) % self.monde.hauteur
            if self.gestation >= self.temps_de_reproduction:
                self.reproduction()
                self.gestation = 0
            else:
                self.monde.grille[self.x][self.y] = 0
                self.monde.grille[new_x][new_y] = '\U0001f41f'
                self.x, self.y = new_x, new_y
                self.gestation += 1

    def reproduction(self):
        #print("Reproduction called for fish at ({}, {})".format(self.x, self.y))  # Ajoutez cette ligne pour le débogage
        poisson_bebe = Poisson(self.monde, self.x, self.y)
        self.monde.poissons.append(poisson_bebe)
        self.monde.grille[self.x][self.y] = '\U0001f41f'
            

class Requin(Poisson):
    def __init__(self, monde, x, y):
        super().__init__(monde, x, y)
        self.energie = 12
        self.temps_de_reproduction = 15
        self.gestation = 0


    def deplacer_requin(self):
        poisson_proche = None
        cases_vides = self.cases_vides_adjacentes()
        if not cases_vides:
            self.gestation += 1
            return
        for poiscaille in self.monde.poissons:
            if abs(self.x - poiscaille.x) <= 1 and abs(self.y - poiscaille.y) <= 1:
                poisson_proche = poiscaille
        if poisson_proche:
            # Si un poisson est proche, se déplacer vers lui
            if self.x < poisson_proche.x:
                new_x, new_y = self.x + 1, self.y
            elif self.x > poisson_proche.x:
                new_x, new_y = self.x - 1, self.y
            elif self.y < poisson_proche.y:
                new_x, new_y = self.x, self.y + 1
            else:
                new_x, new_y = self.x, self.y - 1
            if self.gestation >= self.temps_de_reproduction:
                self.reproduction_requin()
                self.gestation = 0
            else:
                self.monde.grille[self.x][self.y] = 0
                self.monde.grille[new_x][new_y] = '\U0001f988'
                self.x, self.y = new_x, new_y
                self.gestation += 1

        elif cases_vides:
            # Si aucun poisson proche, se déplacer vers une case vide aléatoire
            direction_choisie = random.choice(cases_vides)
            dx, dy = direction_choisie
            new_x = (self.x + dx) % self.monde.longueur
            new_y = (self.y + dy) % self.monde.hauteur
            if self.gestation >= self.temps_de_reproduction:
                self.reproduction_requin()
                self.gestation = 0
            else:
                self.monde.grille[self.x][self.y] = 0
                self.monde.grille[new_x][new_y] = '\U0001f988'
                self.x, self.y = new_x, new_y
                self.gestation += 1
        
            
        
    def starvation(self):
        if self.energie <= 0:
            self.monde.grille[self.x][self.y] = 0
            self.monde.requins.remove(self)
        else:
            self.energie -= 1

    def manger_poisson(self):
        for poiscaille in self.monde.poissons:
            if (abs(self.x - poiscaille.x) <= 1 and abs(self.y - poiscaille.y) == 0) or (abs(self.x - poiscaille.x) == 0 and abs(self.y - poiscaille.y) <= 1):
                self.monde.grille[poiscaille.x][poiscaille.y] = 0
                self.energie += 2
                self.monde.poissons.remove(poiscaille)

    def reproduction_requin(self):
        requin_bebe = Requin(self.monde, self.x, self.y)
        self.monde.requins.append(requin_bebe)
        self.monde.grille[self.x][self.y] = '\U0001f988'
 

chronons = 0
mon_monde = Monde(10, 10)
poissons = mon_monde.poissons
requins = mon_monde.requins
mon_monde.peupler_le_monde(8,2)
mon_monde.affichage_monde()
print()

#Compteur chronons
while chronons < 50:
    os.system('cls')

    # Faites se déplacer chaque poisson
    for poiscaille in mon_monde.poissons:
        poiscaille.deplacer_poisson()

    # Faites se déplacer chaque requin
    for requinx in mon_monde.requins:
        requinx.deplacer_requin()
        requinx.manger_poisson()
        requinx.starvation()

    for poiscaille in mon_monde.poissons:
        mon_monde.grille[poiscaille.x][poiscaille.y] = '\U0001f41f'

    for requinx in mon_monde.requins:
        mon_monde.grille[requinx.x][requinx.y] = '\U0001f988'

    mon_monde.affichage_monde()
    print()
    chronons += 1
    time.sleep(1)