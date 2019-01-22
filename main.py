import pygame as pg
from box import Box
import sys

# Screen background color
BLACK = (0, 0, 0)
# Text color
WHITE = (255, 255, 255)
# Screen resolution
SIZE = (900, 900)


class Main:

    def __init__(self):
        # Pygame initialization methods
        pg.init()
        # Sets up a display window with 'SIZE' as the resolution
        self.screen = pg.display.set_mode(SIZE)
        # Sets the window title
        pg.display.set_caption('Bouncy Box')
        # Pygame clock variable
        self.clock = pg.time.Clock()
        # Main loop switch
        self.running = True
        # Infinite spawning loop
        self.infinite = False

        # Two text directions
        self.direct1 = Text('Press the Space bar for one', 300)
        self.direct2 = Text('Press Enter for a LOT', 600)

        # Pygame group that is used to update and draw all boxes at once
        self.all_boxes = pg.sprite.Group()

    # Main program loop
    def run(self):
        while self.running:
            # Ticks the clock 60 times per second, going through the loop every time
            self.clock.tick(60)
            self.events()
            self.updates()
            self.draw()

    # Pygame uses Event objects for things like keyboard and mouse input
    def events(self):
        # Every loop, this method goes through each Event object and reads them
        for event in pg.event.get():
            # Closes window if x button (not on keyboard) is pressed
            if event.type == pg.QUIT:
                sys.exit()
            # If space bar is pressed, creates a box
            elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                # Turns off infinite spawning switch
                self.infinite = False
                box = Box()
                self.all_boxes.add(box)
            # If enter is pressed, creates a box every loop until the space bar is pressed
            elif event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
                self.infinite = True

    def updates(self):
        # If the infinite switch is on, a box is created every loop
        if self.infinite:
            box = Box()
            self.all_boxes.add(box)
        # Calls the update method on all boxes
        self.all_boxes.update()
        # If any of the boxes go off the screen, they are reflected back
        for box in self.all_boxes.sprites():
            if box.rect.x < 0 or box.rect.right > SIZE[0]:
                # Randomizes the y velocity if it is too low
                if abs(box.vely < 1):
                    box.randomize_y()
                box.velx *= -1
            elif box.rect.y < 0 or box.rect.bottom > SIZE[1]:
                box.vely *= -1

    def draw(self):
        # Fills the screen with pure black
        self.screen.fill(BLACK)
        # Displays directions if there are no boxes
        if not self.all_boxes.sprites():
            self.screen.blit(self.direct1.text, (self.direct1.x, self.direct1.y))
            self.screen.blit(self.direct2.text, (self.direct2.x, self.direct2.y))
        # Draws all boxes to the screen
        self.all_boxes.draw(self.screen)
        # Refreshes the window once at the end of every loop to display everything
        pg.display.flip()


# Text display object
class Text:

    # Input message as the message displayed and y as the y coordinate
    def __init__(self, message, y):
        # Pygame font initialization
        pg.font.init()
        self.font = pg.font.SysFont('arial', 72)
        self.message = message
        self.y = y
        self.text = self.font.render(self.message, True, WHITE)

        # Creates a centered x coordinate
        rect = self.text.get_rect()
        self.x = (SIZE[0] - rect.width) / 2


m = Main()
m.run()
