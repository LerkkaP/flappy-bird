import random
import pygame
from sprites.pipe import Pipe
from utils.score import Score


class PipeMovement:
    """Class responsible for the pipe movement

    Attributes:
        _screen_width: Width of the screen
        _pipe_initial_x: Initial x-coordinate of pipe object
        _speed: Speed in which the pipe object is moving --> controls the x-coordinate
        _pipe_difference: The difference between top and bottom pipes
        --> the whole between the pipes
        score : Instance of the Score class
        _top_pipe_y: Y-coordinate for the top pipe --> 
        random number between -172 and 0 for the starting position
        _bottom_pipe_y: Y-coordinate for the bottom pipe, calculated with the help of top pipe
        _pipe = Pygame sprite group for pipe objects
    """

    def __init__(self, screen_width):
        """Initialize pipe movement

        Args:
            screen_width: Width of the screen
        """
        self._screen_width = screen_width

        self._pipe_initial_x = self._screen_width + 200
        self._speed = 2.5
        self._pipe_difference = 88
        self.score = Score()

        self._top_pipe_y = random.randint(-172, 0)
        self._bottom_pipe_y = self._top_pipe_y + 320 + self._pipe_difference
        self.pipe = pygame.sprite.Group()
        self._initialize_pipes()

    def _initialize_pipes(self):
        """Initialize the pipes
        """
        self.pipe.add(Pipe(self._speed,
                      self._pipe_initial_x, self._bottom_pipe_y, False))
        self.pipe.add(
            Pipe(self._speed, self._pipe_initial_x, self._top_pipe_y, True))

    def _add_pipe(self, x, y, is_top):
        """Adds pipe to the pipe sprite group

        Args:
            x: x-coordinate of the pipe
            y: Y-coordinate of the pipe
            is_top: Boolean value --> True if pipe is top pipe, else False
        """
        self.pipe.add(Pipe(self._speed, x, y, is_top))

    def update_pipe(self):
        """
        Updates the positions of existing pipes and 
        adds new pipes when the pipes closest to the bird reach a certain point on the screen

        Also resets the vertical positions for the top and bottom pipes to create
        gaps of a certain size between them
        """
        self._top_pipe_y = random.randint(-172, 0)
        self._bottom_pipe_y = self._top_pipe_y + 320 + self._pipe_difference
        last_pipe = self.pipe.sprites()[-1]

        if last_pipe.rect.left == 320:
            self._add_pipe(self._screen_width, self._bottom_pipe_y, False)
            self._add_pipe(self._screen_width, self._top_pipe_y, True)

    def update_score(self, sound_manager):
        """Updates the game score based on the position of the pipes

        The method checks the position of each pipe, and if a pipe reaches a certain 
        position, it increments the game score by one and plays a sound effect

        Args:
            sound_manager: SoundManager class to play sounds
        """
        for single_pipe in self.pipe.sprites():
            if single_pipe.rect.left == self._screen_width / 3 + 20:
                self.score.increment_score()
                sound_manager.play_sound("point")

    def check_collision(self, bird_group):
        """Checks for collisions between pipes and bird

        Args:
            bird_group: Pygame sprite group containing bird objects

        Returns:
           bool: True if bird and ground collided, else False
        """
        pipe_collision = pygame.sprite.groupcollide(
            self.pipe, bird_group, False, False)
        return pipe_collision

    def reset_pipes(self):
        """Resets the pipe positions and group at the start of a new game"""

        self.pipe.empty()
        self._top_pipe_y = random.randint(-172, 0)
        self._bottom_pipe_y = self._top_pipe_y + 320 + self._pipe_difference
        self._initialize_pipes()
