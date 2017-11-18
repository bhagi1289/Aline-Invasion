import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	"""Initialize the ship and set its stating position """
	
	def __init__(self, ai_settings, screen):
		""" Initialize the ship and set its starting postion """
		super(Ship, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		# Load the ship image
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		# Start each new ship at the bottom center of the screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		#Store a decimal value for ship's center
		self.center = float(self.rect.centerx)
		# Movement flag
		self.moving_right = False
		self.moving_left = False
		#Ship settings
		#self.ship_speed_factor = 1.5

	def update(self):
		""" Update the ship's position based on the movement flag. """
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor
			
		#update rect object from self.center.
		self.rect.centerx = self.center
	
	def blitme(self):
		""" Draw the ship at its curent location """
		self.screen.blit(self.image, self.rect)
		
	def center_ship(self):
		""" center the ship on the screen """
		self.center = self.screen_rect.centerx