import pygame
pygame.init()


class Protection(object):

    def __init__(self, x, y, radius, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.facing = facing
        self.picture = [pygame.image.load('sprite/perso/wall.png'), pygame.image.load('sprite/perso/wall02.png'), pygame.image.load('sprite/perso/wall.png'), pygame.image.load('sprite/perso/wall02.png') ]
        self.rounds = 0

    def draw(self, windows):
        windows.blit(self.picture[0],  (self.x-15, self.y-15))
        pygame.display.update()


