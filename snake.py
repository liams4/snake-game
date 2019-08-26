import sys

import pygame
from pygame.sprite import Sprite

from settings import Settings

class SnakeHead(Sprite):
    """This class represents a snake head."""
    
    def __init__(self, screen):
        """Initializes a new SnakeHead.
        
        Args:
            screen (pygame.Surface): The screen that this snake head appears on.
        """
        super().__init__()

        game_settings = Settings()
        self.screen = screen
        self.image = pygame.Surface(game_settings.size)
        self.image.fill(game_settings.head_color)
        self.rect = self.image.get_rect()

        self.xdirection = 1
        self.ydirection = 0
        self.dist_between_body_segments = game_settings.dist_between_body_segments
        
        screen_rect = screen.get_rect()
        self.rect.centerx = game_settings.starting_x_position
        self.rect.centery = screen_rect.centery

    def draw_to_screen(self):
        """Draws the snake head on the screen."""
        self.screen.blit(self.image, self.rect)
    
    def update_position(self):
        """Updates the position of the snake head."""
        self.rect.centerx += self.xdirection * self.dist_between_body_segments
        self.rect.centery += self.ydirection * self.dist_between_body_segments
    
    def update_direction(self):
        """Updates the direction of the snake based on user input.
        
        Args:
            snake (SnakeHead): the head of the snake
        """
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if self.xdirection != 0:
                        if event.key == pygame.K_UP: 
                            self.ydirection = -1
                            self.xdirection = 0
                        elif event.key == pygame.K_DOWN:
                            self.ydirection = 1  
                            self.xdirection = 0
                    else:
                        if event.key == pygame.K_RIGHT: 
                            self.xdirection = 1
                            self.ydirection = 0
                        elif event.key == pygame.K_LEFT:
                            self.xdirection = -1  
                            self.ydirection = 0 
    

class SnakeBodySegment(Sprite):
    """This class represents a snake body segment."""
    
    def __init__(self, screen, x_pos, y_pos):
        """Initializes a new SnakeBodySegment.
        
        Args:
            screen (pygame.Surface): The screen that this body segment
                appears on
            x_pos (int): the x-position of the body segment
            y_pos (int): the y-position of the body segment
        """
        super().__init__()

        game_settings = Settings()
        self.screen = screen
        self.image = pygame.Surface(game_settings.size)
        self.image.fill(game_settings.body_color)
        self.rect = self.image.get_rect()
        self.rect.centerx = x_pos
        self.rect.centery = y_pos

    def draw_to_screen(self):
        """Draws the snake body segment on the screen."""
        self.screen.blit(self.image, self.rect)
