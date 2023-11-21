import pygame
from sprites.ground import Ground
import os 

dirname = os.path.dirname(__file__)

class Start:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.start_message = pygame.image.load(os.path.join(dirname, "..",  "assets/images/messages", "start.png"))
        self.start_message_x = ( self.screen_width - self.start_message.get_width()) // 2
        self.start_message_y = (self.screen_height - self.start_message.get_height()) // 2

    

        