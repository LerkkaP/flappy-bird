import pygame
from utils.asset_loader import AssetLoader
from utils.phase_manager import PhaseManager
from .start_renderer import StartRenderer
from .gameplay_renderer import GameplayRenderer
from .end_renderer import EndRenderer
from .stats_renderer import StatsRenderer

class BaseRenderer:
    def __init__(self, display, screen_width, screen_height, game_manager):
        self._display = display
        self._screen_width = screen_width
        self._screen_height = screen_height
        self.start_renderer = StartRenderer(display, game_manager)
        self.gameplay_renderer = GameplayRenderer(display, screen_width, game_manager)
        self.end_renderer = EndRenderer(display, screen_width, game_manager)
        self.stats_renderer = StatsRenderer(display, screen_width)
        self.phase_manager = PhaseManager()

    def render_game(self):
        self._render_background()
        self._render_phase()

    def _render_phase(self):
        if self.phase_manager.game_in_start():
            self.start_renderer.render_start()
        elif self.phase_manager.game_in_gameplay():
            self.gameplay_renderer.render_gameplay()
        elif self.phase_manager.game_in_end():
            self.end_renderer.render_end()
        elif self.phase_manager.game_in_stats():
            self.stats_renderer.render_stats()

    def _render_background(self):
        background_image = self._init_background_image()
        self._display.blit(background_image, (0, 0))

    def _init_background_image(self):
        background_image = AssetLoader.load_image(
            "world", "background-day.png")
        background_image = pygame.transform.scale(
            background_image, (self._screen_width, self._screen_height))
        return background_image
    
