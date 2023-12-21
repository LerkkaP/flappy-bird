import unittest
from db.database_actions import save_score, get_highest_score, get_all_scores, db


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
