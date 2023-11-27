import pygame
from sprites.ground import Ground


class GroundMovement:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.ground_initial_x = 0
        self.ground_initial_y = 550
        self.speed = 2

        self.ground = pygame.sprite.Group()
        self.ground.add(Ground(self.speed, self.screen_width,
                        self.ground_initial_x, self.ground_initial_y))

    def update_ground(self):
        last_ground = self.ground.sprites()[-1]
        if last_ground.rect.right < self.screen_width:
            new_ground_x = last_ground.rect.right
            self.ground.add(Ground(self.speed, self.screen_width,
                            new_ground_x, self.ground_initial_y))
