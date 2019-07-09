"""This module contains functions that are used to help run snake-game.
"""
import sys

import pygame

from settings import Settings

def respond_to_input(snake_head):
    """Responds to user input.
    
    Args:
        snake (SnakeHead): the head of the snake in snake_game 
    """
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if snake_head.xdirection != 0:
                    if event.key == pygame.K_UP: 
                        snake_head.ydirection = -1
                        snake_head.xdirection = 0
                    elif event.key == pygame.K_DOWN:
                        snake_head.ydirection = 1  
                        snake_head.xdirection = 0
                else:
                    if event.key == pygame.K_RIGHT: 
                        snake_head.xdirection = 1
                        snake_head.ydirection = 0
                    elif event.key == pygame.K_LEFT:
                        snake_head.xdirection = -1  
                        snake_head.ydirection = 0 
    

def check_valid_position(snake_head, positions):
    """Checks if the snake is in a valid position.
    
    Args:
        snake_head (SnakeHead): The snake's head in snake game
        positions (list): positions of each segment of the snake
    """
    game_settings = Settings()
    if (positions[0] in positions[1:] or 
        snake_head.rect.centerx < 0 or 
        snake_head.rect.centerx > game_settings.x_dim or 
        snake_head.rect.centery < 0 or 
        snake_head.rect.centery > game_settings.y_dim):
        sys.exit()