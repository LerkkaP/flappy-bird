from db.initialize_database import get_database_connection

db = get_database_connection()


def save_score(score):
    """Saves score in the databaes

    Args:
        score: Score to be saved in the database
    """
    db.insert({"score": score})


def get_highest_score():
    """Returns highest score saved in the database

    Returns:
        Highest score
    """
    scores = get_all_scores()
    highest_score = max(score['score'] for score in scores)
    return highest_score


def get_all_scores():
    """Returns all scores in the database

    Returns:
        Returns all scores
    """
    scores = db.all()
    return scores

def get_number_of_items():
    scores = get_all_scores()
    return len(scores)

def get_list_of_scores():
    scores = get_all_scores()
    return [score["score"] for score in scores]

