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

    def test_bird_update(self):
        initial_sprite = self.bird.current_sprite
        self.bird.update()
        updated_sprite = self.bird.current_sprite
        self.assertNotEqual(initial_sprite, updated_sprite)

    def test_bird_reset(self):
        self.bird.reset_position(200, 300)
        self.assertEqual(self.bird.rect.x, 200)
        self.assertEqual(self.bird.rect.y, 300)
        self.assertEqual(self.bird._velocity, 0)
        self.assertEqual(self.bird._gravity, 0.2)
        self.assertEqual(self.bird._angle, 30)
