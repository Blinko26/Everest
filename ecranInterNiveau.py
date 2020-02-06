def ecranInterNiveau(windows, clock):
    import pygame
    pygame.init()
    pygame.mixer.init()

    clock = pygame.time.Clock()
    run = True
    from main import niveau1
    from Platformer import niveau2
    background = pygame.image.load('sprite/spriteMenu/backgroundmenu.png')
    background = pygame.transform.scale(background, (1024, 768))

    #choix niveau
    jouer = pygame.image.load('sprite/spriteMenu/jouer.png')
    jouer = pygame.transform.scale(jouer, (326, 71))

    retour = pygame.image.load('sprite/spriteMenu/retour.png')
    retour = pygame.transform.scale(retour, (326, 71))

    selection = pygame.image.load('sprite/spriteMenu/selection.png')
    selection = pygame.transform.scale(selection, (41, 71))

    selector = 1
    placement = 280

    def drawecranInterNiveau():
        windows.blit(background, (0, 0))
        if selector == 1:
            placement = 280
        elif selector == 2:
            placement = 380
        elif selector == 3:
            placement = 480
        elif selector == 4:
            placement = 580
        else:
            placement = 680

        windows.blit(selection, (300,placement))
        pygame.display.update()


    runChoix = True
    while runChoix:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('quit')
                pygame.mixer.music.stop()
                runChoix = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    print('space')
                    print(selector)
                    if selector == 1:
                        niveau1()
                    if selector == 2:
                        niveau2(windows,'1')
                    if selector == 3:
                        niveau2(windows,'2')
                    if selector == 4:
                        niveau2(windows,'3')
                    if selector == 5:
                        pygame.mixer.music.stop()
                        runChoix = False
                if event.key == pygame.K_DOWN:
                    print('down')
                    if selector != 5:
                        selector += 1
                if event.key == pygame.K_UP:
                    print('up')
                    if selector != 1:
                        selector -= 1
            drawecranInterNiveau()
