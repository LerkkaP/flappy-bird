import unittest
from sprites.bird import Bird


class TestBird(unittest.TestCase):
    def setUp(self):
        self.screen_width = 480
        self.screen_height = 620

        self.initial_x = self.screen_width / 3
        self.initial_y = self.screen_height / 2

        self.bird = Bird(self.initial_x, self.initial_y)

    def test_if_bird_can_fly(self):
        self.bird.fly(0, -20)

        self.assertEqual(self.bird._velocity, -7)

        self.assertEqual(self.bird.rect.y, self.initial_y - 20)
        self.assertEqual(self.bird.rect.x, self.initial_x)

    def test_if_bird_can_fall(self):
        self.bird.fall()

        self.assertEqual(self.bird.rect.y, self.initial_y + 3)
        self.assertEqual(self.bird.rect.x, self.initial_x)
