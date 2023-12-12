import pygame
from utils.asset_loader import AssetLoader


class Pipe(pygame.sprite.Sprite):
    """Class representing pipes

    Attributes:
        image: Pipe image
        rect: Rect object of the pipe image
        speed: Speed at which the pipe moves horizontally
        x: X-coordinate of the pipe's starting position
        y: Y-coordinate of the pipe's starting position
        flip: Boolean value indicating whether the pipe needs to be flipped
    """
    def __init__(self, speed, x, y, flip):
        """Initialize pipe object

        Args:
            speed: Speed at which the pipe moves horizontally
            x: X-coordinate of the pipe's starting position
            y: Y-coordinate of the pipe's starting position
            flip: Boolean value indicating whether the pipe needs to be flipped
        """
        super().__init__()

        self.image = AssetLoader.load_image("world", "pipe-green.png")

        self.rect = self.image.get_rect()
        self._speed = speed
        self.rect.x = x
        self.rect.y = y

        if flip:
            self.image = pygame.transform.rotate(self.image, 180)

    def update(self):
        """Updates pipe position and destroys it if fully passes screen
        """
        self.rect.x -= self._speed
        if self.rect.right < 0:
            self.kill()
