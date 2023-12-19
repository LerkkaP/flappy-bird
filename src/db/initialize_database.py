import os
from tinydb import TinyDB

dirname = os.path.dirname(__file__)
db = TinyDB(os.path.join(dirname, "..", "data", "scores.json"))


def get_database_connection():
    """Retrieve the connection to the database

    Returns:
        Database object to be interacted with
    """
    return db
