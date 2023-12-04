import pygame
from utils.asset_loader import AssetLoader


class Renderer:
    def __init__(self, display, screen_width, screen_height, game_manager):
        self._display = display
        self._screen_width = screen_width
        self._screen_height = screen_height
        self._game_manager = game_manager

    def render_background(self):
        background_image = AssetLoader.load_image(
            "world", "background-day.png")
        background_image = pygame.transform.scale(
            background_image, (self._screen_width, self._screen_height))

        self._display.blit(background_image, (0, 0))

    def render_phase(self):
        if self._game_manager.game_phase == "start":
            self._render_start_phase()
        elif self._game_manager.game_phase == "gameplay":
            self._render_gameplay_phase()

    def _render_gameplay_phase(self):
        self._render_pipes()
        self._render_ground("gameplay")
        self._render_bird()
        self._render_score()

    def _render_start_phase(self):
        self._render_start_message()
        self._render_ground("start")

    def _render_start_message(self):
        hover_offset_y = self._game_manager.start_phase.start_message_y + \
            self._game_manager.start_phase.current_hover
        self._display.blit(self._game_manager.start_phase.start_message,
                           (self._game_manager.start_phase.start_message_x, hover_offset_y))

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
        score = self._game_manager.gameplay_phase.get_current_score()

        scores = list(str(score))
        for i, digit in enumerate(scores):
            image = AssetLoader.load_image("score", f"{digit}.png")
            self._display.blit(
                image,
                ((self._screen_width - image.get_width()) // 2 + i * 21, 50))
