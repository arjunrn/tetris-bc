import unittest
from block import Block


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.block = Block()

    def test_movement(self):
        original_mask = self.block.mask()

        self.block.rotate_clockwise()
        self.block.move_right(True)

        self.block.rotate_clockwise()
        self.block.move_right(True)

        self.block.rotate_counter()
        self.block.move_left(True)

        self.block.rotate_counter()
        self.block.move_left(True)

        new_mask = self.block.mask()
        self.assertEqual(original_mask, new_mask)


if __name__ == '__main__':
    unittest.main()
