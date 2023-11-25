import pygame
import os

dirname = os.path.dirname(__file__)

class Pipe(pygame.sprite.Sprite):
    def __init__(self, speed, screen_width, screen_height, x, y, flip):
        super().__init__()

        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets/images/world", "pipe-green.png")
        )
        self.rect = self.image.get_rect()
        self.speed = speed
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.rect.x = x
        self.rect.y = y

        if flip:
            self.image = pygame.transform.rotate(self.image, 180)
            
    def update(self):
        self.rect.x -= self.speed
        if self.rect.x <= -self.screen_width:
            self.kill()
