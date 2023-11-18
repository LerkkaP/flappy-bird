import pygame
import os

dirname = os.path.dirname(__file__)

class Ground(pygame.sprite.Sprite):
    def __init__(self, speed, screen_width, x, y):
        super().__init__()

        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets/images/world", "base.png")
        )

        self.rect = self.image.get_rect()
        self.speed = speed
        self.screen_width = screen_width
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x -= self.speed
        if self.rect.x <= -self.screen_width:
            self.kill()