"""This module contains functions that are used to help run Snake."""
import sys

import pygame

from settings import Settings
    

def valid_position(snake_head, positions):
    """Checks if the snake is in a valid position.
    
    Args:
        snake_head (SnakeHead): The snake's head
        positions (list): positions of each body segment of the snake

    Returns:
        True if the snake head's position is valid, False if it is not.
    """
    game_settings = Settings()
    return not (positions[0] in positions[1:] or 
        snake_head.rect.centerx < 0 or 
        snake_head.rect.centerx > game_settings.x_dim or 
        snake_head.rect.centery < 0 or 
        snake_head.rect.centery > game_settings.y_dim)

def add_body_segment(snake_head, body_positions, body_directions):
    """Adds a body segment to the snake.
    
    Args:
        positions (list): the position of each the head and body segment of the snake
        directions (list): the directions of each the headbody segment of the snake
    """
    location = [body_positions[-1][0], body_positions[-1][0] + 1]
    if body_directions[-1][0] == 1:
        location = [body_positions[-1][0] - 1, body_positions[-1][0]]
    elif body_directions[-1][0] == -1:
        location = [body_positions[-1][0] + 1, body_positions[-1][0]]
    elif body_directions[-1][1] == 1:
        location = [body_positions[-1][0], body_positions[-1][0] - 1]

    body_positions.append(location)
    body_directions.append([snake_head.xdirection, snake_head.ydirection])

def update_body_positions_and_directions(snake_head, body_positions, body_directions):
    """Updates the position and direction of each body segment of the
        snake.
    
    Args:
        body_positions (list): the positions of each body segment
        body_directions (list): the directions of each body segment
    """
    for i in range(len(body_positions) - 1, 0, -1):
        body_positions[i] = body_positions[i - 1]
        body_directions[i] = body_directions[i - 1]
    body_positions[0] = [snake_head.rect.centerx, snake_head.rect.centery]
    body_directions[0] = [snake_head.xdirection, snake_head.ydirection]

def check_if_user_wants_to_play_again(play_again_button):
    """Returns True if the user wants to play again.
    
    Args:
        play_again_button (Button): the button that the user clicks if
            they want to play again
    """
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_location = pygame.mouse.get_pos()
                if play_again_button.rect.collidepoint(click_location):
                    return True
            elif event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()
        