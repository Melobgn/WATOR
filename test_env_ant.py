import random

class Planete:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.monde = []  # Initialiser la variable "monde"
    
    # fonction pour créer le monde de départ
    def creation_monde(self, longueur, largueur, nombre_poissons, nombre_requins):
        self.longueur = longueur
        self.largueur = largueur
        self.nombre_poissons = nombre_poissons
        self.nombre_requins = nombre_requins
        monde = [[0 for i in range(largueur)] for y in range(longueur)]  # Créer une grille 2D pour le monde
        random.seed(12)
        coordonnees_possibles = [(x, y) for x in range(longueur) for y in range(largueur)]
        random.shuffle(coordonnees_possibles)

        self.poissons = []  # Liste pour stocker les poissons
        self.requins = []   # Liste pour stocker les requins

        # Place les poissons dans la grille
        for poisson in range(nombre_poissons):
            if not coordonnees_possibles:
                break  # Si on a utilisé toutes les coordonnées possibles, sortir de la boucle
            row, col = coordonnees_possibles.pop()
            monde[row][col] = 1
            self.poissons.append({'row': row, 'col': col})

        # Place les requins dans la grille
        for requin in range(nombre_requins):
            if not coordonnees_possibles:
                break  # Si on a utilisé toutes les coordonnées possibles, sortir de la boucle
            row, col = coordonnees_possibles.pop()
            monde[row][col] = 2
            self.requins.append({'row': row, 'col': col})

        self.monde = monde  # Mets à jour la variable de la planète avec le monde créé
        
        return monde

    def coordoonees_poissons_requins(self):
        # Afficher les coordonnées des poissons
        for poisson in self.poissons:
            print(f"Coordonnées du poisson : ({poisson['row']}, {poisson['col']})")

        # Afficher les coordonnées des requins
        for requin in self.requins:
            print(f"Coordonnées du requin : ({requin['row'], requin['col']})")

    #affiche le monde
    def affichage(self):
        for i in self.monde:
            print(*i)

    #essai pour déplacer les poissons
    def deplacer_poissons(self):
        for poisson in self.poissons:
            x, y = poisson['row'], poisson['col']
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            random.shuffle(directions)

            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy

                if 0 <= new_x < len(self.monde) and 0 <= new_y < len(self.monde[0]) and self.monde[new_x][new_y] == 0:
                    poisson['row'], poisson['col'] = new_x, new_y
                    self.monde[x][y], self.monde[new_x][new_y] = self.monde[new_x][new_y], self.monde[x][y]
                    break
                




# Initialisation des valeurs
longueur = 10
largueur = 8
nombre_poissons = 10
nombre_requins = 5

# création de l'instance de la classe Planete
ma_planete = Planete(0, 0)

# initialisation du monde
ma_planete.creation_monde(longueur, largueur, nombre_poissons, nombre_requins)

# affichage du monde
ma_planete.affichage()

#affiche les coordonnees des poissons et des requins
ma_planete.coordoonees_poissons_requins()

ma_planete.deplacer_poissons()
ma_planete.affichage()