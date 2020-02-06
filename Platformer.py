import pygame, sys
from pygame.locals import *
from enemy import *
from projectile import *
from ecranInterNiveau import *
def niveau2(screen, nbNiveau):



    pygame.init() # initiates pygame
    pygame.mixer.init()

    walkingSound = pygame.mixer.Sound("Sounds/walking.ogg")
    dashSound = pygame.mixer.Sound("Sounds/dash.ogg")
    attackSound = pygame.mixer.Sound("Sounds/attack.ogg")
    enemySound = pygame.mixer.Sound("Sounds/enemy.ogg")
    enemyDeathSound = pygame.mixer.Sound("Sounds/enemy_death.ogg")

    clock = pygame.time.Clock()

    debut_jeu = pygame.time.get_ticks()

    pygame.display.set_caption('Pygame Platformer')

    WINDOW_SIZE = (1024,768)

    screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # initiate the window

    display = pygame.Surface((600, 400)) # used as the surface for rendering, which is scaled

    moving_right = False
    moving_left = False
    vertical_momentum = 0
    air_timer = 0

    walkCount = 0

    true_scroll = [0, 0]
    zoneVictoire = []

    dashing_left = False
    dashing_right = True

    def load_map(path):
        f = open(path + nbNiveau +'.txt','r')
        data = f.read()
        f.close()
        data = data.split('\n')
        game_map = []
        for row in data:
            game_map.append(list(row))
        return game_map

    game_map = load_map('map')

    grass_img = pygame.image.load('sprite/Map/sol01-flat.png')
    grass_img = pygame.transform.scale(grass_img,(16,16))

    grassEdgeLeft_img = pygame.image.load('sprite/Map/sol01-edgeLeft.png')
    grassEdgeLeft_img = pygame.transform.scale(grassEdgeLeft_img,(16,16))

    grassEdgeRight_img = pygame.image.load('sprite/Map/sol01-edgeRight.png')
    grassEdgeRight_img = pygame.transform.scale(grassEdgeRight_img,(16,16))

    dirt_img = pygame.image.load('sprite/Map/sol01-underground.png')
    dirt_img = pygame.transform.scale(dirt_img,(16,16))

    nuage_img01 = pygame.image.load('sprite/Map/cloud02-flat01.png')
    nuage_img01 = pygame.transform.scale(nuage_img01,(16,16))

    nuage_img03 = pygame.image.load('sprite/Map/cloud02-flat02.png')
    nuage_img03 = pygame.transform.scale(nuage_img03,(16,16))

    nuage_img02 = pygame.image.load('sprite/Map/cloud02-flat-ralonge-01-03.png')
    nuage_img02 = pygame.transform.scale(nuage_img02,(16,16))

    nuage_img04 = pygame.image.load('sprite/Map/cloud02-flat03.png')
    nuage_img04 = pygame.transform.scale(nuage_img04,(16,16))



    finish_img = pygame.image.load('finishLine.png')

    player_img = pygame.image.load('sprite/perso/player01-right.png')
    player_img = pygame.transform.scale(player_img,(29,32))

    player_img_left = pygame.image.load('sprite/perso/player01-left.png')
    player_img_left = pygame.transform.scale(player_img_left,(29,32))

    player_rect = pygame.Rect(100,100,29,32)

    dashImg = pygame.image.load('sprite/Dash/BLBLBLBL.png')
    dashImg = pygame.transform.scale(dashImg, (29,32))

    #background_objects = [[0.25,[120,10,70,400]],[0.25,[280,30,40,400]],[0.5,[30,40,40,400]],[0.5,[130,90,100,400]],[0.5,[300,80,120,400]]]
    ile_image = pygame.image.load('sprite/Map/iles.png')
    cloud = pygame.image.load('sprite/Map/nuages-01.png')

    background_objects = [[0.25,[120,10,70,400]],[0.5,[30,40,40,400]]]

    last_facing = True
    dash_vel = 100
    countDash = 0

    all_enemies = pygame.sprite.Group()
    all_projectiles = pygame.sprite.Group()
    all_spawners = []
    list_of_spawned = []

    def stopSounds():
        attackSound.stop()
        walkingSound.stop()
        dashSound.stop()
        enemySound.stop()
        enemyDeathSound.stop()

    def collision_test(rect,tiles):
        hit_list = []
        for tile in tiles:
            if rect.colliderect(tile):
                hit_list.append(tile)
        return hit_list

    def move(rect,movement,tiles):
        collision_types = {'top':False,'bottom':False,'right':False,'left':False}
        rect.x += movement[0]
        hit_list = collision_test(rect,tiles)
        for tile in hit_list:
            if movement[0] > 0:
                rect.right = tile.left
                collision_types['right'] = True
            elif movement[0] < 0:
                rect.left = tile.right
                collision_types['left'] = True
        rect.y += movement[1]
        hit_list = collision_test(rect,tiles)
        for tile in hit_list:
            if movement[1] > 0:
                rect.bottom = tile.top
                collision_types['bottom'] = True
            elif movement[1] < 0:
                rect.top = tile.bottom
                collision_types['top'] = True
        return rect, collision_types

    def spawn_enemies():
        for spawn in all_spawners:
            all_enemies.add(Enemy(spawn[0], spawn[1], spawn[2], spawn[3], spawn[4]))
            all_spawners.remove(spawn)

    run = True
    while run: # game loop
        display.fill((146,244,255)) # clear screen by filling it with blue

        true_scroll[0] += (player_rect.x-true_scroll[0]-152)/20
        true_scroll[1] += (player_rect.y-true_scroll[1]-106)/20
        scroll = true_scroll.copy()
        scroll[0] = int(scroll[0])
        scroll[1] = int(scroll[1])

        #pygame.draw.rect(display,(7,80,75),pygame.Rect(0,120,300,80))

        for background_object in background_objects:
            obj_rect = pygame.Rect(background_object[1][0]-scroll[0]*background_object[0],background_object[1][1]-scroll[1]*background_object[0],background_object[1][2],background_object[1][3])
            if background_object[0] == 0.5:
                display.blit(cloud, obj_rect)
            else:
                display.blit(ile_image, obj_rect)

        tile_rects = []

        y = 0
        for layer in game_map:
            x = 0
            for tile in layer:
                if tile == '1':
                    display.blit(dirt_img, (x * 16 - scroll[0], y * 16 - scroll[1]))
                if tile == '2':
                    display.blit(grass_img, (x * 16 - scroll[0], y * 16 - scroll[1]))
                if tile == '3':
                    display.blit(grassEdgeLeft_img, (x * 16 - scroll[0], y * 16 - scroll[1]))
                if tile == '4':
                    display.blit(grassEdgeRight_img, (x * 16 - scroll[0], y * 16 - scroll[1]))
                if tile == 'a':
                    display.blit(nuage_img01, (x * 16 - scroll[0], y * 16 - scroll[1]))
                if tile == 'b':
                    display.blit(nuage_img02, (x * 16 - scroll[0], y * 16 - scroll[1]))
                if tile == 'c':
                    display.blit(nuage_img03, (x * 16 - scroll[0], y * 16 - scroll[1]))
                if tile == 'd':
                    display.blit(nuage_img04, (x * 16 - scroll[0], y * 16 - scroll[1]))
                if tile == 'f':
                    display.blit(finish_img, (x * 16 - scroll[0], y * 16 - scroll[1]))
                    zoneVictoire.append((x * 16 - scroll[0], y * 16 - scroll[1]))
                if tile == 'e':
                    if (x, y) not in list_of_spawned:
                        all_spawners.append((x * 16, y + 65, 29, 32, scroll))
                        spawn_enemies()
                        list_of_spawned.append((x, y))
                if tile != '0':
                    tile_rects.append(pygame.Rect(x * 16, y * 16, 16, 16))
                x += 1
            y += 1

        jumping_img = [pygame.transform.scale(pygame.image.load('sprite/perso/player01-run.png'), (29, 32)),
                       pygame.transform.scale(pygame.image.load('sprite/perso/player01-run-right.png'), (29, 32))]

        player_movement = [0, 0]

        if moving_right:
            player_movement[0] += 4
        if moving_left:
            player_movement[0] -= 4
        if dashing_left:
            player_movement[0] -= dash_vel
            dashing_left = False
        elif dashing_right:
            player_movement[0] += dash_vel
            dashing_right = False

        player_movement[1] += vertical_momentum
        vertical_momentum += 0.2


        player_rect, collisions = move(player_rect, player_movement, tile_rects)

        if collisions['bottom'] == True:
            air_timer = 0
            vertical_momentum = 0
        else:
            air_timer += 1

        for projectile in all_projectiles:
            if projectile.direction:
                projectile.move(scroll, vertical_momentum)
            else:
                projectile.move_left(scroll, vertical_momentum)

            if projectile.rect.x > 1024 or projectile.rect.x < 0:
                all_projectiles.remove(projectile)

            for enemy in all_enemies:
                if pygame.sprite.collide_rect(projectile, enemy):
                    enemySound.stop()
                    enemyDeathSound.play()
                    all_enemies.remove(enemy)
                    all_projectiles.remove(projectile)

        for enemy in all_enemies:
            enemy.move(player_rect, scroll)

        pygame.draw.rect(display, (255, 0, 0), (player_rect.x - scroll[0], player_rect.y - scroll[1], 29, 32), 2)
        all_projectiles.draw(display)
        all_enemies.draw(display)

        moving_right_img = [pygame.transform.scale(pygame.image.load('sprite/perso/player01-right.png'), (29,32)),
                              pygame.transform.scale(pygame.image.load('sprite/perso/player01-run03-right.png'), (29,32)),
                              pygame.transform.scale(pygame.image.load('sprite/perso/player01-run02-right.png'), (29,32)),
                              pygame.transform.scale(pygame.image.load('sprite/perso/player01-run04-right.png'), (29,32))]

        moving_left_img = [pygame.transform.scale(pygame.image.load('sprite/perso/player01-left.png'), (29, 32)),
                             pygame.transform.scale(pygame.image.load('sprite/perso/player01-run03.png'), (29,32)),
                             pygame.transform.scale(pygame.image.load('sprite/perso/player01-run02.png'), (29,32)),
                             pygame.transform.scale(pygame.image.load('sprite/perso/player01-run04-left.png'), (29,32))]



        if moving_right:
            last_facing = True
            display.blit(moving_right_img[walkCount // 7],(player_rect.x-scroll[0],player_rect.y-scroll[1]))
        elif moving_left:
            last_facing = False
            display.blit(moving_left_img[walkCount // 7], (player_rect.x - scroll[0], player_rect.y - scroll[1]))
        elif vertical_momentum > 3:
            if last_facing:
                display.blit(jumping_img[1], (player_rect.x - scroll[0], player_rect.y - scroll[1]))
            else:
                display.blit(jumping_img[0], (player_rect.x - scroll[0], player_rect.y - scroll[1]))
            vertical_momentum = 3
        else:
            if last_facing:
                display.blit(player_img, (player_rect.x - scroll[0], player_rect.y - scroll[1]))
            else:
                display.blit(player_img_left, (player_rect.x - scroll[0], player_rect.y - scroll[1]))

        if player_rect.y > 768:
            player_rect.x = 0
            player_rect.y = 0

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    walkingSound.play(loops=1000)
                    moving_right = True
                    moving_left = False
                if event.key == K_LEFT:
                    walkingSound.play(loops=1000)
                    moving_left = True
                    moving_right = False
                if event.key == K_UP or event.key == K_SPACE:
                    if air_timer < 6:
                        vertical_momentum = -5
                if event.key == K_a:
                    dashSound.play()
                    if not last_facing:
                        dashing_left = True
                        countDash = 1
                        display.blit(dashImg, (player_rect.x - scroll[0], player_rect.y - scroll[1]))
                    else:
                        dashing_right = True
                        countDash = 1
                        dashImg = pygame.transform.rotate(dashImg, 180)
                        display.blit(dashImg, (player_rect.x - scroll[0], player_rect.y - scroll[1]))
                        dashImg = pygame.transform.rotate(dashImg, 180)
                if event.key == K_e:
                    attacking = True
                    attackSound.play()
                    all_projectiles.add(Projectile(player_rect.x, player_rect.y, scroll, last_facing))
                if event.key == K_ESCAPE:
                    run = False
            if event.type == KEYUP:
                if event.key == K_RIGHT:
                    walkingSound.stop()
                    moving_right = False
                if event.key == K_LEFT:
                    walkingSound.stop()
                    moving_left = False

        walkCount += 1
        if walkCount >= 27:
            walkCount = 0

        while countDash != 0:
            if dashing_right:
                dashImg = pygame.transform.rotate(dashImg, 180)
                display.blit(player_img, (player_rect.x - scroll[0] + (dash_vel / countDash), player_rect.y - scroll[1]))
                dashImg = pygame.transform.rotate(dashImg, 180)
            elif dashing_left:
                display.blit(player_img_left, (player_rect.x - scroll[0] - (dash_vel / countDash), player_rect.y - scroll[1]))

            countDash += 1
            if countDash >= 200:
                countDash = 0

        if player_rect.x > zoneVictoire[0][0] and player_rect.x < zoneVictoire[2][0]:
            stopSounds()
            run = False
            fin_jeu =  pygame.time.get_ticks() - debut_jeu
            f = open('highScore/highScore' + nbNiveau + '.txt', 'a')
            f.write("\n"+str(fin_jeu))
            f.close()
            ecranInterNiveau(screen,fin_jeu, nbNiveau)

        screen.blit(pygame.transform.scale(display,WINDOW_SIZE),(0,0))
        pygame.display.update()
        clock.tick(60)
