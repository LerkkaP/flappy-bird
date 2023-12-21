import unittest
from sprites.pipe import Pipe
from movements.pipe_movement import PipeMovement
from utils.score import Score

speed = 2
screen_width = 480
screen_height = 620
pipe_initial_x = screen_width + 200
pipe_initial_y = 550


class TestPipe(unittest.TestCase):
    def setUp(self):
        self.score = Score()
        self.pipe_movement = PipeMovement(screen_width)

    def test_if_score_is_initially_zero(self):
        initial_score = self.score.get_score()
        self.assertEqual(initial_score, 0)

    def test_increment_score(self):
        self.score.increment_score()
        updated_score = self.score.get_score()
        self.assertEqual(updated_score, 1)

    def test_reset_score(self):
        self.score.increment_score()
        self.score.reset_score()
        reset_score = self.score.get_score()
        self.assertEqual(reset_score, 0)

    def test_if_score_is_updated_correctly(self):
        pipe_bottom = Pipe(speed,
                           screen_width / 3 + 20, pipe_initial_y, False)
        pipe_top = Pipe(speed, screen_width / 3 +
                        20, pipe_initial_y - 320 - self.pipe_movement._pipe_difference, True)

        self.pipe_movement.pipe.add(pipe_bottom)
        self.pipe_movement.pipe.add(pipe_top)

        self.pipe_movement.update_score()

        updated_score = self.score.get_score()
        self.assertEqual(updated_score, 1)
