import pygame
from utils.asset_loader import AssetLoader


class Ground(pygame.sprite.Sprite):
    def __init__(self, speed, screen_width, x, y):
        super().__init__()

        self.image = AssetLoader.load_image("world", "base.png")

        self.rect = self.image.get_rect()
        self.speed = speed
        self.screen_width = screen_width
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()
