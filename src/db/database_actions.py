from db.initialize_database import get_database_connection

db = get_database_connection()

def save_score(score):
    db.insert({"score": score})

def get_highest_score():
    scores = get_all_scores()
    highest_score = max(score['score'] for score in scores)
    return highest_score

# def average_score():

# def number_of_play_times()

def get_all_scores():
    scores = db.all()
    return scores
