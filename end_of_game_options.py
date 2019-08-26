import pygame

from settings import Settings


class PlayAgainButton():
    """This class represents the button that is clicked to replay the
        game."""

    def __init__(self, screen):
        """Initializes a new PlayAgainButton."""
        game_settings = Settings()
        self.screen = screen
        self.font = pygame.font.SysFont('hiraginosansgbinterface', game_settings.font_size)
        self.image = self.font.render('Click to play again!', True, game_settings.foreground_color, game_settings.button_color)
        
        screen_rect = screen.get_rect()
        self.rect = self.image.get_rect()
        self.rect.centerx = screen_rect.centerx
        self.rect.centery = screen_rect.centery
    
    def draw_to_screen(self):
        """Draws the button to the screen."""
        self.screen.blit(self.image, self.rect)

class EndOfGameMessage():
    """This class represents the message which is displayed
        to the user when the game ends."""

    def __init__(self, screen, current_score, high_score):
        """Initializes a new EndOfGameMessage object.
        
        Args:
            screen (pygame.Surface): The screen on which the game is
            being played.
        """
        game_settings = Settings()
        self.screen = screen
        self.score = 0
        self.font = pygame.font.SysFont('hiraginosansgbinterface', game_settings.font_size)

        if current_score <= high_score:
            end_of_game_message = 'Game Over! Your score was ' + str(current_score) + '. High score: ' + str(high_score)
        else:
            end_of_game_message = 'Game Over! Your score was ' + str(current_score) + '. New high score!' 
        self.image = self.font.render(end_of_game_message, True, game_settings.foreground_color, game_settings.background_color)
        screen_rect = self.screen.get_rect()
        self.rect = self.image.get_rect()
        self.rect.centery = screen_rect.centery - 50
        self.rect.centerx = screen_rect.centerx

    def draw_to_screen(self):
        """Print the message to the screen."""
        self.screen.blit(self.image, self.rect)
