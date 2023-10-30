import pygame
from env_world import Planete, ma_planete

pygame.init()

# crée une instance de la classe Planete
ma_planete = Planete(0,0)

# taille de la fenêtre
largeur_fenetre = 800
hauteur_fenetre = 600

fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
fond = pygame.image.load("image/background_wator.png").convert()
pygame.display.set_caption("Simulation Wa-Tor")

# Défini la couleur de fond
couleur_fond = (0,0,0)

# Boucle principal de dessin
en_cours = True
while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False

    # Calcul la taille des cellules en fonction de la taille de la fenetre et du monde
    cell_size = min(largeur_fenetre // largeur, hauteur_fenetre // longueur)

    # Efface l'écran avec la couleur de fond
    fenetre.fill(couleur_fond)


    ma_planete.deplacer_poissons()
    ma_planete.deplacer_requins

    # Dessine le monde
    for y in range(len(ma_planete.monde)):
        for x in range(len(ma_planete.monde[y])):
            cellule = ma_planete.monde[y][x]
            
            # Dessine la cellule en fonction de son contenu
            if cellule == '\U0001f4a7':  # Eau
                pygame.draw.rect(fenetre, (0, 0, 255), (x * cell_size, y * cell_size, cell_size, cell_size))
            elif cellule == '\U0001f41f':  # Poisson
                pygame.draw.rect(fenetre, (0, 255, 0), (x * cell_size, y * cell_size, cell_size, cell_size))
            elif cellule == '\U0001f988':  # Requin
                pygame.draw.rect(fenetre, (255, 0, 0), (x * cell_size, y * cell_size, cell_size, cell_size))


    pygame.display.flip() # Dessine le monde en fonction des données mises à jour

    pygame.quit()