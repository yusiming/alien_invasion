import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    """游戏的主函数，从这里开始运行游戏"""

    pygame.init()
    # 创建设置类
    ai_settings = Settings()
    # 得到表示整个窗口的surface
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # 创建飞船
    ship = Ship(screen)
    screen.fill(ai_settings.bg_color)
    while True:
        # 检测事件
        gf.check_events(ship)
        # 更新飞船的位置
        ship.update()
        # 更新屏幕
        gf.update_screen(ai_settings, screen, ship)


run_game()
