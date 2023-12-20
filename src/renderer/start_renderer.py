
class StartRenderer():
    def __init__(self, display, game_manager):
        self._display = display
        self._game_manager = game_manager

    def render_start(self):
        self._render_start_message()
        self._render_ground()
        
    def _render_start_message(self):
        hover_offset_y = self._game_manager.start_phase.start_message_y + \
            self._game_manager.start_phase.current_hover
        self._display.blit(self._game_manager.start_phase.start_message,
                           (self._game_manager.start_phase.start_message_x, hover_offset_y))

    def _render_ground(self):
        self._game_manager.start_phase.ground_movement.ground.draw(
                self._display)


