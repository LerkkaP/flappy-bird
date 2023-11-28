import pygame
from sprites.bird import Bird
from game_phases.start import Start
from movements.ground_movement import GroundMovement
from movements.pipe_movement import PipeMovement
from utils.asset_loader import AssetLoader


class Gameplay:
    def __init__(self, screen_width, screen_height):

        self.start_phase = Start(screen_width, screen_height)
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.bird = pygame.sprite.Group()
        self.bird.add(Bird(self.screen_width / 3, self.screen_height / 2))

        self.wing_sound = AssetLoader.load_sound("wing.wav")
        self.wing_sound.set_volume(0.2)

        self.ground_movement = GroundMovement(screen_width, screen_height)
        self.pipe_movement = PipeMovement(screen_width, screen_height)

    def update(self):
        self.ground_movement.ground.update()
        self.ground_movement.update_ground()

        self.pipe_movement.pipe.update()
        self.pipe_movement.update_pipe()

    def fly(self, dx=0, dy=0):
        for bird in self.bird.sprites():
            bird.rect.move_ip(dx, dy)
            bird.velocity = -7

            pygame.mixer.Sound.play(self.wing_sound)
            pygame.mixer.music.stop()

    def fall(self, dx=0, dy=3):
        for bird in self.bird.sprites():
            bird.rect.move_ip(dx, dy)
