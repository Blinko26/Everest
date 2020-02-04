import pygame

pygame.init()

height = 768
width = 1024

windows = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()
run = True
background = pygame.image.load('sprite/spriteMenu/backgroundmenu.png')
background = pygame.transform.scale(background, (1024, 768))

titre = pygame.image.load('sprite/spriteMenu/titre.png')
jouer = pygame.image.load('sprite/spriteMenu/jouer.png')
jouer = pygame.transform.scale(jouer, (326, 71))
credits = pygame.image.load('sprite/spriteMenu/credits.png')
credits = pygame.transform.scale(credits, (326, 71))
quitter = pygame.image.load('sprite/spriteMenu/quitter.png')
quitter = pygame.transform.scale(quitter, (326, 71))

def drawMenu():
    windows.blit(background, (0,0))
    windows.blit(titre,(186,80))
    windows.blit(jouer, (349, 280))
    windows.blit(credits, (349, 380))
    windows.blit(quitter, (349, 480))

    pygame.display.update()

while run:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.K_DOWN:
            print('down')
        if event.type == pygame.K_UP:
            print('up')

    drawMenu()

pygame.quit()