import pygame
from pygame.sprite import Sprite

# This class represents the snake in snake-game.
class Snake(Sprite):
    
    def __init__(self, screen, snake_settings):
        super().__init__()
        
        self.screen = screen
        self.image = pygame.Surface(snake_settings.size)
        self.image.fill(snake_settings.head_color)
        self.rect = self.image.get_rect()
        
        # Center the snake
        screen_rect = screen.get_rect()
        self.rect.centerx = screen_rect.centerx
        self.rect.centery = screen_rect.centery

    # Draws the snake on the screen.
    def draw_image(self):
        self.screen.blit(self.image, self.rect)
        