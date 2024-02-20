import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """管理游戏资源和行为的类"""
    
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        #设置窗口大小
        size = (self.settings.screen_width,self.settings.screen_height)
        self.screen = pygame.display.set_mode(size)

        #设置窗口标题
        pygame.display.set_caption("Alien Invasion")

        #设置背景色, 可以通过Settings()来设置
        #self.bg_color = (230,230,230)

        #创建飞船
        self.ship = Ship(self)
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            #监听键盘和鼠标事件(@deprecate)
            #for event in pygame.event.get():
                #if event.type == pygame.QUIT:
                    #sys.exit()
            self._check_events()
            self._update_screen()
            #时钟计时
            self.clock.tick(60)

            #每次循环时重新绘制屏幕(@deprecate)
            #self.screen.fill(self.settings.bg_color)
            #self.ship.blitme()

            #让最新绘制的屏幕可见(@deprecate)
            #pygame.display.flip()

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()

        


