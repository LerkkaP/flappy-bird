import pygame
import unittest
from event_handler import EventHandler
from game_phases.gameplay import Gameplay
from game_phases.end import End
from game_phases.stats import Stats
from utils.phase_manager import PhaseManager
from utils.score import Score


class TestEventHandler(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen_width = 480
        self.screen_height = 620
        self.gameplay_phase = Gameplay(self.screen_width, self.screen_height)
        self.end_phase = End(self.screen_width)
        self.stats_phase = Stats()
        self.phase_manager = PhaseManager()
        self.score = Score()
        self.event_handler = EventHandler(
            self.phase_manager,
            self.gameplay_phase,
            self.end_phase,
            self.stats_phase,
            self.score
        )

    def test_that_initial_game_phase_is_start_and_after_key_press_gameplay(self):
        self.assertEqual(self.event_handler._phase_manager.game_in_start(), True)

        key_press = pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_SPACE})
        pygame.event.post(key_press)

        self.event_handler.handle_events()

        self.assertEqual(
            self.event_handler._phase_manager.game_in_gameplay(), True)

    def test_start_events(self):
        click_mouse = pygame.event.Event(pygame.MOUSEBUTTONDOWN, {'button': 1})
        pygame.event.post(click_mouse)

        self.event_handler._handle_start_events(click_mouse)
        self.assertEqual(
            self.event_handler._phase_manager.game_in_gameplay(), True)

        click_space = pygame.event.Event(
            pygame.KEYDOWN, {'key': pygame.K_SPACE})
        pygame.event.post(click_space)

        self.event_handler._handle_start_events(click_space)
        self.assertEqual(
            self.event_handler._phase_manager.game_in_gameplay(), True)

    def test_that_game_is_restarted(self):
        self.event_handler._restart_game()
        self.assertEqual(self.event_handler._phase_manager.game_in_start(), True)
