import pygame
from utils.asset_loader import AssetLoader


class Pipe(pygame.sprite.Sprite):
    def __init__(self, speed, x, y, flip):
        super().__init__()

        self.image = AssetLoader.load_image("world", "pipe-green.png")

        self.rect = self.image.get_rect()
        self._speed = speed
        self.rect.x = x
        self.rect.y = y

        if flip:
            self.image = pygame.transform.rotate(self.image, 180)

    def update(self):
        self.rect.x -= self._speed
        if self.rect.right < 0:
            self.kill()
