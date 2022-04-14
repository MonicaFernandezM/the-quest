class Settings:
 
    def __init__(self):

        # Screen Settings
        self.screen_width = 1000
        self.screen_height = 750
        self.background_image = 'images/polar-lights-ga4cf63a15_1920.jpg'

        # Ship Settings
        self.ship_velocity = 1
        self.max_ship_velocity = 10
        self.ship_image = 'images/icons8-lanzadera-de-espacio-96.png'

        # Asteroid Settings
        self.asteroid_images = [
            'images/icons8-astronauta-96.png', 
            'images/icons8-baby-yoda-96.png', 
            'images/icons8-ciencia-ficción-96.png', 
            'images/icons8-cometa-96.png', 
            'images/icons8-estrella-de-la-muerte-96.png', 
            'images/icons8-extraterrestre-96.png',
            'images/icons8-grey-96.png',
            'images/icons8-planeta-96.png',
            'images/icons8-satélites-96.png',
            'images/icons8-stormtrooper-96.png']
        self.max_image_size = 80 
        self.min_image_size = 25
        self.max_asteroid_velocity = 2
        self.min_asteorid_velocity = 10 


        # Game Settings
        self.FPS = 60
        self.max_game_time = 60
        self.lives = 3
        self.max_asteroid = 15
        self.game_time = 60
        self.bar_height = 50
        self.image_explosion = [ 
            'images/icons8-flash-bang-48.png',
            'images/icons8-flash-bang-96.png',
            'images/icons8-explosión-de-fuegos-artificiales-96.png',
            'images/icons8-explosión-de-fuegos-artificiales-48.png']
        