import pygame

from settings import Settings
from snake import SnakeHead, SnakeBody
from game_functions import respond_to_input, check_valid_position
from food import Food

def run_game():
    """Driver function for snake-game.
    """
    pygame.init()

    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.x_dim, game_settings.y_dim))
    
    pygame.display.set_caption(game_settings.title)
    background_color = game_settings.background_color
    snake_head = SnakeHead(screen)

    body_positions = [[snake_head.rect.centerx, snake_head.rect.centery]]
    body_directions = [[snake_head.xdirection, snake_head.ydirection]]
    for i in range(game_settings.body_length):
        body_positions.append([body_positions[i][0] - snake_head.dist_between_body_segments, snake_head.rect.centery])
        body_directions.append([snake_head.xdirection, snake_head.ydirection])
    
    food = Food(screen)
    score = 0

    while True:
        screen.fill(background_color)
        respond_to_input(snake_head)
        snake_head.update(body_positions, body_directions)

        snake_head.draw_image()
        food.draw_image()        
        for position in body_positions[1:]:
            body_segment = SnakeBody(screen, game_settings, position[0], position[1])
            body_segment.draw_image()

        check_valid_position(snake_head, body_positions)
        if pygame.sprite.collide_rect(snake_head, food):
            score += 1
            food = Food(screen)
            snake_head.add_length(body_positions, body_directions)
    
        pygame.display.flip()


run_game()
