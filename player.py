import pygame
pygame.init()


class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y

        self.width = width
        self.height = height
        self.velBase = 10
        self.vel = self.velBase
        self.dashVel = 200

        self.isJump = False
        self.left = False
        self.right = True
        self.attacking = False

        self.last_dash = pygame.time.get_ticks()
        self.dash_cooldown = 500

        self.all_projectile = pygame.sprite.Group()

        self.walkCount = 0
        self.jumpCount = 8

        self.standing = True

        self.hitbox = (self.x, self.y, 50, 50)

        self.health = 20

        self.degatCooldown = 2000
        self.last_hit = pygame.time.get_ticks()

     # Animation Marche
        self.walkRight = [pygame.image.load('sprite/perso/player01-right.png'),
                          pygame.image.load('sprite/perso/player01-run03-right.png'),
                          pygame.image.load('sprite/perso/player01-run02-right.png'),
                          pygame.image.load('sprite/perso/player01-run04-right.png')]

        self.walkLeft = [pygame.image.load('sprite/perso/player01-left.png'),
                         pygame.image.load('sprite/perso/player01-run03.png'),
                         pygame.image.load('sprite/perso/player01-run02.png'),
                         pygame.image.load('sprite/perso/player01-run04-left.png')]

     # Animation Saut
        self.jumpLeft = [pygame.image.load('sprite/perso/player01-run.png')]
        self.jumpRight = [pygame.image.load('sprite/perso/player01-run-right.png')]
     # Animation IDLE
        self.charLeft = pygame.image.load('sprite/perso/player01-left.png')
        self.charRight = pygame.image.load('sprite/perso/player01-right.png')
     # Animation Attaque
        self.attackRight = [pygame.image.load('sprite/perso/player01-right-attaque.png'),
                            pygame.image.load('sprite/perso/player01-right-attaque2.png'),
                            pygame.image.load('sprite/perso/player01-right-attaque3.png'),
                            pygame.image.load('sprite/perso/player01-right-attaque4.png')]

        self.attackLeft = [pygame.image.load('sprite/perso/player01-left-attaque.png'),
                            pygame.image.load('sprite/perso/player01-left-attaque2.png'),
                            pygame.image.load('sprite/perso/player01-left-attaque3.png'),
                            pygame.image.load('sprite/perso/player01-left-attaque4.png')]
     # Animation Dash
        self.dashImg = pygame.image.load('sprite/Dash/dashCopie.png')

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
        elif self.attacking:
            if self.right:
                windows.blit(self.attackRight[self.walkCount // 7], (self.x, self.y))
            else:
                windows.blit(self.attackLeft[self.walkCount // 7], (self.x, self.y))
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



        self.hitbox = (self.x, self.y, 60, 64)
        #pygame.draw.rect(windows, (255, 0, 0), self.hitbox, 2)
        font = pygame.font.SysFont("comicsans", 30, True)
        text = font.render("Health: ",1, (0, 0, 0))  # Arguments are: text, anti-aliasing, color
        windows.blit(text, (0, 30))
        pygame.draw.rect(windows, (255, 0, 0), (100, 30, 50 - (5 * (10 - 20)), 10))
        pygame.draw.rect(windows, (0, 128, 0),
                         (100, 30, 50 - (5 * (10 - self.health)), 10))
        pygame.display.update()

    def dash(self, window):
        now = pygame.time.get_ticks()

        if now - self.last_dash >= self.dash_cooldown:
            self.last_dash = now

            if self.right:
                self.dashImg = pygame.transform.rotate(self.dashImg, 180)
                window.blit(self.dashImg, (self.x - 10, self.y))
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
                    window.blit(self.dashImg, (self.x - self.dashVel - (self.dashVel / count_dash), self.y))
                    self.dashImg = pygame.transform.rotate(self.dashImg, 180)
                else:
                    window.blit(self.dashImg, (self.x + self.dashVel - (self.dashVel / count_dash), self.y))
                count_dash += 1
                if count_dash >= 20:
                    count_dash = 0
                pygame.display.update()

    def hit(self):
        now = pygame.time.get_ticks()
        print(now - self.last_hit)
        if now - self.last_hit >= self.degatCooldown:
            self.last_hit = pygame.time.get_ticks()
            if self.health > 0:
                self.health -= 5
                print('hit')
            else:
                self.visible = False
                self.hitbox = (-10000, -10000, -10000, -100000)
        else:
            print('recharge')
        pygame.display.update()



