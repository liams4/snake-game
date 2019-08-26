import pygame
from random import randint
from pygame.sprite import Sprite

from settings import Settings

class Food(Sprite):
    """This class represents a piece of food in snake-game."""
    def __init__(self, screen):
        """Initializes a new Food obejct."""
        game_settings = Settings()
        self.screen = screen
        self.image = pygame.Surface(game_settings.size)
        self.image.fill(game_settings.food_color)
        self.rect = self.image.get_rect()
        self.rect.centerx = randint(0, game_settings.x_dim)
        self.rect.centery = randint(0, game_settings.y_dim)

    def draw_to_screen(self):
        """Draws the food on the screen."""
        self.screen.blit(self.image, self.rect)
