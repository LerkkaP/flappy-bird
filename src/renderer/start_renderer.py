from .mixin_renderer import RendererMixin


class StartRenderer(RendererMixin):
    """Class for rendering the start phase

    Args:
        RendererMixin: Mixin class RendererMixin to access common rendering functionalities

    Attributes:
        _display: Pygame display surface
        _game_manager: Instance of GameManager class
    """

    def __init__(self, display, game_manager):
        """Initialize StartRenderer class

        Args:
            display: Pygame display surface
            game_manager: GameManager class
        """
        super().__init__()
        self._display = display
        self._game_manager = game_manager

    def render_start(self):
        """Renders start screen
        """
        self._render_start_message()
        self.render_ground(self._game_manager.get_ground(), self._display)

    def _render_start_message(self):
        """Renders start message
        """
        start_message, start_message_coordinates = self._game_manager.get_start_message()
        start_message_x = start_message_coordinates[0]
        start_message_y = start_message_coordinates[1]

        hover_offset_y = start_message_y + self._game_manager.start_phase.current_hover
        self._display.blit(start_message, (start_message_x, hover_offset_y))
