import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    """游戏的主函数，从这里开始运行游戏"""

    pygame.init()
    # 创建设置类
    ai_settings = Settings()
    # 得到表示整个窗口的surface
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # 创建飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    while True:
        # 检测事件
        gf.check_events(ai_settings, screen, ship, bullets)
        # 更新飞船的位置
        ship.update()
        gf.update_bullets(bullets)
        # print(len(bullets))
        # 更新屏幕
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
