import pygame

class Projectile(pygame.sprite.Sprite):

    def __init__(self, x, y, scroll, facing):
        super().__init__()
        self.vel = 5
        self.image = pygame.image.load('sprite/Attack/attack06.png')
        self.image = pygame.transform.scale(self.image, (16,24))
        self.rect = self.image.get_rect()
        self.scroll = scroll
        self.rect.x = x - self.scroll[0]
        self.rect.y = y - self.scroll[1]
        self.direction = facing
        self.angle = 0
        self.scale = 1

    def move(self, scroll, vm):
        if self.scroll[0] != scroll[0]:
            self.rect.x += self.scroll[0] - scroll[0]
            self.scroll[0] = scroll[0]
        self.rect.x += self.vel
        if self.scroll[1] != scroll[1] or vm != 0:
            self.rect.y += self.scroll[1] - scroll[1]
            self.scroll[1] = scroll[1]

    def move_left(self, scroll, vm):
        if self.scroll[0] != scroll[0]:
            self.rect.x += self.scroll[0] - scroll[0]
            self.scroll[0] = scroll[0]
        self.rect.x -= self.vel
        if self.scroll[1] != scroll[1] or vm != 0:
            self.rect.y += self.scroll[1]-scroll[1]
            self.scroll[1] = scroll[1]