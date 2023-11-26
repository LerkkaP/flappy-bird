import pygame
from utils.asset_loader import AssetLoader

class Pipe(pygame.sprite.Sprite):
    def __init__(self, speed, screen_width, screen_height, x, y, flip):
        super().__init__()

        self.image = AssetLoader.load_image("world", "pipe-green.png")

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
