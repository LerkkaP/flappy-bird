from game_phases.stats import Stats
from utils.text import Text

class StatsRenderer():
    def __init__(self, display, screen_width):
        self._display = display
        self._screen_width = screen_width
        self._stats = Stats()
        self.text = Text(screen_width)

    def render_stats(self):
        self._render_graph()
        self._render_back_button()

    def _render_graph(self):
        self._display.blit(self._stats.draw_graph(), ((self._screen_width - 400) // 2, 100))  

    def _render_back_button(self):
        back_text_render, back_text_rect = self.text.back_button()
        self._display.blit(back_text_render, back_text_rect)




