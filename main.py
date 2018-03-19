from pygame.sprite import Group
import pygame, sys
import game_function as g_f
from background import Background
from ship import Ship
from settings import Settings
def init_game():
    pygame.init()
    game_settings = Settings()
    screan = pygame.display.set_mode((game_settings.screan_width, game_settings.screan_height))
    ship=Ship(screan)
    bullets=Group()
    aliens=Group()
    g_f.create_fleet(game_settings,screan,aliens,ship)
    background=Background(screan)

    pygame.display.set_caption("Dota 3")
    while True:
        g_f.check_events(game_settings,screan,ship,bullets)
        g_f.update_screan(background,ship,bullets,aliens)
        ship.update()
        bullets.update()

        for bullet in bullets.copy():
            if bullet.rect.bottom<=0:
                bullets.remove(bullet)

init_game()