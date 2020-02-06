import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, scroll):
        super().__init__()
        self.width = width
        self.height = height
        self.radius = 20
        self.image = pygame.image.load('enemy01.png')
        #self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.vel = 1
        self.maxhealth = 25
        self.health = self.maxhealth
        self.attack = 5
        self.rect = self.image.get_rect()
        self.scroll = scroll
        self.rect.x = x - self.scroll[0]
        self.rect.y = y - self.scroll[1]


    def move(self, prect, scroll):
        if prect.x >= self.rect.x - self.radius or prect.x <= self.rect.x + self.radius:
            if self.rect.x >= prect.x - scroll[0] + 30:
                if self.scroll[0] != scroll[0]:
                    self.rect.x += self.scroll[0] - scroll[0]
                    self.scroll[0] = scroll[0]
                self.rect.x -= self.vel
                if self.scroll[1] != scroll[1]:
                    self.rect.y += self.scroll[1] - scroll[1]
                    self.scroll[1] = scroll[1]
            else:
                if self.scroll[0] != scroll[0]:
                    self.rect.x += self.scroll[0] - scroll[0]
                    self.scroll[0] = scroll[0]
                self.rect.x += self.vel
                if self.scroll[1] != scroll[1]:
                    self.rect.y += self.scroll[1] - scroll[1]
                    self.scroll[1] = scroll[1]

            if self.rect.y >= prect.y - scroll[1]:
                if self.scroll[0] != scroll[0]:
                    self.rect.x += self.scroll[0] - scroll[0]
                    self.scroll[0] = scroll[0]
                self.rect.y -= self.vel
                if self.scroll[1] != scroll[1]:
                    self.rect.y += self.scroll[1] - scroll[1]
                    self.scroll[1] = scroll[1]
            else:
                if self.scroll[0] != scroll[0]:
                    self.rect.x += self.scroll[0] - scroll[0]
                    self.scroll[0] = scroll[0]
                self.rect.y += self.vel
                if self.scroll[1] != scroll[1]:
                    self.rect.y += self.scroll[1] - scroll[1]
                    self.scroll[1] = scroll[1]
