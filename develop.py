import random
import os
import time


class Monde:
    def __init__(self):
        
        self.poissons = []
        self.requins = []
        

    def creer_le_monde(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
        self.monde = [['\U0001f4a7' for i in range(largeur)] for y in range(longueur)]
        return self.monde
        

    def affichage_monde(self):
        for i in self.monde:
            print(*i)
    

    def jouer_un_tour(self):
        while chronons < 100:
            os.system('clear')
            chronons += 1
            self.time.sleep= time.sleep()


    def peupler_le_monde(self, nb_poissons, nb_requins):
        self.nb_poissons = nb_poissons
        self.nb_requins = nb_requins
        random.seed(12)
        coordonnees_possibles = [(x, y) for x in range(self.longueur) for y in range(self.largeur)]
        random.shuffle(coordonnees_possibles)
        
        # Place les poissons dans la grille
        for poisson in range(self.nb_poissons):
            if not coordonnees_possibles:
                break  # Si on a utilisé toutes les coordonnées possibles, sortir de la boucle
            row, col = coordonnees_possibles.pop()
            self.monde[row][col] = '\U0001f41f'
            self.poissons.append({'row': row, 'col': col})
        
        # Place les requins dans la grille
        for requin in range(self.nb_requins):
            if not coordonnees_possibles:
                break  # Si on a utilisé toutes les coordonnées possibles, sortir de la boucle
            row, col = coordonnees_possibles.pop()
            self.monde[row][col] = '\U0001f988'
            self.requins.append({'row': row, 'col': col})


class Poisson(Monde):
    def __init__(self, compteur_reproduction, temps_de_reproduction, x, y):
        self.compteur_reproduction = compteur_reproduction
        self.temps_de_reproduction = temps_de_reproduction
        self.x = x
        self.y = y

    
    def cases_vides_adjacentes(self,grille):
        self.grille = grille


    def faire_un_tour(self, grille):
        self.grille = grille
        pass

    def se_deplacer(self):
        # permet d'indiquer comment les poissons se déplacent : (0, 1) = bas, (1, 0) = droite, (0, -1) = haut, (-1, 0) = à gauche
        deplacement_possible = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for poisson in self.poissons: # permet à chaque élément 'poisson' de 'poissons = []' de se déplacer sur un position au hasard
            directions_possibles = deplacement_possible[:]
            random.shuffle(directions_possibles)

            deplacement_reussi = False

            for direction in directions_possibles: # pour chaque direction dans 'directions_possibles'
                new_row = poisson['row'] + direction[0]
                new_col = poisson['col'] + direction[1]
                if 0 <= new_row < self.longueur and 0 <= new_col < self.largeur:
                    if self.monde[new_row][new_col] == '\U0001f4a7':
                        self.monde[poisson['row']][poisson['col']] = '\U0001f4a7'
                        self.monde[new_row][new_col] = '\U0001f41f'
                        poisson['row'] = new_row
                        poisson['col'] = new_col
                        deplacement_reussi = True
                        break

            if not deplacement_reussi:
                return self.monde
            

    def se_reproduire(self, grille, animal, y_target:int, x_target:int):
        self.grille = grille
        self.animal = animal
        self.y_target = y_target
        self.x_target = x_target
        pass


class Requin(Poisson):
    def __init__(self, compteur_reproduction, temps_de_reproduction, x, y, energie) -> None:
        super().__init__(compteur_reproduction, temps_de_reproduction, x, y)
        self.energie = energie

    def cases_poissons_adjacentes(self, monde):
        self.monde = monde
        pass

    def cases_vides_ou_cases_poissons(self, monde):
        self.monde = monde
        pass

    def faire_un_tour(self,monde):
        self.monde = monde
        pass

    def se_deplacer(self, monde, actions_possibles):
        self.monde = monde
        self.action_possibles = actions_possibles
        pass

mon_monde = Monde()
mon_monde.creer_le_monde(10,8)
mon_monde.peupler_le_monde(10,2)
print(mon_monde.affichage_monde())

