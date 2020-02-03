import pygame
import time

pygame.init()


(width, height) = (1024, 768)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Test Fenetre")
animation = [pygame.image.load('./testAnim/dio1.png'), pygame.image.load('./testAnim/dio5.png'), pygame.image.load('./testAnim/dio6.png'), pygame.image.load('./testAnim/dio2.png'), pygame.image.load('./testAnim/dio3.png'), pygame.image.load('./testAnim/dio4.png')]
background = pygame.image.load("./testAnim/bg.jpg")

running = True
def redrawGameWindow():
    screen.blit(background, (0, 0))
    for i in range(0,6,1):
        pygame.time.delay(50)
        screen.blit(animation[i], (250, 250))
        pygame.display.update()
        pygame.time.delay(50)

i = 1
while running:

    screen.blit(background,(0, 0))


    pygame.display.flip()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    redrawGameWindow()



