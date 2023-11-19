import pygame
from sprites.ground import Ground
from sprites.bird import Bird

class Start:
    def __init__(self, screen_width, screen_height):
        self.SCREEN_WIDTH = screen_width
        self.SCREEN_HEIGHT = screen_height

        # ground
        self.ground_initial_x = 0
        self.ground_initial_y = 550
        self.speed = 2
        self.ground = pygame.sprite.Group()
        self.ground.add(Ground(self.speed, self.SCREEN_WIDTH, self.ground_initial_x, self.ground_initial_y))

    def update_ground(self):
        last_ground = self.ground.sprites()[-1]
        if last_ground.rect.right < self.SCREEN_WIDTH:
            new_ground_x = last_ground.rect.right
            self.ground.add(Ground(self.speed, self.SCREEN_WIDTH, new_ground_x, self.ground_initial_y))

    

        