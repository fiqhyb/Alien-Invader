class Setting():
    def __init__(self):
        #Screen Settings
        self.width = 1350
        self.height = 700
        self.color = (220,220,220)

        #Ship Settings
        self.ship_limit = 2

        #Bullet Settings
        self.bullet_width = 5
        self.bullet_height = 150
        self.bullet_color = 200,55,55
        self.bullets_allowed = 1000

        #Alien Settings
        self.drop_speed = 10

        #Game Speed Up
        self.speedup_scale = 1.1

        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        #INITIALIZE SETTING THAT CHANGE THROUGHOUT THE GAME.
        self.ship_speed = 1.5
        self.bullet_speed = 10
        self.alien_speed = 0.5
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points*self.score_scale)
        # print(self.alien_points)