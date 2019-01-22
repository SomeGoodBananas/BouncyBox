import pygame as pg
import random

# Screen center position
CENTER = (450, 450)


# Box is a Pygame sprite object
class Box(pg.sprite.Sprite):

    MAX_SPEED = 7.0
    MAX_ANGLE = 7.0

    def __init__(self):
        # Pygame sprite object initialization
        pg.sprite.Sprite.__init__(self)

        # Creates a Pygame surface
        self.image = pg.Surface((40, 40))
        # Fills the image with a random color, uses the rgb scale
        color = (random.randint(0, 230), random.randint(0, 230), random.randint(0, 230))
        self.image.fill(color)
        # Creates a Pygame rect object from the surface that can be used to control the sprite position
        self.rect = self.image.get_rect()
        # Sets the position to the center of the screen
        self.rect.center = CENTER

        # Velocity x and y variables
        self.velx = 0
        self.vely = 0
        self.randomize_velocity()

    # Randomizes the x and y velocity on creation
    def randomize_velocity(self):
        # Randomizes x velocity based on the max speed
        self.velx = random.uniform(-Box.MAX_SPEED, Box.MAX_SPEED)
        # Randomizes y velocity based on the max angle
        self.vely = random.uniform(-Box.MAX_ANGLE, Box.MAX_ANGLE)

        # If the box is moving too slow, then it randomizes again
        if abs(self.velx) < 1 or abs(self.vely) < .5:
            self.randomize_velocity()

    # Randomizes just the y velocity
    def randomize_y(self):
        # Randomizes y velocity based on the max angle
        self.vely = random.uniform(-Box.MAX_ANGLE, Box.MAX_ANGLE)

    # Method that updates the box position every loop
    def update(self):
        # Moves box
        self.rect.x += self.velx
        self.rect.y += self.vely
