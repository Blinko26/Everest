import pygame
pygame.init()

class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 15 * facing
        self.picture = [pygame.image.load('sprite/Attack/attack06.png'), pygame.image.load('sprite/Attack/attack06-vertical.png')]
        self.rounds = 0

    def draw(self, windows):
        if self.rounds + 1 >= 27:
            self.rounds = 0
        windows.blit(self.picture[self.rounds//13],  (self.x-15, self.y))
        self.rounds += 1
