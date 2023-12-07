class Score():
    def __init__(self):
        self.score = 0

    def increment_score(self):
        self.score += 1

    def get_score(self):
        return int(self.score / 2) 
    
    def reset_score(self):
        self.score = 0

global_score = Score()