import pygame

from settings import Settings


class Scoreboard():
    """This class represents the scoreboard in snake-game."""

    def __init__(self, screen):
        """Initializes a new scoreboard object.
        
        Args:
            screen(pygame.Surface): The screen on which the game is
            being played."""
        game_settings = Settings()
        self.screen = screen
        self.score = 0
        self.font = pygame.font.SysFont('hiraginosansgbinterface', game_settings.font_size)
        self.background_color = game_settings.background_color
        self.foreground_color = game_settings.foreground_color
        self.image = self.font.render(str(self.score), True, self.foreground_color, self.background_color)
        self.rect = self.image.get_rect()
        self.rect.top = 30
        self.rect.left = 30
        self.score_increment = game_settings.score_increment
    
    def add_score(self):
        """Adds to the current score.

        Args:
            increment (int): the value to increase the score by.
        """
        self.score += self.score_increment
        self.image = self.font.render(str(self.score), True, self.foreground_color, self.background_color)

    def draw_to_screen(self):
        """Draws the score to the screen."""
        self.screen.blit(self.image, self.rect)
        