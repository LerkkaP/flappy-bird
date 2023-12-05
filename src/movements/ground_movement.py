import pygame
from sprites.ground import Ground


class GroundMovement:
    def __init__(self, screen_width):
        self._screen_width = screen_width

        self._ground_initial_x = 0
        self._ground_initial_y = 550
        self._speed = 2

        self.ground = pygame.sprite.Group()
        self.ground.add(Ground(self._speed,
                        self._ground_initial_x, self._ground_initial_y))

    def update_ground(self):
        last_ground = self.ground.sprites()[-1]
        if last_ground.rect.right < self._screen_width:
            new_ground_x = last_ground.rect.right
            self.ground.add(Ground(self._speed,
                            new_ground_x, self._ground_initial_y))

    def check_collision(self, bird_group):
        ground_collision = pygame.sprite.groupcollide(
            self.ground, bird_group, False, False)
        return ground_collision
