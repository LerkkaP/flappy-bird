import pygame
import random
from sprites.pipe import Pipe

class PipeMovement:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.pipe_initial_x = self.screen_width + 200
        self.pipe_inital_y = 450
        self.speed = 2.5
        
        self.pipe = pygame.sprite.Group()
        #self.pipe.add(Pipe(self.speed, self.screen_width, self.screen_height ,self.pipe_initial_x, self.pipe_inital_y, False))
        self.pipe.add(Pipe(self.speed, self.screen_width, self.screen_height ,self.pipe_initial_x, 0, True, 450))

    def update_pipe(self):
        height = random.randint(100, 360)
        last_pipe = self.pipe.sprites()[-1]
        if last_pipe.rect.left == 290:
            #self.pipe.add(Pipe(self.speed, self.screen_width, self.screen_height, self.screen_width, self.pipe_inital_y, False))
            self.pipe.add(Pipe(self.speed, self.screen_width, self.screen_height, self.screen_width, 0, True, height))

    #def calculate_pipes(self):
        #height = random.randint(100, 360)


        
'''
    The pipe height varies randomly but it must be so that the hole
    where the bird flies from is not too big and not too small.
    The pipes have fixed y position but their x position changes.
    Once a pipe is over the screen it is destroyed. New pipes must come in a way
    where the gap between for example the bottom pipe and new pipe is some fixed value.
'''