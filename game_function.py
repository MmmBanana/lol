import pygame, sys
from bullet import Bullet
def check_events(game_settings,screan,ship,bullets):
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        elif i.type==pygame.KEYDOWN:
            check_keydown_events(game_settings,screan,i,ship,bullets)
        elif i.type == pygame.KEYUP:
            check_keyup_events(i, ship)

def update_screan(background,ship,bullets,aliens,screan):
    pygame.display.flip()
    #screan.fill(game_settings.bg_color)
    background.update()
    ship.blitme()
    aliens.blitme()
    aliens.draw(screan)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
def check_keydown_events(game_settings,screan,i,ship,bullets):
    if i.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif i.key == pygame.K_LEFT:
        ship.moving_left = True
    elif i.key == pygame.K_UP:
        ship.moving_up = True
    elif i.key == pygame.K_DOWN:
        ship.moving_down = True
    elif i.key == pygame.K_SPACE:
        if len(bullets)<game_settings.bullets_allowed:
            newbullet = Bullet(game_settings, screan, ship)
            bullets.add(newbullet)



"""
def create_fleet(game_settings,screan,aliens):
    alien=Alien(game_settings,screan)
    alien_width=alien.rect.width
    available_space_x=game_settings.screan_width-2*alien_width
    number_aliens_x=int(available_space_x/(2*alien_width))

    for alien_number in range(number_aliens_x):
        alien=Alin(game_settings,screan)
        alien.x=alien_width+2*alien_width*alien_number
        alien.rect.x=alien.x
        aliens.add(alien)
"""
def get_number_rows(game_settings,ship_height,alien_height):
    available_space_y=game_settings.screan_height-(3*alien_height)-ship_height
    number_rows=int(available_space_y/(2*alien_height))
    return (number_rows)

def get_number_aliens_x(game_settings,alien_width):
    available_space_x=game_settings.screan_width-2*alien_width
    number_aliens_x=int(available_space_x/(2*alien_width))
    return (number_aliens_x)

def create_alien(game_settings,screan,aliens,alien_number,row_number):
    alien=Alien(game_settings,screan)
    alien_width=alien.rect.width
    alien.x=alien_width+2*alien_width*alien_number
    alien.rect.x=alien.x
    alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
    aliens.add(alien)

def create_fleet(game_settings,screan,aliens,ship):
    alien=Alien(game_settings,screan)
    number_aliens_x=get_number_aliens_x(game_settings,alien.rect.width)
    number_rows=get_number_rows(game_settings,ship.rect.height,alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(game_settings,screan,aliens,alien_number,row_number)




def check_keyup_events(i,ship):
    if i.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif i.key == pygame.K_LEFT:
        ship.moving_left = False
    elif i.key == pygame.K_UP:
        ship.moving_up = False
    elif i.key == pygame.K_DOWN:
        ship.moving_down = False
    elif i.key == pygame.K_SPACE:
        ship.space_center = False

def update_bullets(bullets):
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)
