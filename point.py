import pygame
from pygame.sprite import Sprite
from random import *

class Point(Sprite):
    def __init__(self, screen):
        super(Point, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/point.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.x = self.screen_rect.x + 15
        self.rect.centery = self.screen_rect.centery
    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Super_point(Point):
    def __init__(self, screen):
        super(Super_point, self).__init__(screen)
        self.image = pygame.image.load('images/super_point.png')
def points_draw(screen, points, paku):
    point = Point(screen)
    points.add(point)
    rs = randint(1, 16)
    n = 10
    for i in range(1, 17):
        if rs != i:
            point = Point(screen)
            point.rect.x = n + 47.8 * i
            points.add(point)
        else:
            super_point = Super_point(screen)
            super_point.rect.x = n + 47.8 * i
            if paku.rect.x - 80 <= super_point.rect.x <= (paku.rect.x + 80):
                rs += 1
                point = Point(screen)
                point.rect.x = n + 47.8 * i
                points.add(point)
            else:
                points.add(super_point)
    return points

