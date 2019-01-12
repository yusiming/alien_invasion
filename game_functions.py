import sys
import pygame


def check_events(ship):
    """响应鼠标和键盘事件"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)


def check_keydown_event(event, ship):
    """检测KEYDOWN事件"""
    if event.key == pygame.K_RIGHT:
        # 将飞船的右移标志设置为True
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # 将飞船的右移标志设置为True
        ship.moving_left = True


def check_keyup_event(event, ship):
    """检测KEYUP事件"""
    if event.key == pygame.K_RIGHT:
        # 将飞船的右移标志设置为False
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # 将飞船的右移标志设置为False
        ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    """更新图像，绘制屏幕"""

    screen.fill(ai_settings.bg_color)
    ship.blit_me()
    # 让最近绘制的屏幕可见
    pygame.display.flip()
