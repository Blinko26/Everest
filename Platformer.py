import pygame, sys
from pygame.locals import *
pygame.init() # initiates pygame
clock = pygame.time.Clock()

pygame.display.set_caption('Pygame Platformer')

WINDOW_SIZE = (1024,768)

screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # initiate the window

display = pygame.Surface((300,200)) # used as the surface for rendering, which is scaled

moving_right = False
moving_left = False
vertical_momentum = 0
air_timer = 0

walkCount = 0

true_scroll = [0, 0]

dashing_left = False
dashing_right = True

def load_map(path):
    f = open(path + '.txt','r')
    data = f.read()
    f.close()
    data = data.split('\n')
    game_map = []
    for row in data:
        game_map.append(list(row))
    return game_map

game_map = load_map('map')

grass_img = pygame.image.load('grass.png')
dirt_img = pygame.image.load('dirt.png')
finish_img = pygame.image.load('finishLine.png')

player_img = pygame.image.load('sprite/perso/player01-right.png')
player_img = pygame.transform.scale(player_img,(29,32))

player_img_left = pygame.image.load('sprite/perso/player01-left.png')
player_img_left = pygame.transform.scale(player_img_left,(29,32))

player_rect = pygame.Rect(100,100,29,32)

dashImg = pygame.image.load('sprite/Dash/BLBLBLBL.png')
dashImg = pygame.transform.scale(dashImg, (29,32))

background_objects = [[0.25,[120,10,70,400]],[0.25,[280,30,40,400]],[0.5,[30,40,40,400]],[0.5,[130,90,100,400]],[0.5,[300,80,120,400]]]

last_facing = True
dash_vel = 100
countDash = 0

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

while True: # game loop
    display.fill((146,244,255)) # clear screen by filling it with blue

    true_scroll[0] += (player_rect.x-true_scroll[0]-152)/20
    true_scroll[1] += (player_rect.y-true_scroll[1]-106)/20
    scroll = true_scroll.copy()
    scroll[0] = int(scroll[0])
    scroll[1] = int(scroll[1])

    pygame.draw.rect(display,(7,80,75),pygame.Rect(0,120,300,80))
    for background_object in background_objects:
        obj_rect = pygame.Rect(background_object[1][0]-scroll[0]*background_object[0],background_object[1][1]-scroll[1]*background_object[0],background_object[1][2],background_object[1][3])
        if background_object[0] == 0.5:
            pygame.draw.rect(display,(14,222,150),obj_rect)
        else:
            pygame.draw.rect(display,(9,91,85),obj_rect)

    tile_rects = []
    y = 0
    for layer in game_map:
        x = 0
        for tile in layer:
            if tile == '1':
                display.blit(dirt_img, (x*16-scroll[0], y*16-scroll[1]))
            if tile == '2':
                display.blit(grass_img, (x*16-scroll[0], y*16-scroll[1]))
            if tile == 'f':
                display.blit(finish_img, (x*16-scroll[0], y*16-scroll[1]))
            if tile != '0':
                tile_rects.append(pygame.Rect(x*16,y*16,16,16))
            x += 1
        y += 1

    player_movement = [0,0]
    if moving_right == True:
        player_movement[0] += 4
    if moving_left == True:
        player_movement[0] -= 4
    if dashing_left:
        player_movement[0] -= dash_vel
        dashing_left = False
    elif dashing_right:
        player_movement[0] += dash_vel
        dashing_right = False
    player_movement[1] += vertical_momentum
    vertical_momentum += 0.2
    if vertical_momentum > 3:
        vertical_momentum = 3

    player_rect,collisions = move(player_rect,player_movement,tile_rects)

    if collisions['bottom'] == True:
        air_timer = 0
        vertical_momentum = 0
    else:
        air_timer += 1

    moving_right_img = [pygame.transform.scale(pygame.image.load('sprite/perso/player01-right.png'), (29,32)),
                          pygame.transform.scale(pygame.image.load('sprite/perso/player01-run03-right.png'), (29,32)),
                          pygame.transform.scale(pygame.image.load('sprite/perso/player01-run02-right.png'), (29,32)),
                          pygame.transform.scale(pygame.image.load('sprite/perso/player01-run04-right.png'), (29,32))]

    moving_left_img = [pygame.transform.scale(pygame.image.load('sprite/perso/player01-left.png'), (29, 32)),
                         pygame.transform.scale(pygame.image.load('sprite/perso/player01-run03.png'), (29,32)),
                         pygame.transform.scale(pygame.image.load('sprite/perso/player01-run02.png'), (29,32)),
                         pygame.transform.scale(pygame.image.load('sprite/perso/player01-run04-left.png'), (29,32))]

    jumping_img = [pygame.transform.scale(pygame.image.load('sprite/perso/player01-run.png'), (29, 32)),
                   pygame.transform.scale(pygame.image.load('sprite/perso/player01-run-right.png'), (29,32))]

    if moving_right:
        last_facing = True
        display.blit(moving_right_img[walkCount // 7],(player_rect.x-scroll[0],player_rect.y-scroll[1]))
    elif moving_left:
        last_facing = False
        display.blit(moving_left_img[walkCount // 7], (player_rect.x - scroll[0], player_rect.y - scroll[1]))
    else:
        if last_facing:
            display.blit(player_img, (player_rect.x - scroll[0], player_rect.y - scroll[1]))
        else:
            display.blit(player_img_left, (player_rect.x - scroll[0], player_rect.y - scroll[1]))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                moving_right = True
                moving_left = False
            if event.key == K_LEFT:
                moving_left = True
                moving_right = False
            if event.key == K_UP or event.key == K_SPACE:
                if air_timer < 6:
                    vertical_momentum = -5
            if event.key == K_a:
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

        if event.type == KEYUP:
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
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

    screen.blit(pygame.transform.scale(display,WINDOW_SIZE),(0,0))
    pygame.display.update()
    clock.tick(60)
