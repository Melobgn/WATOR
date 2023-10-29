import random

class Planete:
    def __init__(self, longueur, largeur, nombre_poissons, nombre_requins):
        self.longueur = longueur
        self.largeur = largeur
        self.nombre_poissons = nombre_poissons
        self.nombre_requins = nombre_requins
        self.monde = [['\U0001f4a7' for _ in range(largeur)] for _ in range(longueur)]
        self.poissons = []
        self.requins = []

    def creation_monde(self):
        random.seed(12)
        coordonnees_possibles = [(x, y) for x in range(self.longueur) for y in range(self.largeur)]
        random.shuffle(coordonnees_possibles)

        # Place les poissons dans la grille
        for _ in range(self.nombre_poissons):
            if not coordonnees_possibles:
                break
            row, col = coordonnees_possibles.pop()
            self.monde[row][col] = '\U0001f41f'
            self.poissons.append({'row': row, 'col': col})

        # Place les requins dans la grille
        for _ in range(self.nombre_requins):
            if not coordonnees_possibles:
                break
            row, col = coordonnees_possibles.pop()
            self.monde[row][col] = '\U0001f988'
            self.requins.append({'row': row, 'col': col})

    def deplacer_poissons(self):
        deplacement_possible = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        poissons_survivants = []
        poisson_mange = False  # Initialisation de la variable à l'extérieur de la boucle

        for poisson in self.poissons:
            directions_possibles = deplacement_possible[:]
            random.shuffle(directions_possibles)

            for direction in directions_possibles:
                new_row = poisson['row'] + direction[0]
                new_col = poisson['col'] + direction[1]

                for requin in self.requins:
                    if abs(new_row - requin['row']) <= 1 and abs(new_col - requin['col']) <= 1:
                        self.monde[poisson['row']][poisson['col']] = '\U0001f4a7'
                        poisson_mange = True
                        break

                if poisson_mange:
                    break

            if not poisson_mange:
                poissons_survivants.append(poisson)

        if poisson_mange:
            self.poissons.remove(poisson)

        self.poissons = poissons_survivants

        for poisson in poissons_survivants:
            directions_possibles = deplacement_possible[:]
            random.shuffle(directions_possibles)

            for direction in directions_possibles:
                new_row = poisson['row'] + direction[0]
                new_col = poisson['col'] + direction[1]

                if 0 <= new_row < self.longueur and 0 <= new_col < self.largeur:
                    if self.monde[new_row][new_col] == '\U0001f4a7':
                        self.monde[poisson['row']][poisson['col']] = '\U0001f4a7'
                        self.monde[new_row][new_col] = '\U0001f41f'
                        poisson['row'] = new_row
                        poisson['col'] = new_col
                        break


    def deplacer_requins(self):
        for requin in self.requins:
            directions_possibles = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            random.shuffle(directions_possibles)

            deplacement_reussi = False

            for direction in directions_possibles:
                new_row = requin['row'] + direction[0]
                new_col = requin['col'] + direction[1]

                if 0 <= new_row < self.longueur and 0 <= new_col < self.largeur:
                    if self.monde[new_row][new_col] == '\U0001f41f':
                        self.monde[requin['row']][requin['col']] = '\U0001f4a7'
                        self.monde[new_row][new_col] = '\U0001f988'
                        requin['row'] = new_row
                        requin['col'] = new_col
                        deplacement_reussi = True
                    elif self.monde[new_row][new_col] == '\U0001f4a7':
                        self.monde[requin['row']][requin['col']] = '\U0001f4a7'
                        self.monde[new_row][new_col] = '\U0001f988'
                        requin['row'] = new_row
                        requin['col'] = new_col
                        deplacement_reussi = True
                    if deplacement_reussi:
                        break

    def coordonnees_poissons_requins(self):
        for poisson in self.poissons:
            print(f"Coordonnées du poisson : ({poisson['row']}, {poisson['col']})")

        for requin in self.requins:
            print(f"Coordonnées du requin : ({requin['row']}, {requin['col']})")

    def affichage(self):
        for row in self.monde:
            print(*row)
