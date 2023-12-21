import pygame
from utils.asset_loader import AssetLoader


class SoundManager:
    """Class that handles sound related tasks

    Attributes:
        _mixer: Pygame mixer instance responsible for sound playback
        _sounds: dictionary that contains the loaded sounds
    """

    def __init__(self):
        """Initializes SoundManager class
        """
        self._mixer = pygame.mixer
        self._mixer.init()
        self._sounds = {
            "wing": AssetLoader.load_sound("wing.wav"),
            "die": AssetLoader.load_sound("die.wav"),
            "point": AssetLoader.load_sound("point.wav")
        }

        for sound in self._sounds.values():
            sound.set_volume(0.2)

    def play_sound(self, name):
        """Plays the given sound

        Args:
            name: Sound to be played
        """
        sound = self._sounds.get(name)
        sound.play()
        self._stop_sound()

    def _stop_sound(self):
        """Stops the playing sound
        """
        self._mixer.music.stop()
