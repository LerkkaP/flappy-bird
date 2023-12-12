import pygame
from utils.asset_loader import AssetLoader


class Bird(pygame.sprite.Sprite):
    """Class representing bird

    Attributes:
        sprites: List containing images of the bird in different flapping positions
        current_sprite: Current flap position index
        image: Bird image in current flap position
        rect.x: The x-coordinate of the top-left corner of the bird's rectangular area
        rect.y: The y-coordinate of the top-left corner of the bird's rectangular area
        _velocity: Current vertical velocity of the bird
        _gravity: Gravity applied to the bird to simulate falling
        _angle: Current angle representing the bird's tilt

    """

    def __init__(self, x, y):
        """Initialize bird object

        Args:
            x: X-coordinate of the bird's starting position
            y: Y-coordinate of the bird's starting position
        """
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
        """Updates the bird's flapping animation and applies gravity"""
        self.current_sprite += 0.1

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[int(self.current_sprite)]

        self._apply_gravity()

    def _apply_gravity(self):
        """Applies gravitational force to the bird and handles its tilting"""
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
        """Rotates the bird
        """
        self.image = pygame.transform.rotate(self.image, self._angle)

    def fly(self, dx, dy):
        """Handles the bird's upward movement"""
        self.rect.move_ip(dx, dy)
        self._velocity = -7

    def fall(self):
        """Simulates the bird's falling
        """
        self.rect.move_ip(0, 3)

    def reset_position(self, x, y):
        """Resets the bird's position to given coordinates

        Args:
            x: The x-coordinate to reset to
            y: The y-coordinate to reset to
        """

        self.rect.x = x
        self.rect.y = y
        self._velocity = 0
        self._gravity = 0.2
        self._angle = 30
