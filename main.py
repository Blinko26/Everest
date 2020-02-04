def niveau1():
    import pygame

    pygame.init()

    from player import Player
    from projectile import projectile
    from enemy import enemy
    from protection import Protection
    windows = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption("MyFirstGame")

    background = pygame.image.load('sprite/background.png')

    x = 50
    y = 300
    width = 40
    height = 60
    vel = 5

    clock = pygame.time.Clock()

    isJump = False
    jumpCount = 10

    left = False
    right = False
    walkCount = 0


    def redrawGameWindow():
        windows.blit(background, (0,0))
        man.draw(windows)
        vison.draw(windows)

        for bullet in bullets:
            bullet.draw(windows)

        text = font.render("Score: " + str(score), 1, (0, 0, 0))  # Arguments are: text, anti-aliasing, color
        windows.blit(text, (390, 10))

        pygame.display.update()

    score = 0
    font = pygame.font.SysFont("comicsans", 30, True)

    man = Player(200, 300, 64, 64)
    vison = enemy(100, 420, 64, 64, 300)

    bullets = []
    run = True

    while run:
        clock.tick(27)

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
            if bullet.x < 500 and bullet.x >0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            if man.left:
                facing = -1
            else:
                facing = 1

            if len(bullets) < 5:
                bullets.append(projectile(round(man.x+man.width//2), round(man.y + man.height//2), 6, (0, 0,0), facing))

        if keys[pygame.K_LEFT] and man.x > man.vel:
            man.x -= man.vel
            man.left = True
            man.right = False
            man.standing = False  # NEW
        elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
            man.x += man.vel
            man.right = True
            man.left = False
            man.standing = False  # NEW
        elif keys[pygame.K_e]:
            if man.left:
                facing = -1
            else:
                facing = 1
            protection = Protection(man.x, man.y, 6, facing)
            protection.draw(windows)
            pygame.display.update()
            pygame.time.delay(500)
        else:

            man.standing = True  # NEW (removed two lines)
            man.walkCount = 0

        if not man.isJump:
            if keys[pygame.K_UP]:
                man.isJump = True
                man.walkCount = 0

        else:
            if man.jumpCount >= -8:
                neg = 1
                if man.jumpCount < 0:
                    neg = -1
                man.y -= (man.jumpCount ** 2) * 0.5 * neg
                man.jumpCount -= 1

            else:
                man.isJump = False
                man.jumpCount = 8

        if keys[pygame.K_a]:
            man.dash(windows)

        redrawGameWindow()

    pygame.quit()