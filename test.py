import random
import time

class Planete:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.monde = []
          
          
    def afficher_le_monde(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
        self.monde = [['\U0001f4a7' for i in range(largeur)] for y in range(longueur)]  # Créer une grille 2D pour le monde
        random.seed(12)
        coordonnees_possibles = [(x, y) for x in range(longueur) for y in range(largeur)]
        random.shuffle(coordonnees_possibles)

    def definir_le_temps(self, sleep_time):
        self.sleep_time = sleep_time
        pass


    def ajouter_poissons(self, nombre_poissons):
        self.nombre_poissons = nombre_poissons
        self.poissons = []  # Liste pour stocker les poissons

        for poisson in range(self, nombre_poissons):
            if not coordonnees_possibles:
                break  # Si on a utilisé toutes les coordonnées possibles, sortir de la boucle
            row, col = coordonnees_possibles.pop()
            monde[row][col] = '\U0001f41f'
            self.poissons.append({'row': row, 'col': col})


    def ajouter_requins(self, nombre_requins):
        self.nombre_requins = nombre_requins
        self.requins = []   # Liste pour stocker les requins
        
        for requin in range(nombre_requins):
            if not coordonnees_possibles:
                break  # Si on a utilisé toutes les coordonnées possibles, sortir de la boucle
            row, col = coordonnees_possibles.pop()
            monde[row][col] = '\U0001f988'
            self.requins.append({'row': row, 'col': col})

        self.monde = monde  # Mets à jour la variable de la planète avec le monde créé
        
        return monde


    def jouer_un_tour(self):
        pass


    def peupler_le_monde(self):
        pass


# création de l'instance de la classe Planete
ma_planete = Planete(0, 0)

# Initialisation des valeurs
# méthode afficher le monde :
my_map = Planete.afficher_le_monde(10, 8, 3)
# méthode ajouter nombres_poissons/requins :
nombre_poissons = Planete.ajouter_poissons(10)
nombre_requins = Planete.ajouter_requins(5)
# méthode définir temps :
timing = Planete.definir_le_temps(3) # = 3sec
chronons = 0


