import sys
import pygame


def run_game():
    """游戏的主函数，从这里开始运行游戏"""

    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("外星人入侵")
    bg_color = (230, 230, 230)
    # 设置窗口背景颜色
    screen.fill(bg_color)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()


run_game()
