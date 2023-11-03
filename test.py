
class Requin(Poisson):
    def __init__(self, monde, x, y):
        super().__init__(monde, x, y)
        self.energie = 10
        self.temps_de_reproduction = 20
        self.gestation = 0


    def deplacer_requin(self):
        cases_vides = self.cases_vides_adjacentes()
        if not cases_vides:
            self.gestation += 1
            return
        elif cases_vides:
            self.cases_poissons_miam()
        if not self.cases_poissons_miam():
            if cases_vides:
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
        
    def cases_poissons_miam(self):
        poisson_proche = None
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
                self.energie += 1
                self.monde.poissons.remove(poiscaille)

    def reproduction_requin(self):
        requin_bebe = Requin(self.monde, self.x, self.y)
        self.monde.requins.append(requin_bebe)
        self.monde.grille[self.x][self.y] = '\U0001f988'