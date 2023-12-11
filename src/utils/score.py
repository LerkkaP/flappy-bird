class Score():
    # Singleton pattern
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Score, cls).__new__(cls)
            cls.score = 0
        return cls.instance

    def increment_score(self):
        self.score += 1

    def get_score(self):
        return int(self.score / 2)
    
    def reset_score(self):
        self.score = 0