import random
import pygame
from sprites.pipe import Pipe
from utils.score import Score
from utils.sound_manager import SoundManager

class PipeMovement:
    def __init__(self, screen_width):
        self._screen_width = screen_width

        self._pipe_initial_x = self._screen_width + 200
        self._speed = 2.5
        self._pipe_difference = 88
        self._sound_manager = SoundManager()
        self.score = Score()

        self._top_pipe_y = random.randint(-172, 0)
        self._bottom_pipe_y = self._top_pipe_y + 320 + self._pipe_difference
        self.pipe = pygame.sprite.Group()
        self._initialize_pipes()

    def _initialize_pipes(self):
        self.pipe.add(Pipe(self._speed,
                      self._pipe_initial_x, self._bottom_pipe_y, False))
        self.pipe.add(
            Pipe(self._speed, self._pipe_initial_x, self._top_pipe_y, True))

    def _add_pipe(self, x, y, is_top):
        self.pipe.add(Pipe(self._speed, x, y, is_top))

    def update_pipe(self):
        self._top_pipe_y = random.randint(-172, 0)
        self._bottom_pipe_y = self._top_pipe_y + 320 + self._pipe_difference
        last_pipe = self.pipe.sprites()[-1]

        if last_pipe.rect.left == 320:
            self._add_pipe(self._screen_width, self._bottom_pipe_y, False)
            self._add_pipe(self._screen_width, self._top_pipe_y, True)

    def update_score(self):
        for single_pipe in self.pipe.sprites():
            if single_pipe.rect.left == self._screen_width / 3 + 20:
                self.score.increment_score()
                self._sound_manager.play_sound("point")

    def check_collision(self, bird_group):
        pipe_collision = pygame.sprite.groupcollide(
            self.pipe, bird_group, False, False)
        return pipe_collision
