import sys
import pygame


def check_events():
    """响应鼠标和键盘事件"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, screen, ship):
    """更新图像，绘制屏幕"""

    screen.fill(ai_settings.bg_color)
    ship.blit_me()
    # 让最近绘制的屏幕可见
    pygame.display.flip()

