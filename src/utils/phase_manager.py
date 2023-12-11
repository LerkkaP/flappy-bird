class PhaseManager():
    # Singleton pattern
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(PhaseManager, cls).__new__(cls)
            cls._phase = "start"
        return cls.instance

    def set_phase(self, phase):
        self._phase = phase

    def current_phase(self):
        return self._phase
    
    def game_end(self):
        if self._phase == "end":
            return True
        return False

