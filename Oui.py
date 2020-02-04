import pygame

pygame.init()

display_width = 1024
display_height = 728

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Un beau jeu')
clock = pygame.time.Clock()


bonhommeImg = [pygame.image.load('sprite/petitTrollDroit.png'), pygame.image.load('sprite/petitTrollGauche.png')]
dashImg = pygame.image.load('sprite/dashSprite.png')

bgfill = [white, black, red]

x = (display_width * 0.45)
y = (display_height * 0.8)

x_change = 0
y_change = 0

Droit = True
Gauche = False
Haut = False
Bas = False

countDash = 0
dashValue = 200

running = True
lvl = 0

while running:

    clock.tick(60)

    pygame.display.flip()

    #gameDisplay.blit(bg[lvl], (0,0))

    gameDisplay.fill(bgfill[lvl])

    while countDash != 0:
        if Haut:
            dashImg = pygame.transform.rotate(dashImg, -90)
            gameDisplay.blit(dashImg, (x + 10, y+dashValue-(dashValue/countDash)))
            dashImg = pygame.transform.rotate(dashImg, 90)
        elif Bas:
            dashImg = pygame.transform.rotate(dashImg, 90)
            gameDisplay.blit(dashImg, (x + 10, y-dashValue+(dashValue/countDash)))
            dashImg = pygame.transform.rotate(dashImg, -90)
        elif Droit:
            dashImg = pygame.transform.rotate(dashImg, 180)
            gameDisplay.blit(dashImg, (x-dashValue+(dashValue/countDash), y+10))
            dashImg = pygame.transform.rotate(dashImg, 180)
        else:
            gameDisplay.blit(dashImg, (x+dashValue-(dashValue/countDash), y+10))
        countDash += 1
        if countDash >= 8000:
            countDash = 0

    #Si le personnage atteint le bout de la fenêtre
    if x > 990:
        if lvl != len(bgfill)-1:
            x = -20
        else:
            x=989
        if lvl < len(bgfill)-1:
            lvl += 1
    elif y > 700:
        y = 699
    elif x < -21:
        if lvl != 0:
            x = 989
        else:
            x = -20
        if lvl > 0:
            lvl -= 1
    elif y < -1:
        y = 0

    #Déplacement
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_q:
                x_change = -5
                gameDisplay.blit(bonhommeImg[1], (x, y))
                Droit = False
                Haut = False
                Bas = False
                Gauche = True
                pygame.display.update()
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                x_change = 5
                gameDisplay.blit(bonhommeImg[0], (x, y))
                Droit = True
                Bas = False
                Haut = False
                Gauche = False
                pygame.display.update()
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                y_change = 5
                Bas = True
                Haut = False
            elif event.key == pygame.K_UP or event.key == pygame.K_z:
                y_change = -5
                Haut = True
                Bas = False
            elif event.key == pygame.K_SPACE:
                if Haut:
                    countDash = 1
                    dashImg = pygame.transform.rotate(dashImg, -90)
                    gameDisplay.blit(dashImg, (x+10, y))
                    dashImg = pygame.transform.rotate(dashImg, 90)
                    y -= dashValue
                elif Bas:
                    countDash = 1
                    dashImg = pygame.transform.rotate(dashImg, 90)
                    gameDisplay.blit(dashImg, (x+10, y))
                    dashImg = pygame.transform.rotate(dashImg, -90)
                    y += dashValue
                else:
                    if Droit:
                        countDash = 1
                        dashImg = pygame.transform.rotate(dashImg, 180)
                        gameDisplay.blit(dashImg, (x + 10, y + 10))
                        dashImg = pygame.transform.rotate(dashImg, 180)
                        x += dashValue
                    else:
                        countDash = 1
                        gameDisplay.blit(dashImg, (x + 10, y + 10))
                        x -= dashValue

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_q or event.key == pygame.K_d:
                x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_z or event.key == pygame.K_s:
                y_change = 0

    x += x_change
    y += y_change

    if Droit == True:
        gameDisplay.blit(bonhommeImg[0], (x, y))
    elif Gauche == True:
        gameDisplay.blit(bonhommeImg[1], (x, y))

