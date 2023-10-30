import random
import time
import os


class Planete:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.monde = []  # Initialiser la variable "monde"
    
    # fonction pour créer le monde de départ
    def creation_monde(self, longueur, largeur, nombre_poissons, nombre_requins):
        self.longueur = longueur
        self.largeur = largeur
        self.nombre_poissons = nombre_poissons
        self.nombre_requins = nombre_requins
        monde = [['\U0001f4a7' for i in range(largeur)] for y in range(longueur)]  # Créer une grille 2D pour le monde
        random.seed(12)
        

        self.poissons = []  # Liste pour stocker les poissons
        self.requins = []   # Liste pour stocker les requins

        # Place les poissons dans la grille
        for poisson in range(nombre_poissons):
            if not coordonnees_possibles:
                break  # Si on a utilisé toutes les coordonnées possibles, sortir de la boucle
            row, col = coordonnees_possibles.pop()
            monde[row][col] = '\U0001f41f'
            self.poissons.append({'row': row, 'col': col})

        # Place les requins dans la grille
        for requin in range(nombre_requins):
            if not coordonnees_possibles:
                break  # Si on a utilisé toutes les coordonnées possibles, sortir de la boucle
            row, col = coordonnees_possibles.pop()
            monde[row][col] = '\U0001f988'
            self.requins.append({'row': row, 'col': col})

        self.monde = monde  # Mets à jour la variable de la planète avec le monde créé
        
        return monde

    def coordoonees_poissons_requins(self):
        # Affiche les coordonnées des poissons
        for poisson in self.poissons:
            print(f"Coordonnées du poisson : ({poisson['row']}, {poisson['col']})")

        # Affiche les coordonnées des requins
        for requin in self.requins:
            print(f"Coordonnées du requin : ({requin['row'], requin['col']})")

    #affiche le monde
    


    def directions(self):
        deplacement_possible = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        poissons_survivants = []  # Nouvelle liste pour les poissons qui ont survécu

        for poisson in self.poissons:
            directions_possibles = deplacement_possible[:]
            random.shuffle(directions_possibles)

            poisson_mange = False

            # Vérifie d'abord si un requin est à proximité
            for direction in directions_possibles:
                new_row = poisson['row'] + direction[0]
                new_col = poisson['col'] + direction[1]

                for requin in self.requins:
                    if abs(new_row - requin['row']) <= 1 and abs(new_col - requin['col']) <= 1:
                        self.monde[poisson['row']][poisson['col']] = '\U0001f4a7'  # le poisson est mangé
                        poisson_mange = True
                        break

                if poisson_mange:
                    break

            if not poisson_mange:
                poissons_survivants.append(poisson)

        # Ne tente de supprimer les poissons que s'ils ont été mangés
        if poisson_mange:
            self.poissons.remove(poisson)

        self.poissons = poissons_survivants  # Mettre à jour la liste des poissons survivants

        # Maintenant, effectuez le déplacement pour les poissons survivants
        for poisson in poissons_survivants:
            directions_possibles = deplacement_possible[:]
            random.shuffle(directions_possibles)

            for direction in directions_possibles:
                new_row = poisson['row'] + direction[0]
                new_col = poisson['col'] + direction[1]

                if 0 <= new_row < self.longueur and 0 <= new_col < self.largeur:
                    if self.monde[new_row][new_col] == '\U0001f4a7':  # eau
                        self.monde[poisson['row']][poisson['col']] = '\U0001f4a7'  # eau
                        self.monde[new_row][new_col] = '\U0001f41f'  # poisson
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
                    if self.monde[new_row][new_col] == '\U0001f41f':  # poisson
                        self.monde[requin['row']][requin['col']] = '\U0001f4a7'  # eau
                        self.monde[new_row][new_col] = '\U0001f988'  # requin
                        requin['row'] = new_row
                        requin['col'] = new_col
                        deplacement_reussi = True
                    elif self.monde[new_row][new_col] == '\U0001f4a7':  # eau
                        self.monde[requin['row']][requin['col']] = '\U0001f4a7'  # eau
                        self.monde[new_row][new_col] = '\U0001f988'  # requin
                        requin['row'] = new_row
                        requin['col'] = new_col
                        deplacement_reussi = True
                    if deplacement_reussi:
                        break

        return self.monde


  


# Initialisation des valeurs
longueur = 10
largeur = 8
nombre_poissons = 10
nombre_requins = 2
chronons = 0

# création de l'instance de la classe Planete
ma_planete = Planete(0, 0)

# initialisation du monde
ma_planete.creation_monde(longueur, largeur, nombre_poissons, nombre_requins)


# affichage du monde
ma_planete.affichage()

# boucle temporel des chronons
while chronons < 100:
    os.system('clear')
    ma_planete.deplacer_poissons()
    ma_planete.deplacer_requins()
    ma_planete.affichage()

# Affiche le chronon, le nombre de requins, le nombre initial de poissons et le nombre de poissons survivants
    poissons_survivants = len(ma_planete.poissons)
    print(f"Chronons en cours : {chronons}\nRequins : {nombre_requins}\nNombre initial de poissons : {nombre_poissons}\nPoissons survivants : {poissons_survivants}")

          
    print()
    chronons += 1
    time.sleep(0.8)