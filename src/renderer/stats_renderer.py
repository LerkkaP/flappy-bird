from game_phases.stats import Stats
from utils.text import Text


class StatsRenderer():
    """Class for rendering the stats phase

    Attributes:
        _display: Pygame display surface
        screen_width: Width of the screen
        _stats: Instance of Stats class
        text: Instance of Text class
    """

    def __init__(self, display, screen_width):
        """Initializes StatsRenderer class

        Args:
            display: Pygame display surface
            screen_width: Width of the screen
        """
        self._display = display
        self._screen_width = screen_width
        self._stats = Stats()
        self.text = Text(screen_width)

    def render_stats(self):
        """Renders stats screen
        """
        self._render_graph()
        self._render_back_button()

    def _render_graph(self):
        """Renders graph
        """
        graph_position = ((self._screen_width - 400) // 2, 100)
        self._display.blit(self._stats.draw_graph(), (graph_position))

    def _render_back_button(self):
        """Renders BACK button
        """
        back_text_render, back_text_rect = self.text.back_button()
        self._display.blit(back_text_render, back_text_rect)
