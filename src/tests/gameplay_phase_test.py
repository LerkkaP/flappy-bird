import unittest
from unittest.mock import MagicMock
from game_phases.gameplay import Gameplay


class TestGameplayPhase(unittest.TestCase):

    def setUp(self):
        self.screen_width = 480
        self.screen_height = 620

        self.gameplay_phase = Gameplay(self.screen_width,  self.screen_height)

        self.mock_ground_movement = MagicMock()
        self.mock_pipe_movement = MagicMock()
        self.mock_bird = MagicMock()

        self.gameplay_phase.ground_movement = self.mock_ground_movement
        self.gameplay_phase.pipe_movement = self.mock_pipe_movement
        self.gameplay_phase.bird = self.mock_bird

    def test_that_update_calls_ground_movement_methods(self):     
        self.gameplay_phase.update()

        self.mock_ground_movement.ground.update.assert_called_once()
        self.mock_ground_movement.update_ground.assert_called_once()

    def test_that_update_calls_pipe_movement_methods(self):
        self.gameplay_phase.update()

        self.mock_pipe_movement.pipe.update.assert_called_once()
        self.mock_pipe_movement.update_pipe.assert_called_once()

    def test_that_update_calls_pipe_movement_score(self):
        self.gameplay_phase.update()

        self.mock_pipe_movement.update_score.assert_called_once()

    def test_that_handle_collision_checks_ground_collision(self):
        self.gameplay_phase.handle_collision()

        self.mock_ground_movement.check_collision(self.mock_bird)

    def test_that_handle_collision_check_pipe_collision(self):
        self.gameplay_phase.handle_collision()

        self.mock_pipe_movement.check_collision(self.mock_bird)
