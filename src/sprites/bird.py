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

        self._velocity = 0
        self._gravity = 0.2
        self._angle = 30

    def update(self):
        self.current_sprite += 0.1

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[int(self.current_sprite)]

        self._apply_gravity()

    def _apply_gravity(self):
        self._velocity += self._gravity
        self.rect.y += self._velocity

        if self._velocity < 0:
            self._angle = 30
            self._rotate_bird()
        else:
            self._gravity = 0.3
            if self._angle >= -90:
                self._angle -= 5
            self.image = self.sprites[1]
            self._rotate_bird()

    def _rotate_bird(self):
        self.image = pygame.transform.rotate(self.image, self._angle)

    def rotate_bird(self):
        self.image = pygame.transform.rotate(self.image, -120)

    def fly(self, dx, dy):
        self.rect.move_ip(dx, dy)
        self._velocity = -7

    def fall(self):
        self.rect.move_ip(0, 3)

    def reset_position(self, x, y):
            
        self.rect.x = x
        self.rect.y = y
        self._velocity = 0  
        self._gravity = 0.2
        self._angle = 30