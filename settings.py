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
        self.ship_limit = 1

        # Bullet Settings
        self.bullet_speed = 6.0
        self.bullet_width = 800
        self.bullet_height = 6
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien Settings
        self.alien_speed = 20.0
        self.fleet_drop_speed = 20.0
        # fleet_deirection of 1 represents right; -1 represents left.
        self.fleet_direction = 1
