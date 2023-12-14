class PhaseManager():
    """Class for managin the game phases

    Attributes:
        _phase = current phase of the gameplay -> initially start
    """
    def __new__(cls):
        """Creates a new instance of the Score class if it doesn't exist using Singleton pattern"""
        if not hasattr(cls, 'instance'):
            cls.instance = super(PhaseManager, cls).__new__(cls)
            cls._phase = "start"
        return cls.instance

    def set_phase(self, phase):
        """Sets the game phase

        Args:
            phase: game phase to be changed to
        """
        self._phase = phase

    def game_in_start(self):
        """Check if the game is currently in the start phase

        Returns:
            bool: True if the game is in the start phase, else False
        """
        return self._phase == "start"

    def game_in_gameplay(self):
        """Check if the game is currently in the gameplay phase

        Returns:
            bool: True if the game is in the gameplay phase, else False
        """
        return self._phase == "gameplay"

    def game_in_end(self):
        """Checks if the game is currently in the end phase

        Returns:
            bool: True if the game is in the end phase, else False
        """
        return self._phase == "end"

    def game_in_stats(self):
        return self._phase == "stats"