import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """管理游戏资源和行为的类"""
    
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        #自定义窗口大小
        size = (self.settings.screen_width,self.settings.screen_height)
        self.screen = pygame.display.set_mode(size)

        # #全屏设置
        # self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        # #更新settings里的屏幕大小参数
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        #设置窗口标题
        pygame.display.set_caption("Alien Invasion")

        #设置背景色, 可以通过Settings()来设置
        #self.bg_color = (230,230,230)

        #创建飞船
        self.ship = Ship(self)

        #创建存储子弹编组
        self.bullets = pygame.sprite.Group()

        #实例化Alien, 创建外星舰队
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    
    #重构_check_evets()方法 （@deprecate）
    # def _check_events(self):
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             sys.exit()
    #         elif event.type == pygame.KEYDOWN:
    #             if event.key == pygame.K_RIGHT:
    #                 self.ship.moving_right = True
    #             if event.key == pygame.K_LEFT:
    #                 self.ship.moving_left = True
    #         elif event.type == pygame.KEYUP:
    #             if event.key == pygame.K_RIGHT:
    #                 self.ship.moving_right = False
    #             if event.key == pygame.K_LEFT:
    #                 self.ship.moving_left = False
    
    def _fire_bullet(self):
        """创建一颗子弹，并将其加入编组bullets"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_keydown_events(self,event):
        """响应按下"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self,event):
        """响应释放"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                    

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        pygame.display.flip()
    
    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
    
    def _create_fleet(self):
        """创建一个外星舰队"""
        #创建一个外星人再不断添加，直到没有空间添加新的外星人为止
        #外星人的间距为外星人的宽度
        alien = Alien(self)
        #self.aliens.add(alien)
        alien_width = alien.rect.width

        current_x = alien_width
        while current_x < (self.settings.screen_width - 2 * alien_width):
            new_alien = Alien(self)
            new_alien.x = current_x + alien_width
            new_alien.rect.x = current_x
            self.aliens.add(new_alien)
            current_x += 2 * alien_width

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            #监听键盘和鼠标事件(@deprecate)
            #for event in pygame.event.get():
                #if event.type == pygame.QUIT:
                    #sys.exit()
            self._check_events()
            self.ship.update()
            self._update_bullets()
            # self.bullets.update()
            # #删除已消失的子弹
            # for bullet in self.bullets.copy():
            #     if bullet.rect.bottom <= 0:
            #         self.bullets.remove(bullet)
            #print(len(self.bullets))
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

        


