import pygame
from sprites.bird import Bird
from movements.ground_movement import GroundMovement
from movements.pipe_movement import PipeMovement
from utils.sound_manager import SoundManager
from utils.phase_manager import PhaseManager
from utils.score import Score
from db.database_actions import save_score


class Gameplay:
    """Class for managing the gameplay phase of the game

    Attributes:
        _screen_width: Width of the screen
        _screen_height: Height of the screen
        _bird: Pygame sprite group for bird objects
        _sound_manager: Instance of SoundManager class
        score: Instance of score class
        ground_movement: Instance of GroundMovement class
        pipe_movement: Instance of PipeMovement class
        phase_manager: Instance of Phase_manager class
    """

    def __init__(self, screen_width, screen_height):
        """Initialize gameplay phase

        Args:
            screen_width: Width of the screen
            screen_height: Height of the screen
        """
        self._screen_width = screen_width
        self._screen_height = screen_height

        self._init_bird()
        self._init_game_elements()

    def _init_bird(self):
        """Initialize bird sprites
        """
        self.bird = pygame.sprite.Group()
        self.bird.add(Bird(160, self._screen_height / 2))

    def _init_game_elements(self):
        """Initialize game elements"""
        self._sound_manager = SoundManager()
        self.score = Score()
        self.ground_movement = GroundMovement(self._screen_width)
        self.pipe_movement = PipeMovement(self._screen_width)
        self.phase_manager = PhaseManager()

    def update(self):
        """Update elements related to gameplay phase"""
        self._update_ground()
        self._update_pipes()

    def _update_ground(self):
        """Update ground"""
        self.ground_movement.ground.update()
        self.ground_movement.update_ground()

    def _update_pipes(self):
        """Update pipes and score that is related to pipe"""
        self.pipe_movement.pipe.update()
        self.pipe_movement.update_pipe()
        self.pipe_movement.update_score(self._sound_manager)

    def handle_bird_fly(self, dx, dy):
        """Handle bird's flying movement

        Args:
            dx: Horizontal movement --> This stays constant
            dy: Vertical movement
        """
        for bird in self.bird.sprites():
            bird.fly(dx, dy)

        self._sound_manager.play_sound("wing")

    def handle_bird_fall(self):
        """Handle bird's falling movement
        """
        if not self.ground_movement.check_collision(self.bird):
            for bird in self.bird.sprites():
                bird.fall()

    def handle_collision(self):
        """Handle collision related logic"""
        ground_collision = self.ground_movement.check_collision(self.bird)
        pipe_collision = self.pipe_movement.check_collision(self.bird)

        if ground_collision or pipe_collision:
            self._handle_collision_environment()

    def _handle_collision_environment(self):
        """Handle collision environment
        """
        self._sound_manager.play_sound("die")
        self.ground_movement.move = False
        self.pipe_movement.move = False
        self.phase_manager.set_phase("end")
        save_score(self.score.get_score())

    def reset_bird(self):
        """Reset the bird's position
        """
        for bird in self.bird:
            bird.reset_position(160, self._screen_height / 2)
