import pygame

from choixNiveau import choixNiveau
pygame.init()
pygame.mixer.init()

height = 768
width = 1024

windows = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()
run = True
background = pygame.image.load('sprite/spriteMenu/backgroundmenu.png')
background = pygame.transform.scale(background, (1024, 768))

pygame.mixer.music.load("Sounds/CelestialEntities.ogg")
pygame.mixer.music.play(loops=1)

boutonVide = pygame.image.load('sprite/spriteMenu/bouton-01.png')
boutonVide = pygame.transform.scale(boutonVide, (652, 142))

creditBackground = pygame.image.load('sprite/spriteMenu/creditsBackground.png')

titre1 = pygame.image.load('sprite/spriteMenu/RIA.png')
titre2 = pygame.image.load('sprite/spriteMenu/titre2.png')

jouer = pygame.image.load('sprite/spriteMenu/jouer.png')
jouer = pygame.transform.scale(jouer, (326, 71))
credits = pygame.image.load('sprite/spriteMenu/credits.png')
credits = pygame.transform.scale(credits, (326, 71))
quitter = pygame.image.load('sprite/spriteMenu/quitter.png')
quitter = pygame.transform.scale(quitter, (326, 71))
selection = pygame.image.load('sprite/spriteMenu/selection.png')
selection = pygame.transform.scale(selection, (41, 71))



selector = 1

choixNiveauB = False

placement = 280

def drawMenu():
    windows.blit(background, (0,0))
    #titre
    windows.blit(boutonVide, (180, 55))
    windows.blit(titre1,(221,80))
    windows.blit(titre2, (420, 85))
    #fin titre
    windows.blit(jouer, (349, 280))
    windows.blit(credits, (349, 380))
    windows.blit(quitter, (349, 480))

    if selector == 1:
        placement = 280
    elif selector == 2:
        placement = 380
    else:
        placement = 480

    windows.blit(selection, (300,placement))

    pygame.display.update()

def drawCredits():
    windows.blit(creditBackground, (0,0))
    windows.blit(boutonVide, (180, 55))
    windows.blit(titre1, (221, 80))
    windows.blit(titre2, (420, 85))
    pygame.display.update()
    exit = False
    while not(exit):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit = True




while run:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                if selector == 1:
                    choixNiveau(windows)
                if selector == 2:
                    drawCredits()
                if selector == 3:
                    pygame.mixer.music.stop()
                    run = False
            if event.key == pygame.K_DOWN:
                if selector != 3:
                    selector += 1
            if event.key == pygame.K_UP:
                if selector != 1:
                    selector -= 1
        drawMenu()

pygame.quit()