import pygame
from game_phases.start import Start
from game_phases.gameplay import Gameplay
from movements.ground_movement import GroundMovement
from movements.pipe_movement import PipeMovement


class GameManager():
    def __init__(self, screen_width, screen_height):
        self.screen_width = 480
        self.screen_height = 620

        self.start_phase = Start(screen_width, screen_height)
        self.gameplay_phase = Gameplay(screen_width, screen_height)
        self.ground_movement = GroundMovement(screen_width, screen_height)
        self.pipe_movement = PipeMovement(screen_width, screen_height)

        self.hover_speed = 0.25
        self.hover_range = 5
        self.hover_direction = 1
        self.current_hover = 0

        self.game_phase = "start"

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.game_phase = "gameplay"
                    self.gameplay_phase.handle_bird_fly(0, -10)
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.game_phase = "gameplay"
                self.gameplay_phase.handle_bird_fly(0, -20)

    def handle_game_state(self):
        if self.game_phase == "start":
            self.start_phase.update()

            self.current_hover += self.hover_speed * self.hover_direction
            if abs(self.current_hover) >= self.hover_range:
                self.hover_direction *= -1

        elif self.game_phase == "gameplay":
            self.gameplay_phase.update()
            self.gameplay_phase.bird.update()
            if not any(pygame.key.get_pressed()):
                self.gameplay_phase.handle_bird_fall()

            ground_collision = pygame.sprite.groupcollide(
                self.ground_movement.ground, self.gameplay_phase.bird, False, False
            )
            pipe_collision = pygame.sprite.groupcollide(
                self.gameplay_phase.pipe_movement.pipe, self.gameplay_phase.bird, False, False
            )
            if ground_collision or pipe_collision:
                pygame.quit()
