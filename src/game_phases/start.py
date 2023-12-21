from movements.ground_movement import GroundMovement
from utils.asset_loader import AssetLoader


class Start:
    """Class for managing the start phase of the game

     Attributes:
        _screen_width: Width of the screen
        _screen_height: Height of the screen
        ground_movement: Instance of GroundMovement class
        start_message: Starting image
        start_message_x: X-coordinate of the start message on the screen
        start_message_y: Y-coordinate of the start message on the screen
        hover_direction: Direction of text hovering
        current_hover: Current position offset for text hovering    """

    def __init__(self, screen_width, screen_height):
        """Initializes Start class

        Args:
            screen_width: Width of the screen
            screen_height: Height of the screen
        """
        self._screen_width = screen_width
        self._screen_height = screen_height
        self.ground_movement = GroundMovement(screen_width)

        self._init_start_message()
        self._init_hover_attributes()

    def _init_start_message(self):
        """Initializes start message attributes
        """
        self.start_message = AssetLoader.load_image("messages", "start.png")
        self.start_message_x = (
            self._screen_width - self.start_message.get_width()) // 2
        self.start_message_y = (self._screen_height -
                                self.start_message.get_height()) // 2

    def _init_hover_attributes(self):
        """Initializes hover attributes for start message
        """
        self.hover_direction = 1
        self.current_hover = 0

    def update(self):
        """Updates start phase objects --> ground movement
        """
        self.ground_movement.ground.update()
        self.ground_movement.update_ground()

    def handle_text_hover(self):
        """Handles the text hovering
        """

        self.current_hover += 0.25 * self.hover_direction
        if abs(self.current_hover) >= 5:
            self.hover_direction *= -1
