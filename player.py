import pygame



class Player():
    def __init__(self):
        self.health = 100
        self.maxHealth= 100
        self.velocity = 5
        self.attack = 10
        self.image = pygame.image.load('./testAnim/player01.png')
        self.all_projectile = pygame.sprite.Group()



    def launchProjectile(self,projectile):
        self.all_projectile.add(projectile) # ajoute un projectile a la liste
