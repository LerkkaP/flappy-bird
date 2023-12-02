import pygame
from game_phases.start import Start
from game_phases.gameplay import Gameplay


class GameManager():
    def __init__(self, screen_width, screen_height):
        self.screen_width = 480
        self.screen_height = 620

        self.start_phase = Start(screen_width, screen_height)
        self.gameplay_phase = Gameplay(screen_width, screen_height)

        self.hover_speed = 0.25
        self.hover_range = 5
        self.hover_direction = 1
        self.current_hover = 0

        self.game_phase = "start"
        self.score = 0

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
            self.gameplay_phase.handle_collision()
            #self.gameplay_phase.handle_score(self.score)

            if not any(pygame.key.get_pressed()):
                self.gameplay_phase.handle_bird_fall()
