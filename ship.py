import pygame


class Ship():
    """飞船类，用来管理飞船的行为"""

    def __init__(self, screen):
        """需要一个代表整个窗口的surface来初始化飞船，并设置其初始位置"""

        self.screen = screen
        # 获取一个表示飞船图像的对象
        self.image = pygame.image.load("images/ship.bmp")
        # 获取图片的外接矩形
        self.rect = self.image.get_rect()
        # 获取整个窗口的外界矩形
        self.screen_rect = screen.get_rect()

        # 设置飞船图形的初始位置，将飞船图像设置在屏幕的底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # 飞船向右移动的标志
        self.moving_right = False

    def blit_me(self):
        """在指定位置绘制飞船"""

        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right:
            self.rect.centerx += 1
