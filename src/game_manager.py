from game_phases.start import Start
from game_phases.gameplay import Gameplay
from game_phases.end import End
from game_phases.stats import Stats
from utils.phase_manager import PhaseManager
from utils.score import Score
from event_handler import EventHandler


class GameManager():
    """Class for managing the game

    Attributes:
        start_phase: Instance of Start class
        gameplay_phase: Instance of Gameplay class
        end_phase: Instance of End class
        stats_phase: Instance of Stats class
        score: Instance of Score class
        event_handler: Instance of EventHandler class
    """

    def __init__(self, screen_width, screen_height):
        """Initializes GameManager class

        Args:
            screen_width: Width of the screen
            screen_height: Height of the screen
        """
        self.start_phase = Start(screen_width, screen_height)
        self.gameplay_phase = Gameplay(screen_width, screen_height)
        self.end_phase = End(screen_width)
        self.stats_phase = Stats()
        self.phase_manager = PhaseManager()
        self.score = Score()
        self.event_handler = EventHandler(
            self.phase_manager,
            self.start_phase,
            self.gameplay_phase,
            self.end_phase,
            self.stats_phase,
            self.score
        )

    def handle_events(self):
        """Handles events
        """
        self.event_handler.handle_events()

    def _restart_game(self):
        """Sets game back to restart phase
        """
        self.phase_manager.set_phase("start")
        self.gameplay_phase.reset_bird()
        self.gameplay_phase.pipe_movement.reset_pipes()
        self.score.reset_score()

    def handle_game_state(self):
        """Handles game state
        """
        if self.phase_manager.game_in_start():
            self.start_phase.update()
            self.start_phase.handle_text_hover()
        elif self.phase_manager.game_in_gameplay():
            self._update_gameplay()
        elif self.phase_manager.game_in_end():
            self._update_gameplay()

    def _update_gameplay(self):
        """Updates gameplay
        """
        if not self.phase_manager.game_in_end():
            self.gameplay_phase.update()
            self.gameplay_phase.bird.update()
            self.gameplay_phase.handle_collision()

        self.gameplay_phase.handle_bird_fall()

    def get_pipes(self):
        """Returns group of pipe objects

        Returns:
            Pygame sprite group of pipe objects
        """
        return self.gameplay_phase.pipe_movement.pipe

    def get_ground(self):
        """Returns group of ground objects

        Returns:
            Pygame sprite group of ground objects
        """
        if self.phase_manager.game_in_start():
            return self.start_phase.ground_movement.ground
        return self.gameplay_phase.ground_movement.ground

    def get_bird(self):
        """Returs group of bird objects

        Returns:
            Pygame sprite group of bird objects
        """
        return self.gameplay_phase.bird

    def get_end_message(self):
        """Returns the end message

        Returns:
            End message and its x and y coordinates
        """
        return (
            self.end_phase.end_message,
            (self.end_phase.end_message_x, self.end_phase.end_message_y)
        )

    def get_start_message(self):
        """Returns the start message

        Returns:
            Start message and its x and y coordinates
        """
        return (
            self.start_phase.start_message,
            (self.start_phase.start_message_x, self.start_phase.start_message_y)
        )
