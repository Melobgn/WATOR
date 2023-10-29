import pygame
from env_world import Planete

pygame.init()

nombre_poissons = 10
nombre_requins = 1
chronon_en_cours = 0
ma_planete = Planete(20, 18, nombre_poissons, nombre_requins)
ma_planete.creation_monde()

# Taille de la fenêtre
largeur_fenetre = 800
hauteur_fenetre = 600
texte_position = (10, hauteur_fenetre + 10)  # Position du texte sous la fenêtre de dessin

fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre + 50))  # Ajoutez 50 pixels pour le texte
fond = pygame.image.load("image/background_wator.png").convert()
pygame.display.set_caption("Simulation Wa-Tor")

# Défini la couleur de fond
couleur_fond = (0, 0, 0)

# Créez une police pour le texte
police = pygame.font.Font(None, 36)

# Boucle principal de dessin
en_cours = True
while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False

    # Calcul la taille des cellules en fonction de la taille de la fenêtre et du monde
    cell_size = min(largeur_fenetre // ma_planete.largeur, hauteur_fenetre // ma_planete.longueur)

    # Efface l'écran avec la couleur de fond
    fenetre.fill(couleur_fond)

    ma_planete.deplacer_poissons()
    ma_planete.deplacer_requins()

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

    # Créez une surface pour afficher le texte
    
    texte_surface = police.render("Chronons en cours: 0", True, (255, 255, 255))
    fenetre.blit(texte_surface, texte_position)
    chronon_en_cours += 1
    pygame.display.flip()

pygame.quit()
