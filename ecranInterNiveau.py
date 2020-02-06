def ecranInterNiveau(windows, time, nbNiveau):
    import pygame
    pygame.init()
    pygame.mixer.init()

    from main import niveau1
    from Platformer import niveau2
    background = pygame.image.load('sprite/spriteMenu/backgroundmenu.png')
    background = pygame.transform.scale(background, (1024, 768))

    #choix niveau
    retour = pygame.image.load('sprite/spriteMenu/retour.png')
    retour = pygame.transform.scale(retour, (326, 71))

    titreVictoire = pygame.image.load('sprite/spriteMenu/victoire.png')

    selection = pygame.image.load('sprite/spriteMenu/selection.png')
    selection = pygame.transform.scale(selection, (41, 71))

    selector = 1
    placement = 280
    font = pygame.font.SysFont("comicsans", 60, True)
    temps = font.render("Temps : " + str(time/1000) + " s", 1, (0, 0, 0))

    def getHighScore():
        f = open('highScore/highScore' + nbNiveau + '.txt', 'r')
        data = f.read()
        f.close()
        data = data.split('\n')
        highScore = int(data[0])
        for score in data:
            if int(score) < highScore:
                highScore = int(score)
        return highScore

    meilleurTemps = font.render("HighScore : " + str(int(getHighScore()) / 1000) + " s", 1, (0, 0, 0))

    def drawecranInterNiveau():
        windows.blit(background, (0, 0))
        windows.blit(titreVictoire, (349, 80))
        windows.blit(retour,(349, 580))
        windows.blit(temps, (349, 280))

        windows.blit(meilleurTemps, (349, 380))
        placement = 580
        windows.blit(selection, (300,placement))
        pygame.display.update()


    runChoix = True
    while runChoix:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                runChoix = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    if selector == 1:
                        pygame.mixer.music.stop()
                        runChoix = False
            drawecranInterNiveau()
