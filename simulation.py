import random

class Monde:
    def __init__(self, longueur, hauteur, taille_cellule):
        self.longueur = longueur
        self.hauteur = hauteur
        self.taille_cellule = taille_cellule
        self.monde = [['\U0001f4a7' for _ in range(longueur)] for _ in range(hauteur)]
        self.poissons = []
        self.requins = []
        self.temps_starvation = 8

    def peupler_le_monde(self, nb_poissons, nb_requins):
        self.nb_poissons = nb_poissons
        self.nb_requins = nb_requins
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

    def get_cell(self, x, y):
        return self.monde[x % self.longueur][y % self.hauteur]

    def set_cell(self, x, y, value):
        self.monde[x % self.longueur][y % self.hauteur] = value


class Poisson:
    def __init__(self, monde):
        self.monde = monde

    def deplacer_poisson(self, x, y, direction):
        new_x = x + direction[0]
        new_y = y + direction[1]
        self.monde.set_cell(x, y, '\U0001f4a7')
        self.monde.set_cell(new_x, new_y, '\U0001f41f')
        return new_x, new_y

    def cases_vides_adjacentes(self, x, y):
        deplacement_possible = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(deplacement_possible)
        cases_vides = []

        for dx, dy in deplacement_possible:
            new_x = x + dx
            new_y = y + dy
            if self.monde.get_cell(new_x, new_y) == '\U0001f4a7':
                cases_vides.append((dx, dy))

        return cases_vides

    def se_deplacer(self):
        new_poissons = []
        for x, y in self.monde.poissons:
            cases_vides = self.cases_vides_adjacentes(x, y)
            if cases_vides:
                direction_choisie = random.choice(cases_vides)
                new_x, new_y = self.deplacer_poisson(x, y, direction_choisie)
                new_poissons.append((new_x, new_y))
            else:
                new_poissons.append((x, y))  # Si le poisson ne peut pas bouger, il reste à sa place

        self.monde.poissons = new_poissons


class Requin(Poisson):
    def __init__(self, monde):
        super().__init__(monde)
        self.energie = 20

    def deplacer_requin(self, x, y, direction):
        new_x = x + direction[0]
        new_y = y + direction[1]
        self.monde.set_cell(x, y, '\U0001f4a7')
        self.monde.set_cell(new_x, new_y, '\U0001f988')
        return new_x, new_y

    def cases_avec_un_poisson(self, x, y):
        deplacement_possible = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        directions_possibles = deplacement_possible[:]
        random.shuffle(directions_possibles)
        cases_avec_poisson = []

        for dx, dy in directions_possibles:
            new_x = x + dx
            new_y = y + dy
            if self.monde.get_cell(new_x, new_y) == '\U0001f41f':
                cases_avec_poisson.append((dx, dy))

        return cases_avec_poisson

    def se_deplacer(self):
        new_requins = []
        for x, y in self.monde.requins:
            cases_vides = self.cases_vides_adjacentes(x, y)
            if cases_vides:
                direction_choisie = random.choice(cases_vides)
                new_x, new_y = self.deplacer_requin(x, y, direction_choisie)
                new_requins.append((new_x, new_y))
            else:
                new_requins.append((x, y))  # Si le requin ne peut pas bouger alors il reste à sa position
        self.monde.requins = new_requins

    def starvation(self):
        requins_a_retirer = []

        for x, y in self.monde.requins:
            if self.energie <= 0:  # Si l'énergie est épuisée
                self.monde.set_cell(x, y, '\U0001f4a7')  # Mettre de l'eau à la place du requin
                requins_a_retirer.append((x, y))
            else:
                self.energie -= 0.5  # Réduire l'énergie du requin à chaque tour

        for requin in requins_a_retirer:
            self.monde.requins.remove(requin)

    def manger_poisson(self):
        poissons_a_retirer = []

        for requin_x, requin_y in self.monde.requins:
            for poisson_x, poisson_y in self.monde.poissons:
                if abs(requin_x - poisson_x) <= 1 and abs(requin_y - poisson_y) <= 1:
                    self.monde.set_cell(poisson_x, poisson_y, '\U0001f4a7')
                    self.energie += 10
                    poissons_a_retirer.append((poisson_x, poisson_y))

        for poisson in poissons_a_retirer:
            self.monde.poissons.remove(poisson)

    def reproduction(self):
        poissons_a_ajouter = []
        for x, y in self.monde.poissons[:]:
            if self.gestation == self.monde.temps_reproduction_poisson:
                directions_possibles = self.cases_vides_adjacentes(x, y)
                if directions_possibles:
                    direction_choisie = random.choice(directions_possibles)
                    new_x, new_y = self.deplacer_poisson(x, y, direction_choisie)
                    poissons_a_ajouter.append((new_x, new_y))
                    self.gestation = 0
                    self.monde.set_cell(new_x, new_y, '\U0001f41f')  # Mettez à jour la grille avec le bébé poisson
            else:
                self.gestation += 1
        self.monde.poissons.extend(poissons_a_ajouter)
