class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship Settings
        self.ship_speed = 8.5

        # Bullet Settings
        self.bullet_speed = 6.0
        self.bullet_width = 3
        self.bullet_height = 6
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3