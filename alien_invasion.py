import sys
import pygame
from settings import Settings
from ship import Ship


def run_game():
    """游戏的主函数，从这里开始运行游戏"""

    pygame.init()
    # 创建设置类
    ai_settings = Settings()
    # 得到表示整个窗口的surface
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # 创建飞船
    ship = Ship(screen)
    pygame.display.set_caption(ai_settings.caption)
    # 设置窗口背景颜色
    screen.fill(ai_settings.bg_color)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        ship.blit_me()
        pygame.display.flip()


run_game()
