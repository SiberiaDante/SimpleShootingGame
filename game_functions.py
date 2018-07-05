import sys
import pygame
from alien import Alien
from bullet import Bullet

def check_event(ai_settings, screen, ship, bullets):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ai_settings, screen, ship, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)

"""更新屏幕上的图像"""
def update_screen(ai_settings, screen, ship, bullets,aliens):
	"""更新屏幕上的图像，并切换到新屏幕"""
	# 每次循环时都重绘屏幕
	screen.fill(ai_settings.bg_color)
	for bulle in bullets.sprites():
		bulle.draw_bullet()
	ship.blitem()
	#alien.blitem()
	aliens.draw(screen)
	# 让最近绘制的屏幕可见
	pygame.display.flip()

"""更新子弹，并删除消失的子弹"""
def update_bullets(bullets):
	# 更新子弹的位置
    bullets.update()
    # 删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)

"""按下方向键"""
def check_keydown_events(event,ai_settings, screen, ship, bullets):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings,screen,ship,bullets)
	elif event.key == pygame.K_q:
		sys.exit()

"""松开方向键"""
def check_keyup_events(event,ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

"""创建子弹"""
def fire_bullet(ai_settings,screen,ship,bullets):
	if len(bullets) <ai_settings.bullet_allowed_count:
		# 创建一颗子弹， 并将其加入到编组bullets中
		new_bullet = Bullet(ai_settings,screen,ship)
		bullets.add(new_bullet)

"""创建外星人群"""
def create_fleet(ai_settings, screen, aliens):
	# 创建一个外星人， 并计算一行可容纳多少个外星人
	# 外星人间距为外星人宽度
	alien =Alien(ai_settings,screen)
	number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)

	for alien_number in range(number_aliens_x):
		create_alien(ai_settings,screen,aliens,alien_number)
	# alien_width = alien.rect.width
	# available_space_x = ai_settings.screen_width - 2 * alien_width
	# number_aliens_x = int(available_space_x / (2 * alien_width))

	# # 创建第一行外星人
	# for alien_number in range(number_aliens_x):
	# 	# 创建第一个外星人并将其加入当前行
	# 	alien = Alien(ai_settings,screen)
	# 	alien_x = alien_width + 2 * alien_width * alien_number
	# 	alien.rect.x = alien_x
	# 	aliens.add(alien)

"""计算每行可容纳多少个外星人"""
def get_number_aliens_x(ai_settings,alien_width):
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x

"""创建一个外星人并将其放在当前行"""
def create_alien(ai_settings, screen, aliens, alien_number):
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	aliens.add(alien)