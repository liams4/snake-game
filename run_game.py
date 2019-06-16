import sys
import pygame
from settings import Settings
from snake import SnakeHead, SnakeBody
from game_functions import respond_to_input

def run_game():
    pygame.init()

    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.x_dim, game_settings.y_dim))
    pygame.display.set_caption(game_settings.title)
    background_color = game_settings.background_color
    snake_head = SnakeHead(screen, game_settings)

    positions = [[snake_head.rect.centerx, snake_head.rect.centery]]
    for i in range(game_settings.starting_body_length):
        positions.append([positions[i][0] - 15, snake_head.rect.centery])

    while True:
        screen.fill(background_color)
        respond_to_input(snake_head)
        snake_head.update(positions)
        snake_head.draw_image()
        
        for position in positions[1:]:
            body_segment = SnakeBody(screen, game_settings, position[0], position[1])
            body_segment.draw_image()

        if (positions[0] in positions[1:] or 
            snake_head.rect.centerx < 0 or 
            snake_head.rect.centerx > game_settings.x_dim or 
            snake_head.rect.centery < 0 or 
            snake_head.rect.centery > game_settings.y_dim):
            sys.exit()

        # if any of the positions match, or if the x or y are outside of certain values

        pygame.display.flip()



run_game()
