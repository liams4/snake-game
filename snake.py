import pygame
from pygame.sprite import Sprite

# This class represents the snake in snake-game.
class SnakeHead(Sprite):
    
    def __init__(self, screen, snake_settings):
        super().__init__()

        self.screen = screen
        self.image = pygame.Surface(snake_settings.size)
        self.image.fill(snake_settings.head_color)
        self.rect = self.image.get_rect()

        self.xdirection = 1
        self.ydirection = 0
        self.speed = 15
        
        # Center the snake
        screen_rect = screen.get_rect()
        self.rect.centerx = screen_rect.centerx
        self.rect.centery = screen_rect.centery

    # Draws the snake head on the screen.
    def draw_image(self):
        self.screen.blit(self.image, self.rect)

    # Updates the position of the snake.
    def update(self, positions):
        
        self.rect.centerx += self.xdirection * self.speed
        self.rect.centery += self.ydirection * self.speed
        
        for i in range(len(positions) - 1, 0, -1):
            positions[i] = positions[i - 1]
        positions[0] = [self.rect.centerx, self.rect.centery]
        
class SnakeBody(Sprite):

    def __init__(self, screen, snake_settings, x_pos, y_pos):
        super().__init__()

        self.screen = screen
        self.image = pygame.Surface(snake_settings.size)
        self.image.fill(snake_settings.body_color)
        self.rect = self.image.get_rect()

        self.rect.centerx = x_pos
        self.rect.centery = y_pos

    # Draws the snake body segment on the screen.
    def draw_image(self):
        self.screen.blit(self.image, self.rect)
