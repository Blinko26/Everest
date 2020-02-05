def niveau1():
    import pygame

    pygame.init()

    from player import Player
    from projectile import projectile
    from enemy import enemy
    from protection import Protection
    windows = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption("DASHLAND")

    background = pygame.image.load('sprite/background.png')
    background = pygame.transform.scale(background, (1024, 768))

    background_mort = pygame.image.load('sprite/background_mort.png')
    background = pygame.transform.scale(background, (1024, 768))
    x = 50
    y = 400
    clock = pygame.time.Clock()

    timer_degats = 2000

    def redrawGameWindow():
        windows.blit(background, (0,0))
        man.draw(windows)
        vison.draw(windows)
        protection.draw(windows, man.x, man.y)
        for bullet in bullets:
            bullet.draw(windows)

        text = font.render("Score: " + str(score), 1, (0, 0, 0))  # Arguments are: text, anti-aliasing, color
        windows.blit(text, (390, 10))

        pygame.display.update()

    score = 0
    font = pygame.font.SysFont("comicsans", 30, True)

    man = Player(x, y, 64, 64)
    vison = enemy(100, 440, 64, 64, 300)

    bullets = []
    protection = Protection(round(man.x+man.width//2), round(man.y + man.height//2), 6, 1)
    run = True

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for bullet in bullets:
            if bullet.y - bullet.radius < vison.hitbox[1] + vison.hitbox[3] and bullet.y + bullet.radius > vison.hitbox[1]:  # Checks x coords
                if bullet.x + bullet.radius > vison.hitbox[0] and bullet.x - bullet.radius < vison.hitbox[0] + \
                        vison.hitbox[2]:  # Checks y coords
                    vison.hit()  # calls enemy hit method
                    score += 1
                    bullets.pop(bullets.index(bullet))  # removes bullet from bullet list
            if bullet.x < windows.get_width() and bullet.x >0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

        #Regarde si le player touche l'ennemie et donne des dégats en contrepartis
        if man.y - man.width < vison.hitbox[1] + vison.hitbox[3] and man.y + man.height > vison.hitbox[
            1]:  # Checks x coords
            if man.x + man.width > vison.hitbox[0] and man.x - man.height < vison.hitbox[0] + vison.hitbox[2]:  # Checks y coords
                man.hit()  # calls enemy hit method
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            man.attacking = True
            if man.left:
                facing = -1
            else:
                facing = 1

            if len(bullets) < 1:
                bullets.append(projectile(round(man.x+man.width//2), round(man.y + man.height//2), 18, (0, 0, 0), facing))

        if (keys[pygame.K_LEFT] or keys[pygame.K_q]) and man.x > 0:
            man.x -= man.vel
            man.left = True
            man.right = False
            man.standing = False  # NEW
            man.attacking = False
        elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and man.x < windows.get_width() - man.width:
            man.x += man.vel
            man.right = True
            man.left = False
            man.standing = False  # NEW
            man.attacking = False
        else:
            man.standing = True

        if keys[pygame.K_e]:
            protection.active = True
            man.vel = 5
        else:
            protection.active = False
            man.standing = True
            #man.walkCount = 0

        if not man.isJump:
            if keys[pygame.K_UP]:
                man.isJump = True
                #man.walkCount = 0

        else:
            if man.jumpCount >= -8:
                neg = 1
                if man.jumpCount < 0:
                    neg = -1
                man.y -= (man.jumpCount ** 2) * 1 * neg
                man.jumpCount -= 1

            else:
                man.isJump = False
                man.jumpCount = 8

        if not protection.active:
            man.vel = man.velBase
            if keys[pygame.K_a]:
                man.attacking = False
                man.dash(windows)
        if (man.health <= 0):
            windows.blit(background_mort, (0, 0))
            pygame.display.update()
        else:
            redrawGameWindow()

    pygame.quit()