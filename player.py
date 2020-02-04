import pygame
pygame.init()


class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.vel = 10
        self.dashVel = 100

        self.isJump = False
        self.left = False
        self.right = False

        self.last_dash = pygame.time.get_ticks()
        self.dash_cooldown = 0

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

        self.dashImg = pygame.image.load('sprite/Dash/dash.png')

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
                windows.blit(self.walkLeft[self.walkCount //7], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                windows.blit(self.walkRight[self.walkCount //7], (self.x, self.y))
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

    def dash(self, window):
        now = pygame.time.get_ticks()

        if now - self.last_dash >= self.dash_cooldown:
            self.last_dash = now

            if self.right:
                self.dashImg = pygame.transform.rotate(self.dashImg, 180)
                window.blit(self.dashImg, (self.x + 10, self.y +20))
                self.dashImg = pygame.transform.rotate(self.dashImg, 180)
                if self.x + self.dashVel > window.get_width():
                    self.x = window.get_width()-self.width-1
                else:
                    self.x += self.dashVel
            else:
                window.blit(self.dashImg, (self.x + 10, self.y + 20))
                if self.x - self.dashVel < 0:
                    self.x = 1
                else:
                    self.x -= self.dashVel

            count_dash = 1
            while count_dash != 0:
                if self.right:
                    self.dashImg = pygame.transform.rotate(self.dashImg, 180)
                    window.blit(self.dashImg, (self.x - self.dashVel + (self.dashVel / count_dash), self.y + 20))
                    self.dashImg = pygame.transform.rotate(self.dashImg, 180)
                else:
                    window.blit(self.dashImg, (self.x + self.dashVel - (self.dashVel / count_dash), self.y + 20))
                count_dash += 1
                if count_dash >= 20:
                    count_dash = 0
                pygame.display.update()

