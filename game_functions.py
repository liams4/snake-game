import pygame
import sys

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