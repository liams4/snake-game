class Settings():
    """This class contains general settings for snake-game."""
    def __init__(self):
        # Screen settings
        self.x_dim = 900
        self.y_dim = 700
        self.title = 'Snake'
        self.background_color = (250, 250, 250)
        self.foreground_color = (0, 0, 0)
        self.button_color = (240, 240, 240)

        # Sprite settings
        self.body_length = 10
        self.size = [15, 15]
        self.head_color = 250, 20, 20
        self.body_color = 20, 250, 20
        self.food_color = 20, 20, 250
        self.dist_between_body_segments = 15
        self.starting_x_position = 200

        self.score_increment = 1
        self.font_size = 33
        