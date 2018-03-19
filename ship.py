import pygame
class Ship():
    def __init__(self,screan):
        self.screan=screan
        self.image=pygame.image.load("images/spaceship-309153_1280.png")
        self.image = pygame.transform.scale(self.image, (600, 300))
        self.rect=self.image.get_rect()
        self.screan_rect=screan.get_rect()
        self.rect.centerx=self.screan_rect.centerx
        self.rect.centery=self.screan_rect.centery
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.space_center = False

    def blitme(self):
        self.screan.blit(self.image,self.rect)
    def update(self):
        if self.moving_right and self.rect.right<self.screan_rect.right:
            self.rect.centerx += 3
        if self.moving_left and self.rect.left>self.screan_rect.left:
            self.rect.centerx -= 3
        if self.moving_up and self.rect.top>self.screan_rect.top:
            self.rect.centery -= 3
        if self.moving_down and self.rect.bottom<self.screan_rect.bottom:
            self.rect.centery += 3
        if self.space_center:
            self.rect.centerx=self.screan_rect.centerx
            self.rect.centery = self.screan_rect.centery