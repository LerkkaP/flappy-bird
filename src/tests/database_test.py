import unittest
from db.database_actions import db
from db.database_actions import save_score
from db.database_actions import get_highest_score
from db.database_actions import get_number_of_items
from db.database_actions import get_list_of_scores

class TestDatabaseActions(unittest.TestCase):

    def setUp(self):
        db.truncate()

    def test_get_highest_score(self):
        save_score(5)
        save_score(15)
        save_score(8)

        highest_score = get_highest_score()
        self.assertEqual(highest_score, 15)

    def test_get_highest_score_duplicates(self):
        save_score(5)
        save_score(5)
        save_score(5)

        highest_score = get_highest_score()
        self.assertEqual(highest_score, 5)

    def test_get_number_of_items_returns_number_of_saved_scores(self):
        save_score(5)
        save_score(5)
        save_score(5)

        scores = get_number_of_items()
        self.assertEqual(scores, 3)

    def test_get_list_of_scores_returns_scores_as_list(self):
        save_score(5)
        save_score(5)
        save_score(5)

        scores = get_list_of_scores()
        self.assertLessEqual(scores, [5, 5, 5])
