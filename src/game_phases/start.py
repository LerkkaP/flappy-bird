from movements.ground_movement import GroundMovement
from utils.asset_loader import AssetLoader


class Start:
    def __init__(self, screen_width, screen_height):
        self._screen_width = screen_width
        self._screen_height = screen_height
        self.ground_movement = GroundMovement(screen_width)

        self._init_start_message()
        self._init_hover_attributes()

    def _init_start_message(self):
        self.start_message = AssetLoader.load_image("messages", "start.png")
        self.start_message_x = (
            self._screen_width - self.start_message.get_width()) // 2
        self.start_message_y = (self._screen_height -
                                self.start_message.get_height()) // 2

    def _init_hover_attributes(self):
        self.hover_speed = 0.25
        self.hover_range = 5
        self.hover_direction = 1
        self.current_hover = 0

    def update(self):
        self.ground_movement.ground.update()
        self.ground_movement.update_ground()

    def handle_text_hover(self):

        self.current_hover += self.hover_speed * self.hover_direction
        if abs(self.current_hover) >= self.hover_range:
            self.hover_direction *= -1
