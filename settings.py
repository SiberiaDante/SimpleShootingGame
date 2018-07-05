class Settings():
	"""存储所有设置的类"""
	def __init__(self):
		# 游戏界面的宽
		self.screen_width=800
		# 游戏界面的高
		self.screen_height=400
		# 游戏界面的背景颜色
		self.bg_color=(230,230,230)
		# 飞机的移动速度
		self.ship_speed_factor = 1.5

		# 子弹设置
		self.bullet_speed_factor = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60,60,60
		self.bullet_allowed_count = 3

		# 外星人设置
		self.alien_speed_factor = 1
		# 外星人撞到边缘时下移的速度
		self.fleet_drop_speed = 5
		# fleet_direction为1表示向右移， 为-1表示向左移
		self.fleet_direction = 1
		