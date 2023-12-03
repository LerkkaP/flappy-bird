import pygame
from sprites.bird import Bird
from movements.ground_movement import GroundMovement
from movements.pipe_movement import PipeMovement
from utils.asset_loader import AssetLoader


class Gameplay:
    def __init__(self, screen_width, screen_height):

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.bird = pygame.sprite.Group()
        self.bird.add(Bird(160, self.screen_height / 2))

        # Sounds
        self._mixer = pygame.mixer
        self._mixer.init()
        self._wing_sound = AssetLoader.load_sound("wing.wav")
        self._wing_sound.set_volume(0.2)

        self._die_sound = AssetLoader.load_sound("die.wav")
        self._die_sound.set_volume(0.2)

        self._point_sound = AssetLoader.load_sound("point.wav")
        self._point_sound.set_volume(0.2)

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
            self._mixer.Sound.play(self._point_sound)
            self._mixer.music.stop()

    def _get_score(self):
        return self.pipe_movement.return_score()
    
    def get_current_score(self):
        return self.score

    def handle_bird_fly(self, dx, dy):
        for bird in self.bird.sprites():
            bird.fly(dx, dy)

        self._mixer.Sound.play(self._wing_sound)
        self._mixer.music.stop()

    def handle_bird_fall(self):

        if not self._ground_collision():
            for bird in self.bird.sprites():
                bird.fall()

    def handle_collision(self):

        if self._ground_collision() or self._pipe_collision():
            self._mixer.Sound.play(self._die_sound)
            self._mixer.music.stop()

            self.ground_movement.move = False
            self.pipe_movement.move = False
            self.pause = True

    def _ground_collision(self):
        ground_collision = pygame.sprite.groupcollide(
        self.ground_movement.ground, self.bird, False, False)
        return ground_collision

    def _pipe_collision(self):
        pipe_collision = pygame.sprite.groupcollide(self.pipe_movement.pipe, self.bird, False, False)
        return pipe_collision
        