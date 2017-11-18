import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import game_functions as gf

def run_game():
	""" Initialize game and create a screen object """
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	#Make play button
	play_button = Button(ai_settings, screen, "Play")
	# create an instance to store game statistics
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)
	
	# Make a ship.
	ship = Ship(ai_settings, screen)
	#Alien instance
	alien = Alien(ai_settings, screen)
	# Group for bullets
	bullets = Group()
	aliens = Group()
	
	# create the fleet of aliens
	gf.create_fleet(ai_settings, screen, ship, aliens)
	""" Starting the main loop for the Game """
	while True:
		gf.check_events(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)		
		
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
			gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()
	