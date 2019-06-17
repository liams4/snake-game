import pygame
import sys
from settings import Settings

# This class contains functions that are used to help run snake-game.

# Responds to user input.
def respond_to_input(snake):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if snake.xdirection != 0:
                    if event.key == pygame.K_UP: 
                        snake.ydirection = -1
                        snake.xdirection = 0
                    elif event.key == pygame.K_DOWN:
                        snake.ydirection = 1  
                        snake.xdirection = 0
                else:
                    if event.key == pygame.K_RIGHT: 
                        snake.xdirection = 1
                        snake.ydirection = 0
                    elif event.key == pygame.K_LEFT:
                        snake.xdirection = -1  
                        snake.ydirection = 0 
    

def check_valid_position(snake_head, positions):
    game_settings = Settings()
    if (positions[0] in positions[1:] or 
            snake_head.rect.centerx < 0 or 
            snake_head.rect.centerx > game_settings.x_dim or 
            snake_head.rect.centery < 0 or 
            snake_head.rect.centery > game_settings.y_dim):
            sys.exit()