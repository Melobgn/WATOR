vide = [0][0]

eau = 0
poisson = 1
requin = 2


class Planete:
    def __init__(self, pos_x, pos_y)
        self.pos_x = pos_x
        self.pos_y = pos_y


class Poisson:
    def __init__(self, pos_x, pos_y, gestation_finie):
        self.id_poisson = id_poisson
        self.pos_x = pos_x
        self.pos_y = pos_y
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
            else: self.gestation_time += 1


class Requin(Poisson):
    def __init__(self, gestation_finie, alimentation, temps_starvation):
        super().__init__(gestation_finie)
        self.alimentation = alimentation
        self.temps_starvation = temps_starvation
        temps_starvation = 15

    def energie(self):
         if Requin.temps_starvation < 0:
            # Creature dies.
            Requin.dead = True
            self.monde_ready[Requin.row][Requin.col] = vide


