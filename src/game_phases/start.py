from movements.ground_movement import GroundMovement
from utils.asset_loader import AssetLoader

class Start:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.start_message = AssetLoader.load_image("messages", "start.png")
        self.start_message_x = ( self.screen_width - self.start_message.get_width()) // 2
        self.start_message_y = (self.screen_height - self.start_message.get_height()) // 2

        self.ground_movement = GroundMovement(screen_width, screen_height)

    def update(self):
        self.ground_movement.ground.update()
        self.ground_movement.update_ground()

    def render(self, display):
        self.ground_movement.ground.draw(display)
