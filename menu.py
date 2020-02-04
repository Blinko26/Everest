import pygame
from main import niveau1
pygame.init()

height = 768
width = 1024

windows = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()
run = True
background = pygame.image.load('sprite/spriteMenu/backgroundmenu.png')
background = pygame.transform.scale(background, (1024, 768))

creditBackground = pygame.image.load('sprite/spriteMenu/creditsBackground.png')

titre = pygame.image.load('sprite/spriteMenu/titre.png')
jouer = pygame.image.load('sprite/spriteMenu/jouer.png')
jouer = pygame.transform.scale(jouer, (326, 71))
credits = pygame.image.load('sprite/spriteMenu/credits.png')
credits = pygame.transform.scale(credits, (326, 71))
quitter = pygame.image.load('sprite/spriteMenu/quitter.png')
quitter = pygame.transform.scale(quitter, (326, 71))
selection = pygame.image.load('sprite/spriteMenu/selection.png')
selection = pygame.transform.scale(selection, (41, 71))

selector = 1
placement = 280

def drawMenu():
    windows.blit(background, (0,0))
    windows.blit(titre,(186,80))
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
    pygame.display.update()
    exit = False
    while not(exit):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('quit')
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit = True

while run:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('quit')
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                print('space')
                print(selector)
                if selector == 1:
                    niveau1()
                if selector == 2:
                    drawCredits()
                if selector == 3:
                    run = False
            if event.key == pygame.K_DOWN:
                print('down')
                if selector != 3:
                    selector += 1
            if event.key == pygame.K_UP:
                print('up')
                if selector != 1:
                    selector -= 1
    drawMenu()

pygame.quit()