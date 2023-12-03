import random
import pygame
from sprites.pipe import Pipe


class PipeMovement:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.pipe_initial_x = self.screen_width + 200
        self.speed = 2.5
        self.pipe_difference = 88

        self.top_pipe_y = random.randint(-172, 0)
        self.bottom_pipe_y = self.top_pipe_y + 320 + self.pipe_difference

        self.pipe = pygame.sprite.Group()
        self.pipe.add(Pipe(self.speed, self.screen_width, self.screen_height,
                      self.pipe_initial_x, self.bottom_pipe_y, False))
        self.pipe.add(Pipe(self.speed, self.screen_width,
                      self.screen_height, self.pipe_initial_x, self.top_pipe_y, True))
        self.score = 0
        

    def update_pipe(self):
        self.top_pipe_y = random.randint(-172, 0)
        self.bottom_pipe_y = self.top_pipe_y + 320 + self.pipe_difference
        last_pipe = self.pipe.sprites()[-1]


        if last_pipe.rect.left == 320:
            self.pipe.add(Pipe(self.speed, self.screen_width, self.screen_height,
                          self.screen_width, self.bottom_pipe_y, False))
            self.pipe.add(Pipe(self.speed, self.screen_width,
                          self.screen_height, self.screen_width, self.top_pipe_y, True))

    def update_score(self):
        previous_score = self.score
        for single_pipe in self.pipe.sprites():
            if single_pipe.rect.left == self.screen_width / 3 + 20: 
                self.score += 1

        return self.score != previous_score

    def return_score(self):
        return int(self.score / 2)