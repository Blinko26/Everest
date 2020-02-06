import pygame
pygame.init()


class Protection(object):

    def __init__(self, x, y, radius, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.facing = facing
        self.picture = [pygame.image.load('sprite/Shield/shield-Fin.png'), pygame.image.load('sprite/Shield/shield-Fin2.png'), pygame.image.load('sprite/Shield/shield-Fin3.png') ]
        self.rounds = 0
        self.active = False
        self.cooldown = 1000

    def draw(self, windows, x, y):
        if self.active:
            if self.rounds +1 >= 27:
                self.rounds = 0
            windows.blit(self.picture[self.rounds // 9], (x - 15, y - 15))

            self.rounds += 1
