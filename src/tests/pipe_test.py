import unittest
from sprites.pipe import Pipe
from movements.pipe_movement import PipeMovement

speed = 2
screen_width = 480
screen_height = 620
pipe_initial_x = screen_width + 200
pipe_initial_y = 550


class TestPipe(unittest.TestCase):
    def setUp(self):
        self.pipe_sprite = Pipe(
            speed, screen_width, screen_height, pipe_initial_x, pipe_initial_y, False)
        self.pipe_movement = PipeMovement(screen_width, screen_height)

    def test_if_pipes_are_moving(self):
        self.pipe_sprite.update()

        self.assertEqual(self.pipe_sprite.rect.x, pipe_initial_x - speed)
