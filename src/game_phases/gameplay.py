import pygame
from sprites.bird import Bird
from game_phases.start import Start
from movements.ground_movement import GroundMovement
from movements.pipe_movement import PipeMovement
from utils.asset_loader import AssetLoader


class Gameplay:
    def __init__(self, screen_width, screen_height):

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.bird = pygame.sprite.Group()
        self.bird.add(Bird(self.screen_width / 3, self.screen_height / 2))

        pygame.mixer.init()
        self.wing_sound = AssetLoader.load_sound("wing.wav")
        self.wing_sound.set_volume(0.2)

        self.ground_movement = GroundMovement(screen_width, screen_height)
        self.pipe_movement = PipeMovement(screen_width, screen_height)

    def update(self):
        self.ground_movement.ground.update()
        self.ground_movement.update_ground()

        self.pipe_movement.pipe.update()
        self.pipe_movement.update_pipe()

    def handle_bird_fly(self, dx, dy):
        for bird in self.bird.sprites():
            bird.fly(dx, dy)

        pygame.mixer.Sound.play(self.wing_sound)
        pygame.mixer.music.stop()

    def handle_bird_fall(self):
        for bird in self.bird.sprites():
            bird.fall()

    def handle_collision(self):

        ground_collision = pygame.sprite.groupcollide(
            self.ground_movement.ground, self.bird, False, False)

        pipe_collision = pygame.sprite.groupcollide(
            self.pipe_movement.pipe, self.bird, False, False
            )
        if ground_collision or pipe_collision:
                pygame.quit()

    #def handle_score(self):
        #if self.bird.rect.right == self.
