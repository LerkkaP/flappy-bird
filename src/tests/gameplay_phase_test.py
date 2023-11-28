import unittest
from unittest.mock import MagicMock
from game_phases.gameplay import Gameplay


class TestStartPhase(unittest.TestCase):

    def setUp(self):
        self.screen_width = 480
        self.screen_height = 620

        self.gameplay_phase = Gameplay(self.screen_width,  self.screen_height)

        self.mock_ground_movement = MagicMock()
        self.mock_pipe_movement = MagicMock()

        self.gameplay_phase.ground_movement = self.mock_ground_movement
        self.gameplay_phase.pipe_movement = self.mock_pipe_movement

    def test_start_phase_update_calls_ground_movement_methods(self):
        self.gameplay_phase.update()

        self.mock_ground_movement.ground.update.assert_called_once()
        self.mock_ground_movement.update_ground.assert_called_once()

        self.mock_pipe_movement.pipe.update.assert_called_once()
        self.mock_pipe_movement.update_pipe.assert_called_once()
