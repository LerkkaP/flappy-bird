import pygame
import os

dirname = os.path.dirname(__file__)

class AssetLoader():
    @staticmethod
    def load_image(type, file):
        return pygame.image.load(
        os.path.join(dirname, "..", f"assets/images/{type}", file)
    )
        
    @staticmethod
    def load_sound(file):
        return pygame.mixer.Sound(os.path.join(dirname, "..", "assets/sounds/", file))   
                
