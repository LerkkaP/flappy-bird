from db.initialize_database import get_database_connection

db = get_database_connection()

def save_score(score):
    """Saves score in the databaes

    Args:
        score: Score to be saved in the database
    """
    db.insert({"score": score})

def get_highest_score():
    """Retrieve the highest score saved in the database

    Returns:
        The highest score found in the database
    """
    scores = get_all_scores()
    highest_score = max(score['score'] for score in scores)
    return highest_score


def get_all_scores():
    """Retrieve all scores stored in the database

    Returns:
        A list containing all scores stored in the database
    """
    scores = db.all()
    return scores

def get_number_of_items():
    """Retrieve the total number of scores saved in the database

    Returns:
        The number of scores stored in the database
    """
    scores = get_all_scores()
    return len(scores)

def get_list_of_scores():
    """Retrieve a list of all scores stored in the database

    Returns:
        A List of scores stored in the database
    """
    scores = get_all_scores()
    return [score["score"] for score in scores]

