import pygame

class Ship():
	"""初始化飞机并设置其初始位置"""
	def __init__(self, screen,ai_setting):
		self.screen = screen
		self.ai_setting = ai_setting

		# 加载飞机图像并获取其外接矩形
		self.image = pygame.image.load('images/ic_aircraft.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# 将飞机放在屏幕底部中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# 存储数值
		self.center = float(self.rect.centerx)
		self.moving_right = False
		self.moving_left = False

	def blitem(self):
		"""在指定位置绘制飞机"""
		self.screen.blit(self.image,self.rect)

	def update(self):
		"""按下方向键时移动飞机位置,并控制飞机左右移动的最远距离"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_setting.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_setting.ship_speed_factor
		self.rect.centerx = self.center
