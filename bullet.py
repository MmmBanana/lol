import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self,game_settings,screan,ship):
        super().__init__()
        self.screan=screan
        self.rect=pygame.Rect(0,0,game_settings.bullet_width,game_settings.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top
        self.color=game_settings.bullet_color
        self.speed=game_settings.bullet_speed_factor
    def update(self):
        self.rect.y-=self.speed
    def draw_bullet(self):
        pygame.draw.rect(self.screan,self.color,self.rect)
