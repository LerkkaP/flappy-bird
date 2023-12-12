import pygame
from game_phases.start import Start
from game_phases.gameplay import Gameplay
from game_phases.end import End
from utils.phase_manager import PhaseManager
from utils.score import Score

class GameManager():
    def __init__(self, screen_width, screen_height):
        self.start_phase = Start(screen_width, screen_height)
        self.gameplay_phase = Gameplay(screen_width, screen_height)
        self.end_phase = End(screen_width)
        self.phase_manager = PhaseManager()
        self.score = Score()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            self._handle_gameplay_events(event)

    def _handle_gameplay_events(self, event):
        if self.phase_manager.current_phase() == "start":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.phase_manager.set_phase("gameplay")
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.phase_manager.set_phase("gameplay")
        if self.phase_manager.current_phase() == "gameplay":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.gameplay_phase.handle_bird_fly(0, -10)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.gameplay_phase.handle_bird_fly(0, -20)
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.end_phase.handle_restart_click(mouse_pos):
                        self.phase_manager.set_phase("start")
                        for bird in self.gameplay_phase.bird:
                            bird.reset_position(160, 620 / 2)
                        self.gameplay_phase.pipe_movement.reset_pipes()
                        self.score.reset_score()

    def handle_game_state(self):
        if self.phase_manager.current_phase() == "start":
            self.start_phase.update()
            self.start_phase.handle_text_hover()
        elif self.phase_manager.current_phase() == "gameplay":
            self._update_gameplay()
        elif self.phase_manager.current_phase() == "end":
            self._update_gameplay()

    def _update_gameplay(self):
        if not self.phase_manager.game_end():
            self.gameplay_phase.update()
            self.gameplay_phase.bird.update()
            self.gameplay_phase.handle_collision()

        if not any(pygame.key.get_pressed()):
            self.gameplay_phase.handle_bird_fall()

