import pygame
from random import randint
from pygame.sprite import Sprite
from settings import Settings

# This class represents the food in snake-game.
class Food(Sprite):

    def __init__(self, screen):
        game_settings = Settings()

        self.screen = screen
        self.image = pygame.Surface(game_settings.size)
        self.image.fill(game_settings.food_color)
        self.rect = self.image.get_rect()
        self.rect.centerx = randint(0, game_settings.x_dim)
        self.rect.centery = randint(0, game_settings.y_dim)


# Draws the food on the screen.
    def draw_image(self):
        self.screen.blit(self.image, self.rect)