import pygame
pygame.init()

class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing =facing
        self.vel = 8 * facing
        self.picture = pygame.image.load('sprite/laser.png')

    def draw(self, windows):
        windows.blit(self.picture,  (self.x, self.y-15))
