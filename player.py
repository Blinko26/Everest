import pygame
pygame.init()

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.all_projectile = pygame.sprite.Group()
        self.walkCount = 0
        self.jumpCount = 8
        self.stranding = True

        self.hitbox = (self.x, self.y, 50, 50)

        self.walkRight = [pygame.image.load('sprite/perso/player01-right.png'), pygame.image.load('sprite/perso/player01-run03-right.png'), pygame.image.load('sprite/perso/player01-run02-right.png'), pygame.image.load('sprite/perso/player01-croisees2.png'), pygame.image.load('sprite/perso/player01-run-right.png')]
        self.walkLeft = [pygame.image.load('sprite/perso/player01-left.png'), pygame.image.load('sprite/perso/player01-run03.png'), pygame.image.load('sprite/perso/player01-run02.png'), pygame.image.load('sprite/perso/player01-croisees.png'), pygame.image.load('sprite/perso/player01-run.png')]
        self.char = pygame.image.load('sprite/perso/player01-left.png')

    def draw(self, windows):
        i = 0
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not (self.standing):
            if self.left:
                    windows.blit(self.walkLeft[self.walkCount //6], (self.x, self.y))
                    pygame.display.update()
                    self.walkCount += 1
            elif self.right:

                    windows.blit(self.walkRight[self.walkCount //6], (self.x, self.y))
                    pygame.display.update()
                    self.walkCount += 1

        else:
            windows.blit(self.char, (self.x, self.y))
        self.hitbox = (self.x +10, self.y+5, 30, 35)  # NEW
        pygame.draw.rect(windows, (255, 0, 0), self.hitbox, 2)
