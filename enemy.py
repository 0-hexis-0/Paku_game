import pygame
from pygame.sprite import Sprite


class Enemy(Sprite):
    def __init__(self, screen):
        super(Enemy, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/enemy.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.x = 650
        self.rect.centery = self.screen_rect.centery
        self.moving = False
        self.weakness =False
        self.horizontal = True
        self.die = False

    def update(self):
        if ((self.rect.x > 780 or self.rect.x < -30) and self.weakness) or self.die:
            pass
        else:
            if self.moving and self.weakness == False:
                self.rect.x += 3
            elif self.moving == 0 and self.weakness == False :
                self.rect.x -= 3
            if self.moving and self.weakness == True:
                self.rect.x -= 3
            elif self.moving == False and self.weakness == True:
                self.rect.x += 3



    def flip_image(self, horizontal = False, vertical = False):
        self.image = pygame.transform.flip(self.image, horizontal, vertical)