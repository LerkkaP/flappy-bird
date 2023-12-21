import pygame
from utils.asset_loader import AssetLoader
from utils.phase_manager import PhaseManager
from .start_renderer import StartRenderer
from .gameplay_renderer import GameplayRenderer
from .end_renderer import EndRenderer
from .stats_renderer import StatsRenderer


class BaseRenderer:
    """Class responsible for rendering different phases of the game

    Attributes:
        _display: Pygame display surface
        _screen_width: Width of the screen
        _screen_height: Height of the screen
        start_renderer: Instance of StartRenderer for rendering the start phase
        gameplay_renderer: Instance of GameplayRenderer for rendering the gameplay phase
        end_renderer: Instance of EndRenderer for rendering the end phase
        stats_renderer: Instance of StatsRenderer for rendering the stats phase
        phase_manager: Instance of PhaseManager for managing different game phases
    """

    def __init__(self, display, screen_width, screen_height, game_manager):
        """Initialize BaseRenderer

        Args:
            display: Pygame display surface
            screen_width: Width of the screen
            screen_height: Height of the screen
            game_manager: Instance of the class GameManager
        """
        self._display = display
        self._screen_width = screen_width
        self._screen_height = screen_height
        self.start_renderer = StartRenderer(display, game_manager)
        self.gameplay_renderer = GameplayRenderer(display, screen_width, game_manager)
        self.end_renderer = EndRenderer(display, screen_width, game_manager)
        self.stats_renderer = StatsRenderer(display, screen_width)
        self.phase_manager = PhaseManager()

    def render_game(self):
        """Renders the background for the game and the current phase
        """
        self._render_background()
        self._render_phase()

    def _render_phase(self):
        """Render the current phase based on PhaseManager"""
        if self.phase_manager.game_in_start():
            self.start_renderer.render_start()
        elif self.phase_manager.game_in_gameplay():
            self.gameplay_renderer.render_gameplay()
        elif self.phase_manager.game_in_end():
            self.end_renderer.render_end()
        elif self.phase_manager.game_in_stats():
            self.stats_renderer.render_stats()

    def _render_background(self):
        """Render the background image
        """
        background_image = self._init_background_image()
        self._display.blit(background_image, (0, 0))

    def _init_background_image(self):
        """Initialize the background image for the game

        Returns:
            background image to be rendered
        """
        background_image = AssetLoader.load_image(
            "world", "background-day.png")
        background_image = pygame.transform.scale(
            background_image, (self._screen_width, self._screen_height))
        return background_image
