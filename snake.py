import pygame
from pygame.sprite import Sprite

from settings import Settings

class SnakeHead(Sprite):
    """This class represents the snake head in snake-game.
    
    Args:
        Sprite ([type]): [description]
    """
    
    def __init__(self, screen):
        """Initialize the head of the snake.
        
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
        self.dist_between_body_segments = 15
        
        # Center the snake
        screen_rect = screen.get_rect()
        self.rect.centerx = screen_rect.centerx
        self.rect.centery = screen_rect.centery

    def draw_image(self):
        """Draws the snake head on the screen.
        """
        self.screen.blit(self.image, self.rect)
 
    def update(self, body_positions, body_directions):
        """Updates the position of the snake head.
        
        Args:
            positions (list): positions of each segment of the snake
            directions (list): current direction of each segment of the snake
        """
        self.rect.centerx += self.xdirection * self.dist_between_body_segments
        self.rect.centery += self.ydirection * self.dist_between_body_segments
        
        for i in range(len(body_positions) - 1, 0, -1):
            body_positions[i] = body_positions[i - 1]
            body_directions[i] = body_directions[i - 1]
        body_positions[0] = [self.rect.centerx, self.rect.centery]
        body_directions[0] = [self.xdirection, self.ydirection]
    
    def add_length(self, body_positions, body_directions):
        """[summary]
        
        Args:
            positions ([type]): [description]
            directions ([type]): [description]
        """
        location = [body_positions[-1][0], body_positions[-1][0] + 1]
        if body_directions[-1][0] == 1:
            location = [body_positions[-1][0] - 1, body_positions[-1][0]]
        elif body_directions[-1][0] == -1:
            location = [body_positions[-1][0] + 1, body_positions[-1][0]]
        elif body_directions[-1][1] == 1:
            location = [body_positions[-1][0], body_positions[-1][0] - 1]

        body_positions.append(location)
        body_directions.append([self.xdirection, self.ydirection])
        
        

class SnakeBody(Sprite):
    """This class represents the snake body segment in snake-game."""
    
    def __init__(self, screen, game_settings, x_pos, y_pos):
        super().__init__()

        self.screen = screen
        self.image = pygame.Surface(game_settings.size)
        self.image.fill(game_settings.body_color)
        self.rect = self.image.get_rect()

        self.rect.centerx = x_pos
        self.rect.centery = y_pos

    def draw_image(self):
        """Draws the snake body segment on the screen.
        """
        self.screen.blit(self.image, self.rect)
