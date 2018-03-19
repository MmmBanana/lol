import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    def __init__(self,game_settings,screan):
        super().__init__()
        self.screan=screan
        self.game_settings=game_settings
        self.image=pygame.image.load("Alien.png")
        self.rect=self.image.get_rect()
    def blitme(self):
        self.screan.blit(self.image,self.rect)