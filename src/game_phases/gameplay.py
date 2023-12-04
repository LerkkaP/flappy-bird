import pygame
from sprites.bird import Bird
from movements.ground_movement import GroundMovement
from movements.pipe_movement import PipeMovement
from utils.sound_manager import SoundManager


class Gameplay:
    def __init__(self, screen_width, screen_height):

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.bird = pygame.sprite.Group()
        self.bird.add(Bird(160, self.screen_height / 2))

        self.sound_manager = SoundManager()

        self.ground_movement = GroundMovement(screen_width, screen_height)
        self.pipe_movement = PipeMovement(screen_width, screen_height)
        self.pause = False
        self.score = 0

    def update(self):
        self.ground_movement.ground.update()
        self.ground_movement.update_ground()

        self.pipe_movement.pipe.update()
        self.pipe_movement.update_pipe()
        score_updated = self.pipe_movement.update_score()

        if score_updated:
            self.score = self._get_score()
            self.sound_manager.play_sound("point")
            self.sound_manager.stop_sound()

    def _get_score(self):
        return self.pipe_movement.return_score()

    def get_current_score(self):
        return self.score

    def handle_bird_fly(self, dx, dy):
        for bird in self.bird.sprites():
            bird.fly(dx, dy)

        self.sound_manager.play_sound("wing")
        self.sound_manager.stop_sound()

    def handle_bird_fall(self):

        if not self._ground_collision():
            for bird in self.bird.sprites():
                bird.fall()

    def handle_collision(self):

        if self._ground_collision() or self._pipe_collision():
            self.sound_manager.play_sound("die")
            self.sound_manager.stop_sound()

            self.ground_movement.move = False
            self.pipe_movement.move = False
            self.pause = True

    def _ground_collision(self):
        ground_collision = pygame.sprite.groupcollide(
            self.ground_movement.ground, self.bird, False, False)
        return ground_collision

    def _pipe_collision(self):
        pipe_collision = pygame.sprite.groupcollide(
            self.pipe_movement.pipe, self.bird, False, False)
        return pipe_collision
