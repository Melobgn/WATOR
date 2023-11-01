import pygame
from simulation import Monde, Poisson, Requin

# Initialisation de Pygame
pygame.init()

# Création de la fenêtre
mon_monde = Monde(12, 12, 50)  # Ajustez les dimensions du monde ici
longueur = mon_monde.longueur * mon_monde.taille_cellule
hauteur = mon_monde.hauteur * mon_monde.taille_cellule

ecran = pygame.display.set_mode((longueur, hauteur + 80))  # Augmentez la hauteur pour accueillir le texte
pygame.display.set_caption("Projet Wa-tor")

# Chargement des images
image_poisson = pygame.image.load("fish.png").convert_alpha()
image_requin = pygame.image.load("shark.png").convert_alpha()


# Redimensionnement des images
image_poisson = pygame.transform.scale(image_poisson, (mon_monde.taille_cellule, mon_monde.taille_cellule))
image_requin = pygame.transform.scale(image_requin, (mon_monde.taille_cellule, mon_monde.taille_cellule))


# Couleur du fond
couleur_fond = (0, 127, 255)

mon_monde.peupler_le_monde(20, 4)

poisson = Poisson(mon_monde)  
requin = Requin(mon_monde)    

# Boucle principale
running = True
chronons = 0

font = pygame.font.Font(None, 25)  # Police et taille du texte
texte_chronons = font.render(f"Chronons: {chronons}", True, (0, 0, 0))
texte_requins = font.render(f"Requins: {len(mon_monde.requins)}", True, (0, 0, 0))
texte_poissons = font.render(f"Poissons: {len(mon_monde.poissons)}", True, (0, 0, 0))



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Quitte le jeu lorsque la fenêtre est fermée

    ecran.fill((255,255,255))  

    # Déplacement des poissons
    poisson.se_deplacer()

    # Déplacement des requins
    requin.se_deplacer()

    # Starvation des requins
    requin.starvation()

    # Manger des poissons
    requin.manger_poisson()

    # Parcours de la grille et affichage de chaque cellule
    for i in range(mon_monde.hauteur):
        for j in range(mon_monde.longueur):
            cellule = mon_monde.get_cell(j, i)
            x = j * mon_monde.taille_cellule
            y = i * mon_monde.taille_cellule

            # Dessin d'une ligne autour de la cellule
            pygame.draw.rect(ecran, couleur_fond, (x, y, mon_monde.taille_cellule, mon_monde.taille_cellule))

            # Affichage des images de poisson, requin et de la mer
            if cellule == '\U0001f41f':
                ecran.blit(image_poisson, (x, y))
            elif cellule == '\U0001f988':
                ecran.blit(image_requin, (x, y))

    # Affichage des informations en temps réel
    texte_chronons = font.render(f"Chronons: {chronons}", True, (0, 0, 0))
    texte_requins = font.render(f"Requins: {len(mon_monde.requins)}", True, (0, 0, 0))
    texte_poissons = font.render(f"Poissons: {len(mon_monde.poissons)}", True, (0, 0, 0))

    # Affichage du texte
    ecran.blit(texte_chronons, (10, hauteur + 10))
    ecran.blit(texte_requins, (10, hauteur + 40))
    ecran.blit(texte_poissons, (10, hauteur + 60))

    # Mise à jour de l'affichage
    pygame.display.flip()

    # Incrémentation des chronons
    chronons += 1
    pygame.time.delay(800)  # Ajout d'un délai de 800 ms (0.8 seconde) entre les chronons

# Sortie propre
pygame.quit()