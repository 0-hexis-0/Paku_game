import pygame
from pygame.sprite import Sprite


class Paku(Sprite):
    def __init__(self, screen):
        super(Paku, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/PAKU.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.x = 150
        self.rect.centery = self.screen_rect.centery
        self.moving = True

    def blitme(self):
        self.screen.blit(self.image, self.rect)


    def update(self, enemy):
        if self.moving:
            self.rect.x += 5
        elif self.moving == 0:
            self.rect.x -= 5

        if self.rect.x > self.screen_rect.width:
            self.rect.x = -30
            enemy.moving = False
            enemy.flip_image(horizontal=True)
            enemy.horizontal = True

        elif self.rect.x < -30:
            self.rect.x = self.screen_rect.width - 0.2
            enemy.moving = True
            enemy.flip_image(horizontal=True)
            enemy.horizontal = False

    def flip_image(self, horizontal = False, vertical = False):
        self.image = pygame.transform.flip(self.image, horizontal, vertical)



