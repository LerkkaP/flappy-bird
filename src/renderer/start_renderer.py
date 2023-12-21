from .mixin_renderer import RendererMixin


class StartRenderer(RendererMixin):
    def __init__(self, display, game_manager):
        super().__init__()
        self._display = display
        self._game_manager = game_manager

    def render_start(self):
        self._render_start_message()
        self.render_ground(self._game_manager.get_ground(), self._display)

    def _render_start_message(self):
        start_message, start_message_coordinates = self._game_manager.get_start_message()
        start_message_x = start_message_coordinates[0]
        start_message_y = start_message_coordinates[1]

        hover_offset_y = start_message_y + self._game_manager.start_phase.current_hover
        self._display.blit(start_message, (start_message_x, hover_offset_y))
