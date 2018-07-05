import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
#from alien import Alien


def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings=Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    # 创建飞船
    ship = Ship(screen,ai_settings)

    # 创建一个存储子弹的编组
    bullets = Group()
    # 创建一个存储外星人的编组
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, aliens)
  

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_event(ai_settings, screen, ship, bullets)
        ship.update()

        # 更新子弹的位置， 并删除已消失的子弹
        gf.update_bullets(bullets)

        # 每次循环时都重新绘制屏幕
        gf.update_screen(ai_settings,screen,ship,bullets,aliens)

run_game()