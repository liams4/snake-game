import pygame
from settings import Settings
from snake import SnakeHead, SnakeBody
from game_functions import *
from food import Food

def run_game():
    pygame.init()

    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.x_dim, game_settings.y_dim))
    pygame.display.set_caption(game_settings.title)
    background_color = game_settings.background_color
    snake_head = SnakeHead(screen, game_settings)

    positions = [[snake_head.rect.centerx, snake_head.rect.centery]]
    for i in range(game_settings.length):
        positions.append([positions[i][0] - 15, snake_head.rect.centery])
    
    food = Food(screen)
    food.draw_image()
    score = 0

    while True:
        screen.fill(background_color)
        respond_to_input(snake_head)
        snake_head.update(positions)
        snake_head.draw_image()
        food.draw_image()
        for position in positions[1:]:
            body_segment = SnakeBody(screen, game_settings, position[0], position[1])
            body_segment.draw_image()

        check_valid_position(snake_head, positions)
        if pygame.sprite.collide_rect(snake_head, food):
            score += 1
            food = Food(screen)
            food.draw_image()
            game_settings.length += 1
        print(score)
        print(game_settings.length)

        pygame.display.flip()



run_game()
