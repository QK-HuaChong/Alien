import sys
import pygame
from ship import Ship
from bullet import Bullet


Up = 273
Dowm = 274
Left = 276
Right = 275


def check_events(ai_settings,screen,ship,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == Right:
                ship.moving_right = True
            if event.key == Left:
                ship.moving_left = True
            if event.key == Up:
                ship.moving_top = True
            if event.key == Dowm:
                ship.moving_down = True
            if event.key == pygame.K_SPACE:
                new_bullet = Bullet(ai_settings,screen,ship)
                bullets.add(new_bullet)

        elif event.type == pygame.KEYUP:
            if event.key == Right:
                ship.moving_right = False
            if event.key == Left:
                ship.moving_left = False
            if event.key == Up:
                ship.moving_top = False
            if event.key == Dowm:
                ship.moving_down = False

def update_screen(ai_settings,screen,ship,bullets):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    pygame.display.flip()
