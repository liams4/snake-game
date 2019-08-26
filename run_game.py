import sys

import pygame

from settings import Settings
from snake import SnakeHead, SnakeBodySegment
from game_functions import (valid_position, add_body_segment, 
                           update_body_positions_and_directions, check_if_user_wants_to_play_again)
from food import Food
from scoreboard import Scoreboard
from end_of_game_options import PlayAgainButton, EndOfGameMessage


def run_game(high_score=0):
    """Driver function for Snake.
    
    Args:
        high_score (int): The high score of current game session.
            Defaults to 0.
    """
    pygame.init()

    game_settings = Settings()
    pygame.display.set_caption(game_settings.title)
    screen = pygame.display.set_mode((game_settings.x_dim, game_settings.y_dim))    
    
    snake_head = SnakeHead(screen)
    body_positions = [[snake_head.rect.centerx, snake_head.rect.centery]]
    body_directions = [[snake_head.xdirection, snake_head.ydirection]]
    for i in range(game_settings.body_length):
        body_positions.append([body_positions[i][0] - snake_head.dist_between_body_segments, snake_head.rect.centery])
        body_directions.append([snake_head.xdirection, snake_head.ydirection])

    food = Food(screen)
    score_board = Scoreboard(screen)
    while True:
        screen.fill(game_settings.background_color)
        snake_head.update_direction()
        snake_head.update_position()
        update_body_positions_and_directions(snake_head, body_positions, body_directions)

        score_board.draw_to_screen()  
        snake_head.draw_to_screen()
        food.draw_to_screen()
        for position in body_positions[1:]:
            body_segment = SnakeBodySegment(screen, position[0], position[1])
            body_segment.draw_to_screen()

        if not valid_position(snake_head, body_positions):
            break
        if pygame.sprite.collide_rect(snake_head, food):
            score_board.add_score()
            food = Food(screen)
            add_body_segment(snake_head, body_positions, body_directions)
    
        pygame.display.flip() # update screen
   
    end_of_game_message = EndOfGameMessage(screen, score_board.score, high_score)
    play_again_button = PlayAgainButton(screen)
    end_of_game_message.draw_to_screen()
    play_again_button.draw_to_screen()
    if score_board.score > high_score:
        high_score = score_board.score

    play_again = check_if_user_wants_to_play_again(play_again_button)
    if play_again:
        run_game(high_score)

run_game()
