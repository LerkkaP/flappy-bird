import pygame
from sprites.ground import Ground


class GroundMovement:
    """Class responsible for handling the ground movement

    Attributes:
        _screen_width: Width of the screen
        _ground_initial_x: Initial x-coordinate of the ground object
        _ground_initial_y: Initial y-coordinate of the ground object
        _speed: Speed in which the ground object moves --> controls the x-coordinate
        ground: Pygame sprite group for ground objects
    """

    def __init__(self, screen_width):
        """Initializes GroundMovement class

        Args:
            screen_width: Width of the screen
        """

        self._screen_width = screen_width

        self._ground_initial_x = 0
        self._ground_initial_y = 550
        self._speed = 2

        self.ground = pygame.sprite.Group()
        self.ground.add(Ground(self._speed,
                        self._ground_initial_x, self._ground_initial_y))

    def update_ground(self):
        """Updates the ground movement by adding new ground objects when needed"""
        last_ground = self.ground.sprites()[-1]
        if last_ground.rect.right < self._screen_width:
            new_ground_x = last_ground.rect.right
            self.ground.add(Ground(self._speed,
                            new_ground_x, self._ground_initial_y))

    def check_collision(self, bird_group):
        """Checks for collision between bird and ground

        Args:
            bird_group: Pygame sprite group containing bird objects

        Returns:
           bool: True if bird and ground collided, else False
        """
        ground_collision = pygame.sprite.groupcollide(
            self.ground, bird_group, False, False)
        return ground_collision
