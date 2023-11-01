import pygame

pygame.init()

ecran = pygame.display.set_mode((300,200))
pygame.display.set_caption("Projet Wa-tor")
blanc = (255, 255, 255)
ecran.fill(blanc)

# charge les images
image_poisson = pygame.image.load("poisson_vector.png").convert_alpha()
image_requin = pygame.image.load("requins_vector.png").convert_alpha()

# redimensionne les images
nouvelle_largeur = 70
nouvelle_hauteur = 70

image_poisson = pygame.transform.scale(image_poisson, (nouvelle_largeur, nouvelle_hauteur))
image_requin = pygame.transform.scale(image_requin, (nouvelle_largeur, nouvelle_hauteur))

continuer = True

while continuer:
    ecran.blit(image_poisson, (0, 50))
    ecran.blit(image_requin, (100, 100))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            continuer = False

    pygame.display.flip()

pygame.quit()