import unittest
from sprites.ground import Ground
from movements.ground_movement import GroundMovement

speed = 2
screen_width = 480
screen_height = 620
ground_initial_x = 0
ground_initial_y = 550


class TestGround(unittest.TestCase):
    def setUp(self):
        self.ground_sprite = Ground(
            speed, screen_width, ground_initial_x, ground_initial_y)
        self.ground_movement = GroundMovement(screen_width, screen_height)

    def test_if_ground_is_moving(self):
        self.ground_sprite.update()

        self.assertEqual(self.ground_sprite.rect.x, ground_initial_x - speed)

    def test_if_new_ground_sprite_is_added_when_ground_exceeds_display_width(self):
        sprites_count_initial = len(self.ground_movement.ground.sprites())

        self.ground_movement.update_ground()

        sprites_count_updated = len(self.ground_movement.ground.sprites())

        self.assertEqual(sprites_count_updated, sprites_count_initial + 1)
