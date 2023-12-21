class Score():
    """Class that handles score related tasks

    Attributes:
        score: Initial score
    """
    def __new__(cls):
        """Creates a new instance of the Score class if it doesn't exist using Singleton pattern"""
        if not hasattr(cls, 'instance'):
            cls.instance = super(Score, cls).__new__(cls)
            cls.score = 0
        return cls.instance

    def increment_score(self):
        """Increments score by one
        """

        self.score += 1

    def get_score(self):
        """Returns score

        Returns:
            Returns score in correct format
        """
        return int(self.score / 2)

    def reset_score(self):
        """Resets score
        """
        self.score = 0
