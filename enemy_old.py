import pygame
pygame.init()

class Enemy_old(object):


    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 3
        self.image = [pygame.image.load('enemy01.png')]

        self.walkRight = [pygame.image.load('sprite/visonDroit.png')]
        self.walkLeft = [pygame.image.load('sprite/visonGauche.png')]

        self.hitbox = (self.x, self.y, 29, 32)
        self.health = 10
        self.visible = True

    def draw(self, windows):
        if self.visible:
            self.move()
            if self.walkCount + 1 >= 33:
                self.walkCount = 0
            if self.vel >= 0:
                windows.blit(self.image[0], (self.x, self.y))
                self.walkCount += 1
            else:
                saveImg = pygame.transform.flip(pygame.transform.rotate(self.image[0], 180), False, True)
                windows.blit(saveImg, (self.x, self.y))
                self.walkCount += 1
            self.hitbox = (self.x, self.y, 60, 30)
            pygame.draw.rect(windows, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(windows, (0, 128, 0),
                             (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))

            self.hitbox = (self.x, self.y + 150, 29, 32)

    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
    def hit(self):
        if self.health >= 0:
            self.health -= 10
            print(self.health)
        else:
            self.visible = False
            self.hitbox = (-10000, -10000, -10000, -100000)