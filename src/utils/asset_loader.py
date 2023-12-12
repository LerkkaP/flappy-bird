import os
import pygame

dirname = os.path.dirname(__file__)


class AssetLoader():
    """Class for loading images and sounds"""

    @staticmethod
    def load_image(file_type, file):
        """Loads an image file

        Args:
            file_type: Specifies the category of image
            file: The specific file to be downloaded

        Returns:
            The loaded image
        """
        return pygame.image.load(
            os.path.join(dirname, "..", f"assets/images/{file_type}", file)
        )

    @staticmethod
    def load_sound(file):
        """Loads a sound file

        Args:
            file: The specific sound file to be loaded

        Returns:
            The loaded sound
        """
        return pygame.mixer.Sound(os.path.join(dirname, "..", "assets/sounds/", file))
