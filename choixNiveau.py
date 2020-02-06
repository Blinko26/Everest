def choixNiveau(windows):
    import pygame
    pygame.init()
    pygame.mixer.init()

    from main import niveau1
    from Platformer import niveau2
    background = pygame.image.load('sprite/spriteMenu/backgroundmenu.png')
    background = pygame.transform.scale(background, (1024, 768))

    #choix niveau
    demo = pygame.image.load('sprite/spriteMenu/demo.png')
    demo = pygame.transform.scale(demo, (326, 71))

    niveau1bouton = pygame.image.load('sprite/spriteMenu/niveau1.png')
    niveau1bouton = pygame.transform.scale(niveau1bouton, (326, 71))

    niveau2bouton = pygame.image.load('sprite/spriteMenu/niveau2.png')
    niveau2bouton = pygame.transform.scale(niveau2bouton, (326, 71))

    niveau3bouton = pygame.image.load('sprite/spriteMenu/niveau3.png')
    niveau3bouton = pygame.transform.scale(niveau3bouton, (326, 71))

    retour = pygame.image.load('sprite/spriteMenu/retour.png')
    retour = pygame.transform.scale(retour, (326, 71))

    selection = pygame.image.load('sprite/spriteMenu/selection.png')
    selection = pygame.transform.scale(selection, (41, 71))

    ChoixDuniveau = pygame.image.load('sprite/spriteMenu/Choix.png')
    ChoixDuniveau = pygame.transform.scale(ChoixDuniveau, (652, 142))

    selector = 1

    def drawChoixNiveau():
        windows.blit(background, (0, 0))
        windows.blit(ChoixDuniveau, (180, 55))

        windows.blit(demo,(349,280))
        windows.blit(niveau1bouton, (349, 380))
        windows.blit(niveau2bouton, (349, 480))
        windows.blit(niveau3bouton, (349, 580))
        windows.blit(retour, (349, 680))
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
                    if selector == 1:
                        pygame.mixer.music.stop()
                        pygame.mixer.music.set_volume(0.25)
                        pygame.mixer.music.load('Sounds/AHJ.ogg')
                        pygame.mixer.music.play()
                        niveau1()
                    if selector == 2:
                        pygame.mixer.music.stop()
                        pygame.mixer.music.set_volume(0.25)
                        pygame.mixer.music.load('Sounds/AHJ.ogg')
                        pygame.mixer.music.play()
                        niveau2(windows,'1')
                    if selector == 3:
                        pygame.mixer.music.stop()
                        pygame.mixer.music.set_volume(0.25)
                        pygame.mixer.music.load('Sounds/AHJ.ogg')
                        pygame.mixer.music.play()
                        niveau2(windows,'2')
                    if selector == 4:
                        niveau2(windows,'3')
                    if selector == 5:
                        pygame.mixer.music.stop()
                        runChoix = False
                if event.key == pygame.K_DOWN:
                    if selector != 5:
                        selector += 1
                if event.key == pygame.K_UP:
                    if selector != 1:
                        selector -= 1
            drawChoixNiveau()
