import pygame


class Ship():
    """飞船类，用来管理飞船的行为"""

    def __init__(self, ai_settings, screen):
        """需要一个代表整个窗口的surface来初始化飞船，并设置其初始位置"""

        self.screen = screen
        self.ai_settings = ai_settings
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
        # 飞船向左移动的标志
        self.moving_left = False
        self.center = float(self.rect.centerx)

    def blit_me(self):
        """在指定位置绘制飞船"""

        self.screen.blit(self.image, self.rect)

    def update(self):
        # 只有当右移标志为True，并且飞船右侧边缘的坐标小于整个屏幕的右侧边缘的坐标时，才更新位置
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        # 只有当左移标志为True，并且飞船左侧边缘的坐标大于0时，才更新位置
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center
