import pygame

from settings import Settings

class Button():
    
    def __init__(self, screen):
        self.screen = screen

        self.font = pygame.font.SysFont('hiraginosansgbinterface', 33)
        self.image = self.font.render('Click to play again!', True, (0, 0, 0), (240, 240, 240))
        
        game_settings = Settings()
        self.rect = self.image.get_rect()
        screen_rect = screen.get_rect()
        self.rect.centerx = screen_rect.centerx
        self.rect.centery = screen_rect.centery
    
    def draw_button(self):
        """Draws the button to the screen."""
        self.screen.blit(self.image, self.rect)
