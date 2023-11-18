import pygame
import os

dirname = os.path.dirname(__file__)

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets/images/bird", "base.png")
        )

        self.rect = self.image.get_rect()