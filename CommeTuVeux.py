import pygame

pygame.init()


(width, height) = (1024, 768)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Test Fenetre")

running = True

while running:

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

