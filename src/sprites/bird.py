import pygame
from utils.asset_loader import AssetLoader


class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.sprites = [AssetLoader.load_image(
            "bird", f"bluebird-{i}.png") for i in ["upflap", "midflap", "downflap"]]

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.velocity = 0
        self.gravity = 0.2
        self.angle = 30

    def update(self):
        self.current_sprite += 0.1

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[int(self.current_sprite)]

        self._apply_gravity()

    def _apply_gravity(self):
        self.velocity += self.gravity
        self.rect.y += self.velocity

        if self.velocity < 0:
            self.angle = 30
            self._rotate_bird()
        else:
            self.gravity = 0.3
            if self.angle >= -90:
                self.angle -= 5
            self.image = self.sprites[1]
            self._rotate_bird()

    def _rotate_bird(self):
        self.image = pygame.transform.rotate(self.image, self.angle)

    def fly(self, dx, dy):
        self.rect.move_ip(dx, dy)
        self.velocity = -7

    def fall(self):
        self.rect.move_ip(0, 3)
