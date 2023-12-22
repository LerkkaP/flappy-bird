import sys
import pygame


class EventHandler:
    """Class for managing events in the game

    Attributes:
        _phase_manager: Instance of PhaseManager class
        _gameplay_phase: Instance of Gameplay class
        _end_phase: Instance of End class
        _stats_phase: Instance of Stats class
        _score: Instance of Score class
    """

    def __init__(self, phase_manager, gameplay_phase, end_phase, stats_phase, score):
        """Initializes EventHandler class

        Args:
            phase_manager: PhaseManager class
            gameplay_phase: Gameplay class
            end_phase: End class
            stats_phase: Stats class
            score: Score class
        """
        self._phase_manager = phase_manager
        self._gameplay_phase = gameplay_phase
        self._end_phase = end_phase
        self._stats_phase = stats_phase
        self._score = score

    def handle_events(self):
        """Handles events
        """
        for event in pygame.event.get():
            self._handle_quit_event(event)
            self._handle_game_events(event)

    def _handle_quit_event(self, event):
        """Handles quit events

        Args:
            event: event triggered by the user
        """
        if event.type == pygame.QUIT:
            self._handle_quit()

    def _handle_quit(self):
        """Handles quitting by shutting down the game and the system
        """
        pygame.quit()
        sys.exit()  # sys.exit() is for removing pygame error: display Surface quit

    def _handle_game_events(self, event):
        """Handles game events

        Args:
            event: event triggered by the user
        """
        if self._phase_manager.game_in_start():
            self._handle_start_events(event)
        if self._phase_manager.game_in_gameplay():
            self._handle_gameplay_events(event)
        else:
            self._handle_end_events(event)

    def _handle_start_events(self, event):
        """Handles start events

        Args:
            event: event triggered by the user
        """
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self._phase_manager.set_phase("gameplay")
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self._phase_manager.set_phase("gameplay")

    def _handle_gameplay_events(self, event):
        """Handles events in the gameplay phase

        Args:
            event: event triggered by the user
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self._gameplay_phase.handle_bird_fly(0, -10)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self._gameplay_phase.handle_bird_fly(0, -20)

    def _handle_end_events(self, event):
        """Handles events in the end phase

        Args:
            event: event triggered by the user
        """
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if self._end_phase.handle_restart_click(mouse_pos):
                self._restart_game()
            elif self._end_phase.handle_statistics_click(mouse_pos):
                self._phase_manager.set_phase("stats")
            elif self._stats_phase.handle_back_click(mouse_pos):
                self._phase_manager.set_phase("end")

    def _restart_game(self):
        """Restarts the game
        """
        self._phase_manager.set_phase("start")
        self._gameplay_phase.reset_bird()
        self._gameplay_phase.pipe_movement.reset_pipes()
        self._score.reset_score()
