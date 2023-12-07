import pygame
from sprites.bird import Bird
from movements.ground_movement import GroundMovement
from movements.pipe_movement import PipeMovement
from utils.sound_manager import SoundManager

class Gameplay:
    def __init__(self, screen_width, screen_height):

        self._screen_height = screen_height

        self.bird = pygame.sprite.Group()
        self.bird.add(Bird(160,self._screen_height / 2))

        self._sound_manager = SoundManager()

        self.ground_movement = GroundMovement(screen_width)
        self.pipe_movement = PipeMovement(screen_width)
        self.pause = False

    def update(self):
        self.ground_movement.ground.update()
        self.ground_movement.update_ground()

        self.pipe_movement.pipe.update()
        self.pipe_movement.update_pipe()
        score_updated = self.pipe_movement.update_score()

        if score_updated:
            self._sound_manager.play_sound("point")
            self._sound_manager.stop_sound()

    def handle_bird_fly(self, dx, dy):
        for bird in self.bird.sprites():
            bird.fly(dx, dy)

        self._sound_manager.play_sound("wing")
        self._sound_manager.stop_sound()

    def handle_bird_fall(self):

        if not self.ground_movement.check_collision(self.bird):
            for bird in self.bird.sprites():
                bird.fall()

    def handle_collision(self):
        ground_collision = self.ground_movement.check_collision(self.bird)
        pipe_collision = self.pipe_movement.check_collision(self.bird)

        if ground_collision or pipe_collision:
            self._sound_manager.play_sound("die")
            self._sound_manager.stop_sound()

            self.ground_movement.move = False
            self.pipe_movement.move = False
            self.pause = True
