from game_phases.stats import Stats

class StatsRenderer():
    def __init__(self, display, screen_width):
        self._display = display
        self._screen_width = screen_width
        self._stats = Stats()

    def render_stats(self):
        self._render_graph()
        self._render_back_button()

    def _render_graph(self):
        self._display.blit(self._stats.draw_graph(), ((self._screen_width - 400) // 2, 100))  

    def _render_back_button(self):
        text_back = self._stats.back_button.text_render
        text_rect_back = self._stats.back_button.text_rect

        self._display.blit(text_back, text_rect_back)



