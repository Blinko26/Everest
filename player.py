import pygame
pygame.init()


class Player(object):
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
        self.standing = True

        self.hitbox = (self.x, self.y, 50, 50)

        self.walkRight = [pygame.image.load('sprite/perso/player01-right.png'), pygame.image.load('sprite/perso/player01-run03-right.png'), pygame.image.load('sprite/perso/player01-run02-right.png'), pygame.image.load('sprite/perso/player01-run04-right.png')]
        self.walkLeft = [pygame.image.load('sprite/perso/player01-left.png'), pygame.image.load('sprite/perso/player01-run03.png'), pygame.image.load('sprite/perso/player01-run02.png'), pygame.image.load('sprite/perso/player01-run04-left.png')]
        self.jumpLeft = [pygame.image.load('sprite/perso/player01-run.png')]
        self.jumpRight = [pygame.image.load('sprite/perso/player01-run-right.png')]
        self.charLeft = pygame.image.load('sprite/perso/player01-left.png')
        self.charRight = pygame.image.load('sprite/perso/player01-right.png')

    def draw(self, windows):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not self.standing:
            if self.isJump:
                if self.right:
                    windows.blit(self.jumpRight[0], (self.x, self.y))
                else:
                    windows.blit(self.jumpLeft[0], (self.x, self.y))
            elif self.left:
                windows.blit(self.walkLeft[self.walkCount // 7], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                windows.blit(self.walkRight[self.walkCount // 7], (self.x, self.y))
                self.walkCount += 1

        else:
            if self.isJump:
                if self.right:
                    windows.blit(self.jumpRight[0], (self.x, self.y))
                elif self.left:
                    windows.blit(self.jumpLeft[0], (self.x, self.y))

            else:
                if self.right:
                    windows.blit(self.charRight, (self.x, self.y))
                else:
                    windows.blit(self.charLeft, (self.x, self.y))
        self.hitbox = (self.x + 10, self.y + 5, 20, 90)  # NEW
        pygame.draw.rect(windows, (255, 0, 0), self.hitbox, 2)

        pygame.display.update()
