import pygame

class Scoreboard():

    def __init__(self, screen:
        """Initializes a new scoreboard object."""

        self.screen = screen
        self.score = 0
    
    def update_score(self, increment=1):
        """Increments the score.

        Args:
            increment (int): the value to increase the score by.
        """
        self.score += increment
