# This class contains general settings for snake_game.
class Settings():
    
    def __init__(self):
        # Screen settings
        self.x_dim = 1200
        self.y_dim = 800
        self.title = 'Snake'

        # Snake sprite settings
        self.starting_body_length = 3
        self.size = [10, 10]
        self.head_color = 250, 20, 20
        self.body_color = 20, 250, 20

        # Other settings
        self.food_color = 20, 20, 250
