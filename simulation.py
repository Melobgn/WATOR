import random
import pygame
import matplotlib.pyplot as plt



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
        poisson_bebe = Poisson(self.monde, self.x, self.y)
        self.monde.poissons.append(poisson_bebe)
        self.monde.grille[self.x][self.y] = '\U0001f41f'
            

class Requin(Poisson):
    def __init__(self, monde, x, y):
        super().__init__(monde, x, y)
        self.energie = 6
        self.temps_de_reproduction = 11
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
                self.energie += 4
                self.monde.poissons.remove(poiscaille)

    def reproduction_requin(self):
        requin_bebe = Requin(self.monde, self.x, self.y)
        self.monde.requins.append(requin_bebe)
        self.monde.grille[self.x][self.y] = '\U0001f988'
 
class Simulation:
    def __init__(self, longueur, hauteur, nb_poissons, nb_requins, delai_chronon, taille_cellule):
        self.monde = Monde(longueur, hauteur)
        self.chronons = 0
        self.duree_chronon = delai_chronon
        self.en_cours = True
        self.nb_poissons = nb_poissons
        self.nb_requins = nb_requins
        self.taille_cellule = taille_cellule  # Nouvel attribut pour la taille des cellules

        # Initialisation des données pour le graphique
        self.temps = [0]
        self.nb_poissons_data = [self.nb_poissons]
        self.nb_requins_data = [self.nb_requins]

    def initialiser(self):
        # Initialisation de Pygame
        pygame.init()
        longueur = self.monde.longueur * self.taille_cellule  # Calcul de la taille de l'écran en fonction des cellules
        hauteur = self.monde.hauteur * self.taille_cellule  # Calcul de la taille de l'écran en fonction des cellules
        ecran = pygame.display.set_mode((longueur, hauteur + 80))
        pygame.display.set_caption("Projet Wa_tor")

        # Chargement des images
        image_poisson = pygame.image.load("fish.png").convert_alpha()
        image_requin = pygame.image.load("shark.png").convert_alpha()

        # Redimensionnement des images en fonction de la taille de la cellule
        image_poisson = pygame.transform.scale(image_poisson, (self.taille_cellule, self.taille_cellule))
        image_requin = pygame.transform.scale(image_requin, (self.taille_cellule, self.taille_cellule))
        couleur_fond = (0, 127, 255)
        self.monde.peupler_le_monde(self.nb_poissons, self.nb_requins)

        running = True
        font = pygame.font.Font(None, 25)

        # Initialisation du graphique
        plt.ion()
        fig, ax = plt.subplots()
        ax.set_title("Évolution du nombre de poissons et de requins")
        ax.set_xlabel("Temps")
        ax.set_ylabel("Nombre")

        poissons_line, = ax.plot(self.temps, self.nb_poissons_data, label="Poissons")
        requins_line, = ax.plot(self.temps, self.nb_requins_data, label="Requins")

        ax.legend(loc="upper left")

        plt.show()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminer_simulation()
            ecran.fill((255, 255, 255))

            # Appel des méthodes de déplacement et d'interaction des poissons et requins
            for poiscaille in self.monde.poissons:
                poiscaille.deplacer_poisson()
            for requinx in self.monde.requins:
                requinx.deplacer_requin()
                requinx.starvation()
                requinx.manger_poisson()

            # Dessin des cellules
            for i in range(self.monde.hauteur):
                for j in range(self.monde.longueur):
                    cellule = self.monde.grille[i][j]
                    x = j * self.taille_cellule
                    y = i * self.taille_cellule
                    pygame.draw.rect(ecran, couleur_fond, (x, y, self.taille_cellule, self.taille_cellule))
                    if cellule == '\U0001f41f':
                        ecran.blit(image_poisson, (x, y))
                    elif cellule == '\U0001f988':
                        ecran.blit(image_requin, (x, y))

            # Affichage des informations
            texte_chronons = font.render(f"Chronons: {self.chronons}", True, (0, 0, 0))
            texte_requins = font.render(f"Requins: {len(self.monde.requins)}", True, (0, 0, 0))
            texte_poissons = font.render(f"Poissons: {len(self.monde.poissons)}", True, (0, 0, 0))
            ecran.blit(texte_chronons, (10, hauteur + 10))
            ecran.blit(texte_requins, (10, hauteur + 40))
            ecran.blit(texte_poissons, (10, hauteur + 60))
            pygame.display.flip()
            self.chronons += 1
            pygame.time.delay(self.duree_chronon)

            # Mise à jour des données du graphique
            self.temps.append(self.chronons)
            self.nb_poissons_data.append(len(self.monde.poissons))
            self.nb_requins_data.append(len(self.monde.requins))

            # Mise à jour du graphique en temps réel
            poissons_line.set_data(self.temps, self.nb_poissons_data)
            requins_line.set_data(self.temps, self.nb_requins_data)

            ax.relim()
            ax.autoscale_view()

            plt.pause(0.01)
            plt.draw()

            pygame.display.flip()
            self.chronons += 1
            pygame.time.delay(self.duree_chronon)

    def gerer_evenements(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.terminer_simulation()

    def mise_a_jour(self):
        self.poisson.se_deplacer()
        self.requin.starvation()
        self.requin.se_deplacer()
        self.requin.manger_poisson()
        self.chronons += 1
        pygame.time.delay(self.duree_chronon)

    def afficher(self):
        pass

    def en_cours(self):
        return self.en_cours

    def terminer_simulation(self):
        self.en_cours = False
        pygame.quit()


   