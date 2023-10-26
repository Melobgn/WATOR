class Poisson:
    def __init__(self, energie, gestation_finie):
        self.energie = energie
        self.gestation_finie = gestation_finie
        gestation_finie = 8

    def gestation(self):
        self.gestation_time = 0

     def mouvement(self):
        # find empty neighbors...
        vide = [voisin for voisin in self.cell.voisin if voisin.content is None]
        if vide:
            if self.gestation_time >= self.gestation_finie:     # if the gestation clock is past due:
                self.cell.place(Poisson())         #   place a new fish at the current position
                self.gestation_time = 0 


class Requin(Poisson):
    def __init__(self, nom, energie, alimentation):
        super().__init__(nom , energie)
        self.alimentation = alimentation


    def energie(self):
         if Requin.temps_starvation < 0:
            # Creature dies.
            Requin.dead = True
            self.grid[Requin.y][Requin.x] = vide