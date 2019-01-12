import sys
import pygame
from bullet import Bullet


def check_events(ai_settings, screen, ship, bullets):
    """响应鼠标和键盘事件"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)


def check_keydown_event(event, ai_settings, screen, ship, bullets):
    """检测KEYDOWN事件"""
    if event.key == pygame.K_RIGHT:
        # 将飞船的右移标志设置为True
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # 将飞船的右移标志设置为True
        ship.moving_left = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(bullets, ai_settings, screen, ship)


def check_keyup_event(event, ship):
    """检测KEYUP事件"""
    if event.key == pygame.K_RIGHT:
        # 将飞船的右移标志设置为False
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # 将飞船的右移标志设置为False
        ship.moving_left = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False


def update_screen(ai_settings, screen, ship, bullets):
    """更新图像，绘制屏幕"""

    screen.fill(ai_settings.bg_color)
    ship.blit_me()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(bullets):
    """更新子弹的位置，删除已消失的子弹"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(bullets, ai_settings, screen, ship):
    # 创建一颗子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed_max:
        bullets.add(Bullet(ai_settings, screen, ship))
