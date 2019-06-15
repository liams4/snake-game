import sys
import pygame
from settings import Settings
from snake import Snake

def run_game():
    pygame.init()
    game_settings = Settings()

    # initialize screen
    screen = pygame.display.set_mode((game_settings.x_dim, game_settings.y_dim))
    pygame.display.set_caption(game_settings.title)
    background_color = [250, 250, 250]

    # create snake
    snake = Snake(screen, game_settings)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # check for user input
        # move snake based on user input
        # react to move
        screen.fill(background_color)
        snake.draw_image()
        

        pygame.display.flip()



run_game()
