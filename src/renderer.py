import pygame
from utils.asset_loader import AssetLoader
from utils.score import Score
from utils.phase_manager import PhaseManager
from game_phases.end import get_highest_score, End
from game_phases.stats import Stats


class Renderer:
    def __init__(self, display, screen_width, screen_height, game_manager):
        self._display = display
        self._screen_width = screen_width
        self._screen_height = screen_height
        self._game_manager = game_manager
        self.phase_manager = PhaseManager()
        self.score = Score()
        self._end_phase = End(screen_width)
        self.stats = Stats()

    def render_background(self):
        background_image = AssetLoader.load_image(
            "world", "background-day.png")
        background_image = pygame.transform.scale(
            background_image, (self._screen_width, self._screen_height))

        self._display.blit(background_image, (0, 0))

    def render_phase(self):
        if self.phase_manager.game_in_start():
            self._render_start_phase()
        elif self.phase_manager.game_in_gameplay():
            self._render_gameplay_phase()
        elif self.phase_manager.game_in_end():
            self._render_end_phase()
        elif self.phase_manager.game_in_stats():
            self._render_stats_phase()

    def _render_gameplay_phase(self):
        self._render_pipes()
        self._render_ground("gameplay")
        self._render_bird()
        self._render_score()

    def _render_start_phase(self):
        self._render_start_message()
        self._render_ground("start")

    def _render_stats_phase(self):
        self._display.blit(self.stats.draw_graph(), ((self._screen_width - 400) // 2, 10))  

    def _render_end_phase(self):
        self._render_pipes()
        self._render_ground("gameplay")
        self._render_bird()
        self._render_end_message()
        self._render_end_scores()
        self._render_buttons()

    def _render_start_message(self):
        hover_offset_y = self._game_manager.start_phase.start_message_y + \
            self._game_manager.start_phase.current_hover
        self._display.blit(self._game_manager.start_phase.start_message,
                           (self._game_manager.start_phase.start_message_x, hover_offset_y))

    def _render_end_message(self):
        self._display.blit(
            self._game_manager.end_phase.end_message,
            (
                self._game_manager.end_phase.end_message_x,
                self._game_manager.end_phase.end_message_y
            )
        )

    def _render_ground(self, phase):
        if phase == "gameplay":
            self._game_manager.gameplay_phase.ground_movement.ground.draw(
                self._display)
        elif phase == "start":
            self._game_manager.start_phase.ground_movement.ground.draw(
                self._display)

    def _render_pipes(self):
        self._game_manager.gameplay_phase.pipe_movement.pipe.draw(
            self._display)

    def _render_bird(self):
        self._game_manager.gameplay_phase.bird.draw(self._display)

    def _render_score(self):
        score = self.score.get_score()
        score_digits = list(str(score))
        for i, digit in enumerate(score_digits):
            image = AssetLoader.load_image("score", f"{digit}.png")
            self._display.blit(
                image,
                ((self._screen_width - image.get_width()) // 2 + i * 21, 50))

    def _render_highest_score(self):
        highest_score = get_highest_score()
        score_digits = list(str(highest_score))
        for i, digit in enumerate(score_digits):
            image = AssetLoader.load_image("score", f"{digit}.png")
            self._display.blit(
                image,
                ((self._screen_width - image.get_width()) // 2 + i * 21, 200))

    def _render_end_scores(self):
        self._render_score()
        self._render_highest_score()

    def _render_buttons(self):
        text_restart = self._end_phase.restart_text
        text_rect_restart = self._end_phase.restart_text_rect

        text_stats = self._end_phase.statistics_text
        text_rect_stats = self._end_phase.statistics_text_rect

        self._display.blit(text_restart, text_rect_restart)
        self._display.blit(text_stats, text_rect_stats)
