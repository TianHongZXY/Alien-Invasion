import pygame.font

class Scoreboard():
	'''显示得分信息的类'''

	def __init__(self,ai_settings,screen,stats):
		'''初始化显示得分涉及的属性'''
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		self.stats = stats

		#显示得分信息时使用的字体设置
		self.text_color = (30,30,30)
		self.font = pygame.font.SysFont(None,36)

		#准备初始得分图像
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
	def prep_score(self):
		'''将得分转换为一幅渲染的图像'''
		score_str = "{:,}".format(self.stats.score)
		self.score_image = self.font.render('score:' + score_str,True,self.text_color,
			self.ai_settings.bg_color)

		#将得分放在屏幕右上角
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 0

	def prep_high_score(self):
		'''将最高得分渲染为图像'''
		high_score = self.stats.high_score
		high_score_str = "{:,}".format(high_score)
		self.high_score_image = self.font.render('highest:' + high_score_str,True
			,self.text_color,self.ai_settings.bg_color)

		#将最高分放在屏幕中央
		self.high_score_rect = self.score_image.get_rect()
		self.high_score_rect.right = self.screen_rect.centerx
		self.high_score_rect.top = self.score_rect.top

	def prep_level(self):
		'''将等级渲染成图像'''
		self.level_image = self.font.render('level:'+ str(self.stats.level),True,
		self.text_color,self.ai_settings.bg_color)

		#将等级放在得分下方
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom + 5

	def show_score(self):
		'''在屏幕上显示得分'''
		self.screen.blit(self.score_image,self.score_rect)
		self.screen.blit(self.high_score_image,self.high_score_rect)
		self.screen.blit(self.level_image,self.level_rect)