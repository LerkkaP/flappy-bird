import pygame
from utils.asset_loader import AssetLoader


class Ground(pygame.sprite.Sprite):
    """Class representing ground

    Attributes:
        image: Ground image
        rect: Rect object of the ground image
        speed: Speed at which the ground moves horizontally
        rect.x: The x-coordinate of the top-left corner of the ground's rectangular area
        rect.y: The y-coordinate of the top-left corner of the ground's rectangular area


    """
    def __init__(self, speed, x, y):
        """Initialize ground object

        Args:
            speed: Speed at which the ground moves horizontally
            x: X-coordinate of the ground's starting position
            y: Y-coordinate of the ground's starting position
        """
        super().__init__()

        self.image = AssetLoader.load_image("world", "base.png")

        self.rect = self.image.get_rect()
        self._speed = speed
        self.rect.x = x
        self.rect.y = y

    def update(self):
        """Updates groun position and destroys it if fully passes screen
        """
        self.rect.x -= self._speed
        if self.rect.right < 0:
            self.kill()
